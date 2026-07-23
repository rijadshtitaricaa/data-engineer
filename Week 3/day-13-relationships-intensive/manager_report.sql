-- 1. Which courses have the most enrollments?

SELECT
    c.course_name,
    COUNT(e.enrollment_id) AS total_enrollments
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id
ORDER BY total_enrollments DESC;


-- 2. Which students are active in more than one course?

SELECT
    s.full_name,
    COUNT(e.course_id) AS active_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.status = 'active'
GROUP BY s.student_id
HAVING COUNT(e.course_id) > 1;


-- 3. Which course has the strongest average attendance?

SELECT
    c.course_name,
    AVG(
        CASE 
            WHEN a.status = 'Present' THEN 1 
            ELSE 0 
        END
    ) * 100 AS attendance_percentage
FROM courses c
JOIN enrollments e
ON c.course_id = e.course_id
JOIN attendance a
ON e.enrollment_id = a.enrollment_id
GROUP BY c.course_id
ORDER BY attendance_percentage DESC
LIMIT 1;


-- 4. Which course has the weakest assignment completion?

SELECT
    c.course_name,
    COUNT(sub.submission_id) AS completed_submissions
FROM courses c
JOIN assignments a
ON c.course_id = a.course_id
LEFT JOIN submissions sub
ON a.assignment_id = sub.assignment_id
AND sub.status = 'Submitted'
GROUP BY c.course_id
ORDER BY completed_submissions ASC;


-- 5. Which students need attention because of missing/late submissions?

SELECT
    s.full_name,
    c.course_name,
    sub.status
FROM submissions sub
JOIN students s
ON sub.student_id = s.student_id
JOIN assignments a
ON sub.assignment_id = a.assignment_id

JOIN courses c
ON a.course_id = c.course_id
WHERE sub.status IN ('Late', 'Missing');


-- 6. Which instructor has the highest active enrollments?

SELECT
    i.full_name AS instructor_name,
    COUNT(e.enrollment_id) AS active_enrollments
FROM instructors i
JOIN courses c
ON i.instructor_id = c.instructor_id
JOIN enrollments e
ON c.course_id = e.course_id
WHERE e.status = 'active'
GROUP BY i.instructor_id
ORDER BY active_enrollments DESC
LIMIT 1;



-- 7. Final management overview report


SELECT
    s.full_name AS student_name,
    c.course_name,
    i.full_name AS instructor_name,
    e.status AS enrollment_status,

    COUNT(a.attendance_id) AS total_sessions,

    SUM(
        CASE 
            WHEN a.status = 'Present' THEN 1 
            ELSE 0 
        END
    ) AS attended_sessions,

    AVG(sub.score) AS average_score

FROM students s

JOIN enrollments e
ON s.student_id = e.student_id

JOIN courses c
ON e.course_id = c.course_id

JOIN instructors i
ON c.instructor_id = i.instructor_id

LEFT JOIN attendance a
ON e.enrollment_id = a.enrollment_id

LEFT JOIN assignments ass
ON c.course_id = ass.course_id

LEFT JOIN submissions sub
ON ass.assignment_id = sub.assignment_id
AND s.student_id = sub.student_id

GROUP BY 
    s.student_id,
    c.course_id,
    e.enrollment_id;
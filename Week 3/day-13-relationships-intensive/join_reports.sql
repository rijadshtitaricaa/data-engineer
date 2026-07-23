-- =====================================
-- Beginner: Show all students with city and email
-- =====================================
SELECT 
    s.full_name,
    s.city,
    s.email
FROM students s;


-- =====================================
-- Beginner: Show courses with instructor details
-- =====================================
SELECT
    c.course_name,
    c.level,
    i.full_name AS instructor_name,
    i.specialization
FROM courses c
INNER JOIN instructors i
ON c.instructor_id = i.instructor_id;


-- =====================================
-- Beginner: Show assignments with course name and due date
-- =====================================
SELECT
    a.title AS assignment_title,
    c.course_name,
    a.due_date
FROM assignments a
INNER JOIN courses c
ON a.course_id = c.course_id;


-- =====================================
-- Intermediate: Show enrollments with student and course information
-- =====================================
SELECT
    s.full_name AS student_name,
    c.course_name,
    e.enrollment_date,
    e.status
FROM enrollments e
INNER JOIN students s
ON e.student_id = s.student_id
INNER JOIN courses c
ON e.course_id = c.course_id;


-- =====================================
-- Intermediate: Show only active enrollments
-- =====================================
SELECT
    s.full_name,
    c.course_name,
    e.status
FROM enrollments e
INNER JOIN students s
ON e.student_id = s.student_id
INNER JOIN courses c
ON e.course_id = c.course_id
WHERE e.status = 'active';


-- =====================================
-- Intermediate: Show attendance records
-- =====================================
SELECT
    s.full_name AS student_name,
    c.course_name,
    a.session_date,
    a.status
FROM attendance a
INNER JOIN enrollments e
ON a.enrollment_id = e.enrollment_id
INNER JOIN students s
ON e.student_id = s.student_id
INNER JOIN courses c
ON e.course_id = c.course_id;


-- =====================================
-- Intermediate: Show submissions with student, assignment, course
-- =====================================
SELECT
    s.full_name AS student_name,
    a.title AS assignment_title,
    c.course_name,
    sub.score,
    sub.status
FROM submissions sub
INNER JOIN students s
ON sub.student_id = s.student_id
INNER JOIN assignments a
ON sub.assignment_id = a.assignment_id
INNER JOIN courses c
ON a.course_id = c.course_id;


-- =====================================
-- Advanced: Count students enrolled in each course
-- =====================================
SELECT
    c.course_name,
    COUNT(e.student_id) AS student_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id;


-- =====================================
-- Advanced: Show students enrolled in more than one course
-- =====================================
SELECT
    s.full_name,
    COUNT(e.course_id) AS total_courses
FROM students s
INNER JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id
HAVING COUNT(e.course_id) > 1;


-- =====================================
-- Advanced: Average score by course
-- =====================================
SELECT
    c.course_name,
    AVG(sub.score) AS average_score
FROM courses c
INNER JOIN assignments a
ON c.course_id = a.course_id
INNER JOIN submissions sub
ON a.assignment_id = sub.assignment_id
GROUP BY c.course_id;


-- =====================================
-- Advanced: Missing or late submissions
-- =====================================
SELECT
    s.full_name,
    c.course_name,
    a.title,
    sub.status
FROM submissions sub
INNER JOIN students s
ON sub.student_id = s.student_id
INNER JOIN assignments a
ON sub.assignment_id = a.assignment_id
INNER JOIN courses c
ON a.course_id = c.course_id
WHERE sub.status IN ('Late', 'Missing');


-- =====================================
-- Advanced: Students with no enrollments (LEFT JOIN)
-- =====================================
SELECT
    s.full_name,
    s.city,
    s.email
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;


-- =====================================
-- Advanced: Assignments with no submissions (LEFT JOIN)

SELECT
    a.title,
    c.course_name
FROM assignments a
LEFT JOIN submissions sub
ON a.assignment_id = sub.assignment_id
INNER JOIN courses c
ON a.course_id = c.course_id
WHERE sub.submission_id IS NULL;
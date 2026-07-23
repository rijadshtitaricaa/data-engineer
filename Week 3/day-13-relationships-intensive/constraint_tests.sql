PRAGMA foreign_keys = ON;


-- Invalid course instructor
-- Expected: Rejected because instructor_id 999 does not exist

INSERT INTO courses (course_name, level, instructor_id)
VALUES ('Machine Learning', 'Beginner', 999);



-- Invalid enrollment student
-- Expected: Rejected because student_id 999 does not exist

INSERT INTO enrollments (student_id, course_id, status)
VALUES (999, 1, 'active');



-- Invalid enrollment course

-- Expected: Rejected because course_id 999 does not exist

INSERT INTO enrollments (student_id, course_id, status)
VALUES (1, 999, 'active');



-- Duplicate enrollment
-- Expected: Rejected because UNIQUE(student_id, course_id)
-- prevents the same student joining the same course twice

INSERT INTO enrollments (student_id, course_id, status)
VALUES (1, 1, 'active');




-- Invalid attendance enrollment
-- Expected: Rejected because enrollment_id 999 does not exist

INSERT INTO attendance (enrollment_id, status)
VALUES (999, 'Present');



-- Invalid course level
-- Expected: Rejected because CHECK only allows
-- Beginner, Intermediate, Advanced

INSERT INTO courses (course_name, level, instructor_id)
VALUES ('AI Course', 'Expert', 1);



-- Invalid submission assignment
-- Expected: Rejected because assignment_id 999 does not exist

INSERT INTO submissions (assignment_id, student_id, score, status)
VALUES (999, 1, 90, 'Submitted');



-- Invalid submission score
-- Expected: Rejected because score cannot be above 100

INSERT INTO submissions (assignment_id, student_id, score, status)
VALUES (1, 1, 150, 'Submitted');



-- Negative submission score
-- Expected: Rejected because score cannot be negative

INSERT INTO submissions (assignment_id, student_id, score, status)
VALUES (1, 1, -10, 'Submitted');



-- Duplicate email
-- Expected: Rejected because email has UNIQUE constraint

INSERT INTO students (full_name, city, email)
VALUES ('Duplicate Student', 'Prishtina', 'john.smith@email.com');
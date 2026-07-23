
INSERT INTO students (full_name, city, email) VALUES
('John Smith', 'Prishtina', 'john.smith@email.com'),
('Emma Brown', 'Prizren', 'emma.brown@email.com'),
('Liam Wilson', 'Peja', 'liam.wilson@email.com'),
('Sophia Taylor', 'Gjakova', 'sophia.taylor@email.com'),
('Noah Davis', 'Ferizaj', 'noah.davis@email.com'),
('Olivia White', 'Mitrovica', 'olivia.white@email.com'),
('Lucas Johnson', 'Gjilan', 'lucas.johnson@email.com'),
('Mia Green', 'Skenderaj', 'mia.green@email.com');

SELECT * FROM students;


INSERT INTO instructors (full_name, specialization) VALUES
('Alice Johnson', 'SQL'),
('Bob Miller', 'Python'),
('Carol Davis', 'Data Engineering');

SELECT * FROM instructors;


INSERT INTO courses (course_name, level, instructor_id) VALUES
('SQL', 'Beginner', 1),
('Python', 'Beginner', 2),
('Databricks', 'Intermediate', 3),
('PySpark', 'Advanced', 3),
('Data Modeling', 'Intermediate', 1);

SELECT * FROM courses;


INSERT INTO enrollments (student_id, course_id, status) VALUES
(1,1,'active'),
(1,2,'active'),
(2,1,'completed'),
(2,5,'active'),
(3,2,'active'),
(3,3,'active'),
(4,4,'active'),
(4,5,'completed'),
(5,1,'active'),
(5,3,'active'),
(6,2,'dropped'),
(7,5,'active');

SELECT * FROM enrollments;


INSERT INTO attendance (enrollment_id, status) VALUES
(1,'Present'),
(1,'Late'),
(2,'Present'),
(2,'Present'),
(3,'Absent'),
(3,'Present'),
(4,'Present'),
(5,'Late'),
(6,'Present'),
(7,'Absent'),
(8,'Present'),
(9,'Present'),
(10,'Late'),
(11,'Absent'),
(12,'Present'),
(4,'Present'),
(6,'Late'),
(9,'Present');

SELECT * FROM attendance;


INSERT INTO assignments (course_id, title, due_date) VALUES
(1,'SQL Basics','2026-08-01'),
(1,'SQL Joins','2026-08-08'),
(2,'Python Functions','2026-08-05'),
(3,'Databricks Notebook','2026-08-10'),
(4,'PySpark Transformations','2026-08-15'),
(5,'ER Diagram','2026-08-20');

SELECT * FROM assignments;


INSERT INTO submissions
(assignment_id, student_id, score, status)
VALUES
(1,1,95,'Submitted'),
(2,1,90,'Submitted'),
(1,2,88,'Late'),
(6,2,92,'Submitted'),
(3,3,85,'Submitted'),
(4,3,80,'Late'),
(5,4,93,'Submitted'),
(6,4,97,'Submitted'),
(1,5,70,'Late'),
(4,5,NULL,'Missing'),
(3,6,NULL,'Missing'),
(6,7,89,'Submitted');

SELECT * FROM submissions;
Database Design

Students 

Represents people enrolled in the training program.

Primary key:
student_id

Relationships:
One student can have many enrollments.
One student can have many submissions.

Instructors

Represents teachers who delivers courses.

Primary key:
instructor_id

Relationships:
One instructor can teach many courses.

Courses 

Represents training courses offered by Unity Tech Hub.

Primary key:
course_id

Relationships:
One course belongs to one Instructor and can have many enrollments.

Enrollments

Connects student with courses. 

Primary key:
enrollment_id

Foreign key:
student_id - students
course_id - courses

Purpose:
Stores which students are enrolled in which courses

Attendance
Stores attendance records for enrolled students.

Primary Key:
attendance_id

Foreign Keys:
enrollment_id → enrollments

Purpose:
One enrollment can have many attendance records.



Assignments
Represents homework or projects for a course.

Primary Key:
assignment_id

Foreign Keys:
course_id → courses

Purpose:
One course can have many assignments.



Submissions
Stores assignment submissions from students.

Primary Key:
submission_id

Foreign Keys:
student_id → students
assignment_id → assignments

Purpose:
Records a student's submission, score, and status.



One-to-Many Relationships

One instructor → Many courses
One course → Many assignments
One student → Many enrollments
One enrollment → Many attendance records

Many-to-Many Relationship

Students and courses have a many-to-many relationship.
A student can enroll in many courses, and a course can have many students.

This is solved using the enrollments table, which acts as a bridge table.

Why course_name should not be stored in students

If course_name were stored in the students table, the same course name would be repeated for many students.
If the course name changed, every student record would need to be updated, increasing the risk of inconsistent data.

Relationship Diagram

instructors
      │
   courses
   │      │
       
enrollments   assignments
     │             │
                
attendance   submissions
      │
   students
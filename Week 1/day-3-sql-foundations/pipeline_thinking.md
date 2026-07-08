# Data Pipeline Thinking - Day 3

## Chosen business:
Unity Tech Hub Student Management System

## Source Data:
Student registration forms, course enrollments, attendance records, payment records, and student progress reports.

## Ingestion:
Student data is collected from registration forms and uploaded into the database. Attendance and payment information are regularly added from different systems.

## Storage:
The data is stored in SQL database tables such as Unity_Students, payments, courses, and attendance records.

## Cleaning:
Cleaning removes duplicate student records, fixes missing names or courses, corrects incorrect attendance values, and standardizes student statuses like Active and Inactive.

## Transformation:
The data can be transformed by calculating monthly revenue, average attendance, student performance, and active student counts.

## Business Output:
The final output can be a student dashboard showing active students, attendance reports, course statistics, and payment summaries.

## Business questions we can answer:
1. How many active students are currently enrolled?
2. Which courses have the highest number of students?
3. What is the average attendance rate for each course?

## Possible data problems:
1. Missing student information such as name or course.
2. Duplicate student records.
3. Incorrect attendance or payment values.
# Day 13 - Intensive Relationships and Foreign Keys

## Project Goal

The goal of this project was to design a normalized database for Unity Tech Hub. The database manages students, instructors, courses, enrollments, attendance, assignments, and submissions while maintaining accurate relationships between tables.

## Database Design

The database was designed by separating different real-world entities into individual tables instead of storing everything in one large table. This reduces duplicated data and improves data accuracy.

The main entities are:

- Students
- Instructors
- Courses
- Enrollments
- Attendance
- Assignments
- Submissions

## Tables and Relationships

The database contains the following relationships:

- One instructor can teach many courses.
- One course can have many enrollments.
- One student can have many enrollments.
- One enrollment can have many attendance records.
- One course can have many assignments.
- One student can have many submissions.
- One assignment can have many submissions.

The enrollments table acts as a bridge table between students and courses because they have a many-to-many relationship.

## Primary Keys, Foreign Keys, and Constraints

Primary keys were used to uniquely identify every row in each table.

Foreign keys were used to connect related tables and maintain valid relationships.

Constraints used:

- PRIMARY KEY: Ensures every row has a unique identifier.
- AUTOINCREMENT: Automatically creates new IDs.
- FOREIGN KEY: Protects relationships between tables.
- NOT NULL: Prevents missing required values.
- UNIQUE: Prevents duplicate values such as duplicate emails.
- CHECK: Restricts invalid values.

## Seed Data

Realistic sample data was inserted into the database:

- 8 students from different cities.
- 3 instructors with different specializations.
- 5 courses including SQL, Python, Databricks, PySpark, and Data Modeling.
- Multiple enrollments showing students taking different courses.
- Attendance records.
- Assignments and submissions.

The data was created so JOIN reports could provide meaningful results.

## Constraint Tests

Constraint tests were created to prove that the database protects data quality.

Tests included:

- Invalid foreign keys.
- Duplicate enrollments.
- Invalid course levels.
- Invalid submission scores.
- Duplicate emails.

Failed inserts were expected because the database rejected invalid data.

## JOIN Reports

JOIN reports were created to combine information from multiple tables.

Examples:

- Students with their courses.
- Courses with instructors.
- Assignments with course details.
- Submission reports.
- Students without enrollments using LEFT JOIN.

These reports demonstrate how relational databases support business analysis.

## Manager Report

A manager report was created to answer business questions, including:

- Courses with the highest enrollment.
- Students active in multiple courses.
- Instructor enrollment performance.
- Student submission issues.
- Overall student and course performance.

## Screenshots

Screenshots of the database tables, successful queries, and constraint test results are stored in the screenshots folder.

## What I Can Explain Live

I can explain:

- Why normalization is important.
- How primary keys identify records.
- How foreign keys connect tables.
- Why enrollments is a bridge table.
- How JOIN queries combine information.
- How constraints protect data quality.

## What I Would Improve Next

Possible improvements:

- Add more detailed attendance tracking.
- Add course schedules and class sessions.
- Add more reporting dashboards.
- Connect the database with analytics tools such as Databricks.
- Add more advanced validation rules.
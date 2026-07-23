# Answers

## What problem does a primary key solve?

A primary key gives every row a unique identity. It prevents duplicate records and allows other tables to reference a specific row.


## What problem does AUTOINCREMENT solve?

AUTOINCREMENT automatically creates a new unique ID for each new record. This avoids manually choosing IDs and reduces the chance of duplicates.


## What problem does a foreign key solve?

A foreign key creates a connection between tables and keeps relationships valid. It prevents inserting records that reference data that does not exist.


## Why is enrollments a bridge table?

Enrollments is a bridge table because students and courses have a many-to-many relationship. One student can join many courses, and one course can have many students, so enrollments connects them.


## Why is submissions also a relationship table?

Submissions connects students and assignments. A student can submit many assignments, and an assignment can have submissions from many students. It also stores relationship information like score and status.


## What is one-to-many in your project? Give two examples.

One-to-many means one record in a parent table can have many related records in another table.

Examples:
- One instructor can teach many courses.
- One course can have many assignments.


## What is many-to-many in your project? Give one example.

The many-to-many relationship is between students and courses. Many students can join many courses, and the enrollments table works as the bridge table.


## Why should we not store instructor_name directly inside every course report table?

Storing instructor_name repeatedly creates duplicate data. If the instructor changes their name, many records would need to be updated, which can cause inconsistent data.


## What is the difference between INNER JOIN and LEFT JOIN?

INNER JOIN only shows records that have matching data in both tables.

LEFT JOIN shows all records from the left table, even if there is no matching record in the right table.


## Which constraint test was most important and why?

The foreign key tests were important because they prevent invalid relationships, such as creating an enrollment for a student or course that does not exist.


## How does this prepare you for Databricks tables and reporting?

This prepares me for Databricks because good data modeling, relationships, keys, and clean tables are important for building reliable analytics and reports.
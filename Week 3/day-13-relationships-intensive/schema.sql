PRAGMA foreign_keys = ON;

create table students(
student_id INTEGER primary KEY AUTOINCREMENT,
full_name TEXT NOT NULL,
  city TEXT NOT NULL,
  email TEXT not NULL UNIQUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
  );
  
  create table instructors(
    instructor_id INTEGER PRIMARY key AUTOINCREMENT,
    full_name text not null,
    specialization text not null
    );
    
  	CREATE TABLE courses(
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    level TEXT NOT NULL CHECK(level IN ('Beginner', 'Intermediate', 'Advanced')),
    instructor_id INTEGER NOT NULL,

    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);
 CREATE TABLE enrollments(
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('active', 'completed', 'dropped')),

    UNIQUE(student_id, course_id),

    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
      
CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL,
    session_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK (status IN ('Present', 'Absent', 'Late')),

    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);
CREATE TABLE assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    due_date TIMESTAMP NOT NULL,

    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
CREATE TABLE submissions (
    submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    submitted_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    score INTEGER CHECK (score >= 0 AND score <= 100),
    status TEXT NOT NULL CHECK (status IN ('Submitted', 'Late', 'Missing')),

    FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
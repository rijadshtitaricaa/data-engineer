import pandas as pd

studentat = [
    {"student_id": 1,"name":"arta",  "city":"vushtrri", "course": "Python", "age": 17, "attendance": 90, "homework_score": 85},
    {"student_id": 2,  "name": "blend", "city": "prishtina", "course": "React", "age": 18, "attendance": 60, "homework_score": 70},
    {"student_id": 3, "name": "dion", "city": "vushtrri", "course": "Python", "age": 16, "attendance": 75, "homework_score": 95},
    {"student_id": 4,"name": "elira", "city": "mitrovica", "course": "React", "age": 17, "attendance": 80, "homework_score": 60},
    {"student_id": 5,  "name": "faton", "city": "vushtrri", "course": "Data Engineering", "age": 19, "attendance": 100, "homework_score": 90},
    {"student_id": 6,"name":  "gresa","city":  "prishtina",  "course":"Python",  "age": 18,"attendance": 55,  "homework_score": 88}
]


#  DETYRA 1 
# def print_basic_data(studentat):
#     print("Total Students", len(studentat))

#     print("\nStudent names ")
#     for student in studentat:
#         print(student["name"])

#     print("\nStudent details ")
#     for student in studentat[:2]:
#         print(f"{student['name']} is from {student['city']} and is learning {student['course']}")


# DETYRA 2 
# def filter_data(studentat):
#     print("\nStudents from Vushtrri:")
#     for student in studentat:
#         if student["city"] == "vushtrri":
#             print(student["name"])

#     print("\nStudents with low attendance:")
#     for student in studentat:
#         if student["attendance"] < 70:
#             print(student["name"])

#     print("\nStudents with homework score above 85:")
#     for student in studentat:
#         if student["homework_score"] > 85:
#             print(student["name"])


#  DETYRA 3 
# def calculations(studentat):
#     total_attendance = 0
#     for student in studentat:
#         total_attendance += student["attendance"]

#     avg_attendance = total_attendance / len(studentat)
#     print("Average attendance:", avg_attendance)

#     total_homework = 0
#     for student in studentat:
#         total_homework += student["homework_score"]

#     avg_homework = total_homework / len(studentat)
#     print("Average homework score", avg_homework)

#     city_count = {}
#     for student in studentat:
#         city = student["city"]
#         if city in city_count:
#             city_count[city] += 1
#         else:
#             city_count[city] = 1

#     print("\nStudents by city:")
#     for city, count in city_count.items():
#         print(city, count)

#     course_count = {}
#     for student in studentat:
#         course = student["course"]

#         if course in course_count:
#             course_count[course] += 1
#         else:
#             course_count[course] = 1

#     print("\nStudents per course:")
#     for course, count in course_count.items():
#         print(course, count)


#  DETYRA 4
# def performance_status(studentat):
#     print("Performance Stauts")

#     for student in studentat:
#         name = student["name"]
#         attendance = student["attendance"]
#         homework = student["homework_score"]

#         if attendance >= 80 and homework >= 80:
#             status = "Strong"
#         elif attendance >= 60 and homework >= 60:
#             status = "Average"
#         else:
#             status = "Needs Support"

#         print(name, status)


# # ---------------- DETYRA 5 ----------------
# def clean_report(studentat):
#     clean_studentat = []

#     for student in studentat:
#         attendance = student["attendance"]
#         homework = student["homework_score"]

#         if attendance >= 80 and homework >= 80:
#             status = "Strong"
#         elif attendance >= 60 and homework >= 60:
#             status = "Average"
#         else:
#             status = "Needs Support"

#         clean_record = {
#             "student_id": student["student_id"],
#             "name": student["name"],
#             "course": student["course"],
#             "performance_status": status
#         }

#         clean_studentat.append(clean_record)

#     print("Clean report records")
#     for student in clean_studentat:
#         print(f"{student['student_id']}   {student['name']}   {student['course']}   {student['performance_status']}")


# MAIN 
# print_basic_data(studentat)
# filter_data(studentat)
# calculations(studentat)
# performance_status(studentat)
# clean_report(studentat)
from monday_practice import studentat

clean_studentat = []

for student in studentat:
    attendance = student["attendance"]
    homework = student["homework_score"]

    if attendance >= 80 and homework >= 80:
        status = "Strong"
    elif attendance >= 60 and homework >= 60:
        status = "Average"
    else:
        status = "Needs Support"

    clean_studentat.append({
        "student_id": student["student_id"],
        "name": student["name"],
        "city": student["city"],
        "course": student["course"],
        "attendance": attendance,
        "homework_score": homework,
        "performance_status": status
    })

print("Student Report\n")

print(f"Total students: {len(clean_studentat)}")

avg_attendance = sum(student["attendance"] for student in clean_studentat) / len(clean_studentat)
avg_homework = sum(student["homework_score"] for student in clean_studentat) / len(clean_studentat)

print(f"\nAverage attendance: {round(avg_attendance, 2)}")
print(f"Average homework score: {round(avg_homework, 2)}")

print("\nStudents by city:")
city_count = {}
for student in clean_studentat:
    city = student["city"]
    city_count[city] = city_count.get(city, 0) + 1

for city, count in city_count.items():
    print(f"{city}: {count}")

print("\nStudents by course:")
course_count = {}
for student in clean_studentat:
    course = student["course"]
    course_count[course] = course_count.get(course, 0) + 1

for course, count in course_count.items():
    print(f"{course}: {count}")

print("\nStudents with low attendance:")
for student in clean_studentat:
    if student["attendance"] < 70:
        print(student["name"])

print("\nStrong students:")
for student in clean_studentat:
    if student["performance_status"] == "Strong":
        print(student["name"])

print("\nStudents that need support:")
for student in clean_studentat:
    if student["performance_status"] == "Needs Support":
        print(student["name"])
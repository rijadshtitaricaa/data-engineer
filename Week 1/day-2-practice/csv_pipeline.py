import csv

cleaned_students = []
students = []
missing = []
invalid = []
inconsistent = []
def load_students():
    with open("data/students_raw.csv", "r") as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if count == 0:
                count = count + 1
                continue

            line = line.strip()
            if line != "":
                row = line.split(",")
                students.append(row)


def print_stats():
    print("\nTotal raw records:", len(students))

    print("\nColumns:")
    print("student_id")
    print("name")
    print("age")
    print("city")
    print("course")
    print("attendance")
    print("homework_score")

    print("\nFirst 3 records:")
    record_counter = 0
    for student in students:
        if record_counter < 3:
            print(student[0], "-", student[1], "-", student[2], "-", student[3])
            record_counter = record_counter + 1


def check_data_quality():
    for student in students:
        if student[0].strip() == "":
            missing.append("student_id=" + student[0] + ", column=student_id")
        if student[1].strip() == "":
            missing.append("student_id=" + student[0] + ", column=name")
        
        if student[2].strip() == "":
            missing.append("student_id=" + student[0] + ", column=city")
        
        if student[3].strip() == "":
            missing.append("student_id=" + student[0] + ", column=course")
        
        if student[4].strip() == "":
            missing.append("student_id=" + student[0] + ", column=age")
        
        if student[5].strip() == "":
            missing.append("student_id=" + student[0] + ", column=attendance")
        
        if student[6].strip() == "":
            missing.append("student_id=" + student[0] + ", column=homework_score")

        if student[4].strip() != "":
            if not student[4].strip().isdigit():
                invalid.append("student_id=" + student[0] + ", column=age, value=" + student[4] )

        if student[5].strip() != "":
            if not student[5].strip().replace(".", "", 1).isdigit():
                invalid.append("student_id="+ student[0]+ ", column=attendance, value=" + student[5])
        
        if student[6].strip() != "":
            if not student[6].strip().replace(".", "", 1).isdigit():
                invalid.append("student_id=" + student[0] + ", column=homework_score, value=" + student[6])

        if student[2] == "VUSHTRRI" or student[2] == "prishtina":
            inconsistent.append("student_id=" + student[0] + ", column=city, value=" + student[2])

        if student[3] == "Data engineering":
            inconsistent.append("student_id=" + student[0] + ", column=course, value=" + student[3])

def clean_data():
    for student in students:
        raw_id = student[0].strip()
        raw_name = student[1].strip()
        raw_city = student[2].strip()
        raw_course = student[3].strip()
        raw_age = student[4].strip()
        raw_attendance = student[5].strip()
        raw_homework = student[6].strip()
        raw_date = student[7].strip()

        clean_id = int(raw_id)

        if raw_city == "":
            clean_city = "Unknown"
        elif raw_city == "VUSHTRRI":
            clean_city = "Vushtrri"
        elif raw_city == "prishtina":
            clean_city = "Prishtina"
        else:
            clean_city = raw_city

        if raw_course == "":
            clean_course = "Not Assigned"
        elif raw_course == "Data engineering":
            clean_course = "Data Engineering"
        else:
            clean_course = raw_course

        if raw_age == "":
            clean_age = 0
        elif not raw_age.isdigit():
            clean_age = 0
        else:
            clean_age = int(raw_age)

        if raw_attendance == "":
            clean_attendance = 0
        elif not raw_attendance.replace(".", "", 1).isdigit():
            clean_attendance = 0
        else:
            clean_attendance = float(raw_attendance)

        if raw_homework == "":
            clean_homework = 0
        elif not raw_homework.replace(".", "", 1).isdigit():
            clean_homework = 0
        else:
            clean_homework = float(raw_homework)

        if raw_date == "":
            clean_date = "Unknown Date"
        else:
            clean_date = raw_date

        total_score = clean_attendance + clean_homework

        if clean_attendance >= 80 and clean_homework >= 80:
            performance_status = "Strong"
        elif clean_attendance >= 60 and clean_homework >= 60:
            performance_status = "Average"
        else:
            performance_status = "Needs Support"

        if clean_attendance < 60 or clean_homework < 60:
            risk_flag = "At Risk"
        else:
            risk_flag = "OK"

        clean_row = [
            clean_id,
            raw_name,
            clean_city,
            clean_course,
            clean_age,
            clean_attendance,
            clean_homework,
            clean_date,
            total_score,
            performance_status,
            risk_flag
        ]
        
        cleaned_students.append(clean_row)
def make_report():
    total = len(missing) + len(invalid) + len(inconsistent)

    print("Data Quality Report")
    print("Total issues found: " + str(total))
    print("")
    print("Missing values:")
    for current_line in missing:
        print(current_line)
    print("")
    print("Invalid numeric values:")
    for current_line in invalid:
        print(current_line)
    print("")
    print("Inconsistent text values:")
    for current_line in inconsistent:
        print(current_line)

    with open("output/data_quality_report.txt", "w") as file:
        file.write("Data Quality Report\n")
        file.write("Total issues found: " + str(total) + "\n\n")

        file.write("Missing values:\n")
        for current_line in missing:
            file.write(current_line + "\n")

        file.write("\nInvalid numeric values\n")
        for current_line in invalid:
            file.write(current_line + "\n")

        file.write("\nInconsistent text values\n")
        for current_line in inconsistent:
            file.write(current_line + "\n")

def print_performance():
    print("\nPerformance Status")
    for current_line in cleaned_students:
        print(current_line[1] + ": " + current_line[9] + " - " + current_line[10])


def save_clean_csv():
    with open("output/students_clean.csv", "w") as file:
        file.write("student_id,name,city,course,age,attendance,homework_score,registered_date,total_score,performance_status,risk_flag\n")
        for current_line in cleaned_students:
            row_string = (str(current_line[0]) + "," +str(current_line[1]) + "," +str(current_line[2]) + "," +str(current_line[3]) + "," +str(current_line[4]) + ","
            +str(current_line[5]) + "," +str(current_line[6]) + "," +
                    str(current_line[7]) + "," +
            str(current_line[8]) + "," +
                str(current_line[9]) + "," +
                str(current_line[10]) + "\n"
            )
            file.write(row_string)

def make_summary_report():

    total_issues = len(missing) + len(invalid) + len(inconsistent)

    total_attendance = 0
    total_homework = 0

    cities = {}
    courses = {}

    strong_students = []
    support_students = []
    risk_students = []

    for student in cleaned_students:

        name = student[1]
        city = student[2]
        course = student[3]
        attendance = student[5]
        homework = student[6]
        total_score = student[8]
        performance = student[9]
        risk = student[10]

        total_attendance += attendance
        total_homework += homework

        if city in cities:
            cities[city] += 1
        else:
            cities[city] = 1

        if course in courses:
            courses[course] += 1
        else:
            courses[course] = 1

        if performance == "Strong":
            strong_students.append(name)

        if performance == "Needs Support":
            support_students.append(name)

        if risk == "At Risk":
            risk_students.append(name)


    average_attendance = total_attendance / len(cleaned_students)
    average_homework = total_homework / len(cleaned_students)


    top_students = sorted(
        cleaned_students,
        key=lambda x: x[8],
        reverse=True
    )[:3]


    report = ""

    report += "Final Student Data Report\n"
    report += "========================\n"
    report += "Total raw records: " + str(len(students)) + "\n"
    report += "Total cleaned records: " + str(len(cleaned_students)) + "\n"
    report += "Total data quality issues found: " + str(total_issues) + "\n\n"

    report += "Average attendance: " + str(round(average_attendance, 2)) + "\n"
    report += "Average homework score: " + str(round(average_homework, 2)) + "\n\n"


    report += "Students by city:\n"
    for city, count in cities.items():
        report += city + ": " + str(count) + "\n"


    report += "\nStudents by course:\n"
    for course, count in courses.items():
        report += course + ": " + str(count) + "\n"


    report += "\nStrong students:\n"
    for student in strong_students:
        report += student + "\n"


    report += "\nStudents that need support:\n"
    for student in support_students:
        report += student + "\n"


    report += "\nAt Risk students:\n"
    for student in risk_students:
        report += student + "\n"


    report += "\nTop 3 students by total score"
    for student in top_students:
        report += student[1] + ": " + str(student[8]) + "\n"


    print(report)


    with open("output/summary_report.txt", "w") as file:
        file.write(report)

def main():
    print("\nCSV Inspection")
    load_students()
    print_stats()
    print("\n")
    check_data_quality()
    make_report()
    clean_data()
    print_performance()
    save_clean_csv()
    make_summary_report()


if __name__ == "__main__":
    main()  
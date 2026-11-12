import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


students = load_students()


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    print("\n--- ADD NEW STUDENT ---")

    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "reg_no": reg_no,
        "course": course
    }

    for existing in students:
        if existing["reg_no"] == reg_no:
            print("Registration number already exists!")
            return

    students.append(student)
    save_students()

    print("Student added successfully!")


def view_students():
    print("\n--- ALL STUDENTS ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-------------------------")
        print("Name:", student["name"])
        print("Registration Number:", student["reg_no"])
        print("Course:", student["course"])


def search_student():
    print("\n--- SEARCH STUDENT ---")

    reg_no = input("Enter registration number: ")

    for student in students:
        if student["reg_no"] == reg_no:
            print("Student found!")
            print("Name:", student["name"])
            print("Registration Number:", student["reg_no"])
            print("Course:", student["course"])
            return

    print("Student not found.")


def delete_student():
    print("\n--- DELETE STUDENT ---")

    reg_no = input("Enter registration number: ")

    for student in students:
        if student["reg_no"] == reg_no:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
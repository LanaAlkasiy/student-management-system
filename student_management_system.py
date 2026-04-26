def addStudent():
    try:
        file = open("students.txt", "a")

        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        grade = float(input("Enter student grade: "))

        file.write(str(student_id) + "\n")
        file.write(name + "\n")
        file.write(str(grade) + "\n")

        file.close()
        print("Student added successfully.\n")

    except ValueError:
        print("Invalid input. ID must be integer and grade must be numeric.\n")
    except IOError:
        print("Error: could not write to file.\n")


def displayStudents():
    try:
        file = open("students.txt", "r")

        print("\nID\tName\tGrade")
        print("------------------------")

        while True:
            student_id = file.readline().strip()
            if student_id == "":
                break

            name = file.readline().strip()
            grade = file.readline().strip()

            print(student_id, "\t", name, "\t", grade)

        file.close()
        print()

    except IOError:
        print("Error: could not open or read the file.\n")


def displayAvg():
    try:
        file = open("students.txt", "r")

        total = 0
        count = 0

        while True:
            student_id = file.readline().strip()
            if student_id == "":
                break

            name = file.readline().strip()
            grade = float(file.readline().strip())

            total += grade
            count += 1

        file.close()

        if count > 0:
            avg = total / count
            print("Average grade =", avg, "\n")
        else:
            print("No students in file.\n")

    except IOError:
        print("Error: could not open or read the file.\n")
    except ValueError:
        print("Error: invalid data found in file.\n")


def displayTop():
    try:
        file = open("students.txt", "r")

        top_name = ""
        top_grade = -1

        while True:
            student_id = file.readline().strip()
            if student_id == "":
                break

            name = file.readline().strip()
            grade = float(file.readline().strip())

            if grade > top_grade:
                top_grade = grade
                top_name = name

        file.close()

        if top_grade != -1:
            print("Top student:", top_name)
            print("Grade:", top_grade, "\n")
        else:
            print("No students in file.\n")

    except IOError:
        print("Error: could not open or read the file.\n")
    except ValueError:
        print("Error: invalid data found in file.\n")


def search():
    try:
        wanted_id = int(input("Enter student ID to search for: "))
        file = open("students.txt", "r")

        found = False

        while True:
            student_id = file.readline().strip()
            if student_id == "":
                break

            name = file.readline().strip()
            grade = file.readline().strip()

            if int(student_id) == wanted_id:
                print("Student found:")
                print("Name:", name)
                print("Grade:", grade, "\n")
                found = True
                break

        file.close()

        if not found:
            print("No student with that ID.\n")

    except ValueError:
        print("Invalid input. Student ID must be an integer.\n")
    except IOError:
        print("Error: could not open or read the file.\n")


def countFailed():
    try:
        file = open("students.txt", "r")

        count = 0

        while True:
            student_id = file.readline().strip()
            if student_id == "":
                break

            name = file.readline().strip()
            grade = float(file.readline().strip())

            if grade < 60:
                count += 1

        file.close()
        print("Number of failed students =", count, "\n")

    except IOError:
        print("Error: could not open or read the file.\n")
    except ValueError:
        print("Error: invalid data found in file.\n")


def main():
    choice = 0

    while choice != 7:
        try:
            print("********************************")
            print("Welcome to Student Records!")
            print("********************************")
            print("Please select one of the following:")
            print("1: Add a new student")
            print("2: Display all students")
            print("3: Display the average grade")
            print("4: Display the name and grade of the top student")
            print("5: Search for a student by ID")
            print("6: Display number of failed students")
            print("7: Exit")

            choice = int(input("Your selection: "))

            if choice == 1:
                addStudent()
            elif choice == 2:
                displayStudents()
            elif choice == 3:
                displayAvg()
            elif choice == 4:
                displayTop()
            elif choice == 5:
                search()
            elif choice == 6:
                countFailed()
            elif choice == 7:
                print("Goodbye!")
            else:
                print("Invalid choice, try again.\n")

        except ValueError:
            print("Invalid input. Please enter a numeric menu option.\n")


main()
# Student Information System (SIS) using dictionaries, lists, and file handling
# students_data: {student_id: (name, major)}
# courses_data: {course_code: (course_name, credits)}
# grades_data: list of dictionaries, each containing a student's grade record
#we're storing the data here:
students_data = {}
courses_data = {} #dictionary
grades_data = [] #list

#open the cvs files/ read line by line/ split the values/ store them in the correct structure
def load_data():
    try:
        students = open("Students.csv","r")
        for line in students:
            split_line = line.rsplit(",")
            students_data[split_line[0]]=(split_line[1],split_line[2].rstrip()) #adds the data that is read form the file and splited
        students.close() 
           
        grades = open("grades.csv","r")
        for line in grades:
            split_line = line.rsplit(",")
            grades_data.append({
                "student_id": split_line[0],
                "course_code": split_line[1],
                "semester": split_line[2],
                "grade": split_line[3].rstrip()
                })
        grades.close()   
        courses = open("courses.csv","r")
        for line in courses:
            split_line = line.rsplit(",")
            courses_data[split_line[0]] = (split_line[1], int(split_line[2].rstrip()))
        courses.close()    
    except FileNotFoundError:
            print("One or more data files not found. ")

def add_new_student(): #option 1
    print("--- Add New Student ---")

    student_id = input("Enter Student ID: ")

    if student_id in students_data:
        print(f"Error: Student ID {student_id} already exists.")
        return

    name = input("Enter student name: ")
    major = input("Enter student major: ")

    students_data[student_id] = (name, major)

    print("Student added successfully.")
    
def record_student_grade(): #option 2
    print('--- Record Student Grade ---')
    student_id = input("Enter student ID: ")
    if student_id not in students_data:
        print(f"Error: Student ID '{student_id}' not found.")
        return
    
    course_code = input("Enter course code: ")
    if course_code not in courses_data:
        print(f"Error: course code '{course_code}' not found.")
        return
    
    semester = input("Enter semester (e.g., Fall2025): ")
        
    grade = input("Enter grade (A, B, C, D, or F): ")
    possible_grades = ['A', 'B', 'C', 'D', 'F']
    if grade not in possible_grades:
        print("Error: Invalid grade. Must be A, B, C, D, or F.")
        return
    
    for record in grades_data:
        if record['student_id'] == student_id and record['course_code'] == course_code and record['semester'] == semester:
            print(f"Error: Student {student_id} already has a grade for {course_code} in {semester}.")
            return
    
    grades_data.append({'student_id': student_id, 'course_code': course_code, 'semester': semester, 'grade': grade})
    print('Grade recorded successfully.')
    
def delete_student_record(): #option 3
    print("--- Delete Student ---")

    student_id = input("Enter Student ID: ")

    if student_id not in students_data:
        print("Student not found")
        return
    
    name, major = students_data[student_id]
    print(f"Student found: {name}, {major}")

    confirm = input("Are you sure you want to delete this student and all their grades? (yes/no): ") # confirmation

    if confirm.lower() == "yes":

        del students_data[student_id] # delete from dictionary
        
        for g in grades_data[:]: # delete all grades related to this student
            if g['student_id'] == student_id:
                grades_data.remove(g)

        print(f"Student {student_id} and all associated grades deleted.")
                
def display_student_transcript(): #option 4
    print('--- Display Student Transcript ---')
    student_id = input('Enter Student ID to display transcript: ')
    print('---------------------------------------')
    
    if student_id not in students_data:
        print("Student not found.")
        return
    student_name = students_data[student_id][0]
    major = students_data[student_id][1]

    print('Student Transcript')
    print(f'Name: {student_name}')
    print(f'Major: {major}')
    print("---------------------------------------")
    print('Course Code\tCourse Name\t\tSemester\tCredits\tGrade')
    print('-----------------------------------------------------------------------')

    found = False
    for record in grades_data: #record is a dictionary
        if record['student_id']==student_id:
            found = True
            course_code = record['course_code']
            course_name = courses_data[course_code][0]
            credits = courses_data[course_code][1]
            semester = record['semester']
            grade = record['grade']
            print(f'{course_code}\t{course_name}\t\t{semester}\t{credits}\t{grade}')
    if found == False:
            print("No grades found for this student.")

    
def calculate_student_gpa(): #option 5
    print('--- Calculate Student GPA ---')
    student_id = input('Enter student ID to calculate GPA: ')
    print('---------------------------------------')
    if student_id not in students_data:
        print(f"Error: Student ID '{student_id}' not found.")
        return
    
    grade_values = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    total_points = 0.0
    total_credits = 0

    for record in grades_data:
        if record['student_id']==student_id:
            course_code = record['course_code']
            grade = record['grade']
            credits = courses_data[course_code][1]
            total_points += grade_values[grade]*credits
            total_credits += credits

    if total_credits==0:
        print('No grades found. Cannot calculate GPA.')
        return
    
    gpa = total_points/total_credits
    student_name = students_data[student_id][0]
    major = students_data[student_id][1]

    print('GPA Calculation')
    print(f'Student: {student_name}')
    print(f'GPA: {gpa:.2f}')
    print('---------------------------------------')

def display_course_enrollment(): #option 6
    print('--- Display Course Enrollment ---')
    course_code = input("Enter Course Code: ")
    if course_code not in courses_data:
        print("Course not found.")
        return
    print(f'--- Students Enrolled in {course_code}: {courses_data[course_code][0]} ---')
    student_number = 0
    for data in grades_data: #data is each dictionary in the list
        if course_code == data['course_code']:
            student_number += 1
            student_id = data['student_id']
            student_name = students_data[student_id][0]
            print(f'{student_number}. {student_name}')       
    
    if student_number == 0: 
        print("No students found for this course.")
        

def search_students_by_major(): #option 7
    print('--- Search Students by Major ---')
    major = input('Enter the major to search for: ')
    print(f"--- Students in '{major.title()}' ---")
    print('Student ID\tStudent Name')
    print('----------------------------------------')

    found = False
    for student_id in students_data: #only loops over keys
        info = students_data[student_id]
        student_name = info[0]
        student_major = info[1]

        if student_major.lower()==major.lower():
            found = True
            print(f'{student_id}\t{student_name}')
    if found == False:
        print("No students found in that major.")

    print('----------------------------------------')
    
def search_courses_by_credits(): #option 8
    print('--- Search Courses by Credit Hours ---')
    credits = int(input('Enter the number of credit hours to search for: '))
    print(f'--- Courses with {credits} Credit(s) ---')
    print('Course Code \t Course Name')
    print('---------------------------------------------')
    found = False
    for code, (name, course_credits) in courses_data.items():
        if course_credits == credits:
            found = True
            print(f'{code}\t{name}')
    
    if found == False:
        print("No courses found with that number of credits.")
    
    print('---------------------------------------------')

def search_grades_by_semester(): #option 9
    print('--- Search Grades by Semester ---')
    semester = input('Enter the semester to search for (e.g., Fall2025): ')
    print(f'--- Grade Report for Semester: {semester} ---')
    print('Student ID\tName\tCourse Code\tCourse Name\tGrade')
    print('-----------------------------------------------------------------------------')

    found = False
    for record in grades_data:
        if record['semester'] == semester:
            found = True
            student_id = record['student_id']
            student_name = students_data[student_id][0]
            course_code = record['course_code']
            course_name = courses_data[course_code][0]
            grade = record['grade']
            print(f'{student_id}\t{student_name}\t{course_code}\t{course_name}\t{grade}')
    if found == False:
        print("No grades found for this semester.")
    
    print('-----------------------------------------------------------------------------')
    
def exit_program(): #option 10
    students = open("Students.csv","w") #writing the students data back to the csv in csv format
    for student_id in students_data:
        name , major = students_data[student_id]
        line = student_id + "," + name + "," + major
        students.write(line + "\n") #bc students data is a dictionary, and write only accepets strings, cant add it as a sting 
    students.close() 
    
    courses=open("courses.csv","w")   
    for course_code in courses_data:
        course_name , course_credit = courses_data[course_code] #this is called unpacking
        line = course_code + "," + course_name + "," + str(course_credit)
        courses.write(line + "\n")
    courses.close() 
    
    grades=open("grades.csv","w")    
    for record in grades_data:
        student_id = record["student_id"]
        course_code = record["course_code"]
        semester = record["semester"]
        grade = record["grade"]
        line = student_id + "," + course_code + "," + semester + "," + grade
        grades.write(line + "\n")
    grades.close()  
                             
def main(): #this dispplays the menu,  takes input, and calls functions based on user's input
    load_data()
    while True:        #to keep the program running until user exit
        print("1. Add Student")
        print("2. Record Grades")
        print("3. Delete Student")
        print("4. Display Transcript")
        print("5. Calculate GPA")
        print("6. Course Enrollment")
        print("7. Search by Major")
        print("8. Search by Credits")
        print("9. Search by Semester")
        print("10. Exit")
        try:  
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. please enter a number from 1-10 ")
            continue 
        if choice == 1:
            add_new_student()
        elif choice == 2:
            record_student_grade()
        elif choice == 3:
            delete_student_record()
        elif choice == 4:
            display_student_transcript()
        elif choice == 5:
            calculate_student_gpa()
        elif choice == 6:
            display_course_enrollment()
        elif choice == 7:
            search_students_by_major()
        elif choice == 8:
            search_courses_by_credits()
        elif choice == 9:
            search_grades_by_semester()
        elif choice == 10:
            exit_program()
            break
        else:
            print("Invalid Choice، Please try again. ")
            
main()          


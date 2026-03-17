from database import get_connection
class Faculty:
    def __init__(self):
        self.db = get_connection()
        self.cursor = self.db.cursor()
    
    def login(self):
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        query = "SELECT * FROM faculty WHERE email=%s AND password =%s"
        self.cursor.execute(query, (email, password))
        result = self.cursor.fetchone()
        if result:
            print("Login successful")
            self.menu(email)
        else:
            print("Invalid credentials")
    def menu(self, email):
        while True:
            print("\nFaculty Menu")
            print("1. View Profile")
            print("2. View subjects assigned")
            print("3. View students assigned")
            print("4. Change password")
            print("5. Add/Update student marks")
            print("6. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_profile(email)
            elif choice == "2":
                self.subjects_assigned(email)
            elif choice == "3":
                self.students_assigned(email)
            elif choice == "4":
                self.change_password(email)
            elif choice == "5":
                self.add_marks(email)
            elif choice == "6":
                break
            else:
                print("Invalid option")
    def view_profile(self, email):
        query = "SELECT id, name, email, dob, course FROM faculty where email=%s"
        self.cursor.execute(query, (email,))
        faculty = self.cursor.fetchone()
        if faculty:
            print(f"Name: {faculty[1]}, Email: {faculty[2]}, Course: {faculty[4]}")
        else:
            print("No profile found")
    def subjects_assigned(self, email):
        query = "SELECT speciality FROM faculty where email=%s"
        self.cursor.execute(query, (email,))
        faculty = self.cursor.fetchone()
        if faculty:
            print(f"The subjects assigned are: {faculty[0]}")
        else:
            print("No subjects assigned")
    def students_assigned(self, email):
        query = "SELECT students.id, students.name AS stud_name, students.email, students.course, faculty.name AS faculty_name FROM students JOIN faculty on students.course = faculty.course WHERE faculty.email=%s"
        self.cursor.execute(query, (email,))
        students = self.cursor.fetchall()

        if not students:
            print("Not assigned")
        else:
            for student in students:
                print(student)

    def change_password(self, email):
        password_old = input("Enter the old password: ")
        query = "SELECT * FROM faculty where email =  %s and password = %s"
        self.cursor.execute(query, (email, password_old))
        result = self.cursor.fetchone()
        if result:
            new_password = input("Enter a new password: ")
            confirm_password = input(("Enter the password again: "))
            if new_password == confirm_password:
                new_query = "UPDATE faculty SET password = %s WHERE email = %s"
                self.cursor.execute(new_query, (new_password, email))
                self.db.commit()
                print("Password changed successfully")
            else:
                print("Passwords are not matching")
        else:
            print("Previous password is not correct")
    
    def add_marks(self, email):
        student_email = input("Enter student's email: ")
        subject = input("Enter subject: ")
        try:
            marks = int(input("Enter marks: "))
        except ValueError:
            print("Invalid marks! Enter a number.")
            return
        query = """SELECT students.email 
               FROM students 
               JOIN faculty ON students.course = faculty.course 
               WHERE faculty.email=%s AND students.email=%s"""
        self.cursor.execute(query, (email, student_email))
        result = self.cursor.fetchone()
        if not result:
            print("You cannot add marks for this student")
            return
        query = "SELECT * FROM marks WHERE student_email=%s AND subject=%s"
        self.cursor.execute(query, (student_email, subject))
        existing = self.cursor.fetchone()
        if existing:
            update_query = "UPDATE marks SET marks=%s WHERE student_email=%s AND subject=%s"
            self.cursor.execute(update_query, (marks, student_email, subject))
        else:
            insert_query = "INSERT INTO marks (student_email, subject, marks) VALUES (%s, %s, %s)"
            self.cursor.execute(insert_query, (student_email, subject, marks))
        self.db.commit()
        print("Marks updated successfully")
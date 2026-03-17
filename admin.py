from database import get_connection
class Admin:
    def __init__(self):
        self.db = get_connection()
        self.cursor = self.db.cursor()
    def login(self):
        email = input("Enter Admin email: ")
        password = input("Enter password: ")

        query = "SELECT * from admin where email=%s and password=%s"
        self.cursor.execute(query, (email, password))
        result = self.cursor.fetchone()

        if result:
            print("login successful")
            self.menu()
        else:
            print("Invalid credentials")

    def menu(self):
        while True:
            print("\nADMIN MENU")
            print("1. Add Students")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Add Faculty")
            print("5. View Faculty")
            print("6. Delete Faculty")
            print("7. Logout")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.add_faculty()
            elif choice == "5":
                self.view_faculty()
            elif choice == "6":
                self.delete_faculty()
            elif choice == "7":
                break
            else:
                print("Invalid choice!")
    def add_student(self):
        name = input("Name: ")
        email = input("Email: ")
        password = input("Password: ")
        dob = input("DOB(YYYY-MM-DD): ")
        
        valid_courses = ["CSE", "AIML", "DS", "IT", "CYS", "ECE", "EEE", "CCE", "MECH", "CIV", "BIO"]
        while True:
            course = input("You can choose from the options(CSE, AIML, DS, IT, CYS, ECE, EEE, CCE, MECH, CIV, BIO): ").upper()
            if course in valid_courses:
                break
            else:
                print("Invalid, choose again!")

        query = "INSERT INTO students (name, email, password, dob, course) VALUES(%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (name, email, password, dob, course))
        self.db.commit()

        print("Student added")

    def view_students(self):
        query = "SELECT name, email, dob, fees_paid, course FROM students"
        self.cursor.execute(query)
        students = self.cursor.fetchall()

        if not students:
            print("No students")
        else:
            for student in students:
                print(student)
    
    def delete_student(self):
        email = input("Enter student's email to delete: ")
        query = "DELETE FROM students WHERE email = %s"
        self.cursor.execute(query, (email,))
        self.db.commit()
        print("Student deleted")
    
    def add_faculty(self):
        name = input("Enter faculty member's name: ")
        email = input("Enter faculty member's email: ")
        password = input("Enter password: ")
        dob = input("(YYYY-MM-DD): ")
        speciality = input("Enter the subjects taught by instructor(separate by comma): ")
        valid_courses = ["CSE", "AIML", "DS", "IT", "CYS", "ECE", "EEE", "CCE", "MECH", "CIV", "BIO"]
        while True:
            course = input("You can choose from the options(CSE, AIML, DS, IT, CYS, ECE, EEE, CCE, MECH, CIV, BIO): ").upper()
            if course in valid_courses:
                break
            else:
                print("Invalid, choose again!")


        query = "INSERT INTO faculty (name, email, password, dob, speciality, course) VALUES(%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (name, email, password, dob, speciality, course))
        self.db.commit()
        print("Faculty added")

    def view_faculty(self):
        query = "SELECT name, email, dob, speciality, course FROM faculty"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if not records:
            print("No Faculty")
        else:
            for record in records:
                print(record)
                
    def delete_faculty(self):
        email = input("Enter email to delete: ")
        query = "DELETE FROM faculty WHERE email=%s"
        self.cursor.execute(query, (email,))
        self.db.commit()
        print("Faculty deleted")
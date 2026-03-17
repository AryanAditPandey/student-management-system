from database import get_connection
class Student:
    def __init__(self):
        self.db = get_connection()
        self.cursor = self.db.cursor()
    
    def login(self):
        print("Your email is your First name in capital following an '.' and your date of birth(DD) after that + '@' + college_name.com ")
        email = input("Enter your email address: ")
        print("Your first time login password is your firstname+coursename+DD")
        password = input("Enter your password: ")

        query = "SELECT * FROM students WHERE email=%s and password=%s"
        self.cursor.execute(query, (email, password))
        result = self.cursor.fetchone()
        if result:
            print("login successful")
            self.menu(email)
        else:
            print("Invalid credentials")
    
    def menu(self, email):
        while True:
            print("\nStudent Menu")
            print("1. View Profile")
            print("2. Pay fees")
            print("3. View Marks")
            print("4. Change password")
            print("5. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_profile(email)
            elif choice == "2":
                self.pay_fees(email)
            elif choice == "3":
                self.view_marks(email)
            elif choice == "4":
                self.change_password(email)
            elif choice == "5":
                break
            else:
                print("Invalid choice")
    
    def view_profile(self, email):
        query = "SELECT id, name, email, dob, fees_paid, course FROM students where email=%s"
        self.cursor.execute(query, (email,))
        student = self.cursor.fetchone()
        print(student)
        
    def pay_fees(self, email):
        query = "SELECT fees_paid FROM students WHERE email=%s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        if result and result[0]:
            print("Fees already paid")
        else:
            update_query = "UPDATE students set fees_paid = TRUE where email = %s"
            self.cursor.execute(update_query, (email,))
            self.db.commit()
            print("Fees paid successfully")

    def view_marks(self, email):
        query = "SELECT subject, marks FROM marks where student_email = %s"
        self.cursor.execute(query, (email,))
        results = self.cursor.fetchall()
        if not results:
            print("No marks yet")
        else:
            for subject, marks in results:
                print(f"{subject}: {marks}")

    def change_password(self, email):
        password_old = input("Enter the old password: ")
        query = "SELECT * FROM students where email =  %s and password = %s"
        self.cursor.execute(query, (email, password_old))
        result = self.cursor.fetchone()
        if result:
            new_password = input("Enter a new password: ")
            confirm_password = input(("Enter the password again: "))
            if new_password == confirm_password:
                new_query = "UPDATE students SET password = %s WHERE email = %s"
                self.cursor.execute(new_query, (new_password, email))
                self.db.commit()
                print("Password changed successfully")
            else:
                print("Passwords are not matching")
        else:
            print("Previous password is not correct")






        




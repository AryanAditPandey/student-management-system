from admin import Admin
from student import Student
from faculty import Faculty

def main():
    while True:
        print(" USER-MENU ")
        print("1. Admin")
        print("2. Student")
        print("3. Faculty")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            admin = Admin()
            admin.login()
        elif choice == "2":
            student = Student()
            student.login()
        elif choice == "3":
            faculty = Faculty()
            faculty.login()
        elif choice == "4":
            print("Closing the application")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
#Exercise N1
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    def __str__(self):
        return (f'account number: {self.account_number}, '
                f'account holder: {self.account_holder}, '
                f'balance: ${self.balance}')


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'deposited: ${amount}. new balance: ${self.balance}')
        else:
            print("amount must be positive number")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -=amount
                print(f'withdrew ${amount}. ur new balance is ${self.balance}')
            else:
                print('not enough money in ur bank account')
        else:
            print('amount must be positive number')       


bankacc = BankAccount(1,'jane smith')

bankacc2 = BankAccount(2, 'john doe')

bankacc.deposit(1000)
bankacc.withdraw(500)

bankacc2.deposit(1500)
bankacc2.withdraw(2000)

print(bankacc)
print(bankacc2)



#Exercise N2

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.enrolled_students = []

    def show_students(self):
        if not self.enrolled_students:
            print(f"no students enrolled in '{self.name}'")
            return
        names = ', '.join([student for student in self.enrolled_students])
        if len(self.enrolled_students) == 1:
            print(f"{names} is registered in {self.name}.")
        else:
            print(f"{names} are registered in {self.name}.")

class Student:
    def __init__(self, name, student_id):
        self.student_id = student_id
        self.name= name
        self.courses = []

    def show_info(self):
        courses_list = ', '.join(self.courses) if self.courses else "None"
        print(f"Student Name: {self.name}, Student ID: {self.student_id}, Student's Courses: {courses_list}")

    def register(self, course):
        if course.max_students > len(course.enrolled_students):
            course.enrolled_students.append(self.name)
            self.courses.append(course.name)
            print(f"Student {self.name} registered for course '{course.name}'")
        else:
            print(f"Unfortunately for {self.name}, the course '{course.name}' is full")

student = Student('jane', 1)
student2 = Student('john', 2)

student.show_info()
student2.show_info()

py_course = Course('intro to python', 2)
js_course = Course('intro to javascript', 1)

student.register(py_course)
student2.register(py_course)

student.register(js_course)
student2.register(js_course)

py_course.show_students()
js_course.show_students()
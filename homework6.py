#Exercise N1

user_input = input('enter some text: ')
frequency_dict = {}
splited_user_input = user_input.split()
for i in splited_user_input:
    counter = splited_user_input.count(i)
    frequency_dict[i] = counter
print(frequency_dict)


# #Exercise N2

operations = {
    '+': "addition",
    '-': "subtraction",
    '*': "multiplication",
    '/': "division",
    '%': "modulus",
    '**': "exponentiation"
}

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
operator = input("enter a mathematical operator (+, -, *, /, %, **): ")

match operator:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "cannot divide by zero"
    case '%':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "cannot modulus by zero"
    case '**':
        result = num1 ** num2
    case _:
        result = "invalid operator"

if result == "Invalid operator" or result == "cannot divide by zero" or result == "cannot modulus by zero":
    print(result)
else:
    print(f"Result: {num1} {operator} {num2} = {result}")


# #Exercise N3

squares = {x: x**2 for x in range(11)}
print(squares)

#Exercise N4

departments = {
    "HR": [
        {"first_name": "John", "last_name": "Doe", "age": 30, "salary": 70000},
        {"first_name": "Jane", "last_name": "Smith", "age": 28, "salary": 50000}
    ],
    "IT": [
        {"first_name": "Alice", "last_name": "Johnson", "age": 35, "salary": 100000},
        {"first_name": "Bob", "last_name": "Brown", "age": 40, "salary": 120000}
    ],
    "Finance": [
        {"first_name": "Charlie", "last_name": "Davis", "age": 45, "salary": 105000},
        {"first_name": "Diana", "last_name": "Miller", "age": 50, "salary": 115000}
    ]
}
total_salary = 0

for department, employees in departments.items():
    department_salary = 0
    
    for employee in employees:
        department_salary += employee['salary']
    
    avg_salary = department_salary / len(employees) 
    total_salary += department_salary
    
    print(f'average salary in {department} is salary ${avg_salary}')

print(f"\ntotal salary is ${total_salary}")

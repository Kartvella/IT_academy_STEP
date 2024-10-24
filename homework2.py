# # დავალება N1
print("დავალება N1\n")

number = 0

if number % 2 == 1:
    print(f"Number {number} is odd")
else:
    print(f"Number {number} is even")


# დავალება N2
print("დავალება N2\n")

user_input = input("enter a word: ")
if 'small' in user_input:
    print("'small' was in ur input")
elif 'tall' in user_input:
    print("'tall' was in ur input")
elif 'middle' in user_input:
    print("'middle' was in ur input")
else:
    print("neither 'small', 'tall', or 'middle' were in ur input")


#დავალება N3
print("დავალება N3\n")

try:
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))
except ValueError:
    print('number u entered is invalid')
    quit()
operator = input("enter an operator (+, -, *, /, //, %, **): ")

result = None

match operator:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("can not divide by 0")
        else:
            result = num1 / num2
    case '//':
        if num2 == 0:
            print("can not divide by 0")
        else:
            result = num1 // num2
    case '%':
        if num2 == 0:
            print("can not perform modulus by 0")
        else:
            result = num1 % num2
    case '**':
        result = num1 ** num2
    case _:
        print("operator u entered is not valid")

if result is not None:
    print(f"Result: {result}")
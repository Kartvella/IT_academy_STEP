# დავალება N1
print(0.1+0.2)

print("დავალება N1\n")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

sum_of_nums = num1 + num2 + num3

print(f"Sum of those numbers are: {sum_of_nums}\n\n")


# დავალება N2

print("დავალება N2\n")

length = int(input("Enter length of a cube: "))

volume = length ** 3

area = 6 * length ** 2


print(f"area of a cube is: {area}\nand volume is: {volume}\n\n")


#დავალება N3

print("დავალება N3\n")

monitor_price = float(input("enter price of monitor: "))
system_unit_price = float(input("enter price of system unit: "))
keyboard_price = float(input("enter price of keyboard: "))
mouse_price = float(input("enter price of mouse: "))


computer_price = monitor_price + system_unit_price + keyboard_price + mouse_price

print(f"Total price for computer is: {computer_price}")

# Exercise N1
user_input = int(input("enter a positive number: "))
if user_input <= 0:
    print("enter a positive integer!")
else:
    while user_input > 0:
        print(user_input)
        user_input -= 1
print('\n')


#Exercise N2
total_sum = 0

while True:
    user_input = input("enter a number or type 'sum' to see sum of numbers: ")

    if user_input.lower() == 'sum':
        break

    try:
        number = int(user_input)
        if number > 0:
            total_sum += number
        else:
            print('only positive integers')       
    except ValueError:
        print("invalid input. enter an integer.")

print(f"total sum of the entered numbers is: {total_sum}")
print('\n')

#Exercise N3

import random

n_to_guess = random.randint(1, 20)
lives = 5

while lives > 0:
    try:
        guess = int(input("enter a number to guess between 1 and 20: "))
        if guess < 1 or guess > 20:
            print("enter a number between 1 and 20!")
            continue
    except ValueError:
        print("invalid input. enter a valid number.")
        continue

    if guess != n_to_guess:
        if guess > n_to_guess:
            print("go lower!")
        else:
            print("go higher!")
        lives -= 1
        if lives == 1:
            print("be careful, u have 1 live left")
        else:
            print(f"u have {lives} lives left")
    else:
        print(f"u won. correct number was: {n_to_guess}.")
        break
else:
    print("U HAVE LOST!")
    print(f"the correct number was {n_to_guess}.")
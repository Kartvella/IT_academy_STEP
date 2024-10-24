#Exercise N1
user_input = input("enter text to check if it is a palindrome: ")
if user_input == user_input[::-1]:
    print(f"word '{user_input}' is a palindrome")
else:
    print(f"word '{user_input}' is NOT a palindrome")


#Exercise N2

text_input = input("enter text/symbols to convert to ASCII: ")
for char in text_input:
    print(ord(char))

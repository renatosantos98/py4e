# Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

user_input = input("Input some text: ")
index = len(user_input) - 1

while index >= 0:
    letter = user_input[index]
    print(letter)
    index = index - 1

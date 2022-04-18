# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

try:
    hrs = float(input("Enter Hours: "))
except:
    print("Error: Please enter numeric input")
    quit()

try:
    rph = float(input("Enter Rate: "))
except:
    print("Error: Please enter numeric input")
    quit()

if hrs > 40:
    pay = round(40 * rph + (hrs - 40) * rph * 1.5, 2)
else:
    pay = round(hrs * rph, 2)

print("Pay:", pay)

# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hrs = float(input('Enter Hours: '))
rph = float(input('Enter Rate: '))
if hrs > 40:
    pay = round(40 * rph + (hrs - 40) * rph * 1.5,2)
else:
    pay = round(hrs * rph,2)
print('Pay:',pay)

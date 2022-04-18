# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

hrs = float(input('Enter Hours: '))
rph = float(input('Enter Rate: '))
pay = round(hrs * rph, 2)
print('Pay:', pay)

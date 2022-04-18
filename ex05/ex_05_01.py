# Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

total = 0
count = 0

while True:
    line = input("Enter a number, or type 'done' to finish: ")
    if line == "done" and count == 0:
        print("Error: Please enter at least one number.")
        continue
    elif line == "done":
        break
    else:
        try:
            number = float(line)
        except:
            print("Error: Invalid Data. Enter a number, or type 'done' to finish.")
            continue
        else:
            total = total + number
            count = count + 1
            average = total / count

print("Total: ", total)
print("Count: ", count)
print("Average: ", average)

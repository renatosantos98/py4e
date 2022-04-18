# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

maximum = None
minimum = None
count = 0

# Loop that prompts the user for input.
while True:
    num = input("Enter a number, or type 'done' to finish: ")
    # Check if 'done' was used as the first input string.
    if num == "done" and count == 0:
        print("Error: Please enter at least one number.")
        continue
    # Check if 'done' was used, but not as the first input string, and break the loop.
    elif num == "done":
        break
    # If the input is a number, convert into float and update number input count.
    else:
        try:
            num = float(num)
        except:
            print("Error: Invalid Data. Enter a number, or type 'done' to finish.")
            continue
        else:
            count = count + 1

    # Check if input is the maximum entered.
    if maximum is None:
        maximum = num
    elif num > maximum:
        maximum = num

    # Check if input is the minimum entered.
    if minimum is None:
        minimum = num
    elif num < minimum:
        minimum = num

# When the loop ends, prints the maximum and minimum values entered.
print("The maximum number is: ", maximum)
print("The minimum number is: ", minimum)

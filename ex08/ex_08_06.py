# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters "done".
# Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

number_list = list()

while True:
    line = input("Enter a number, or type 'done' to finish: ")
    if line == "done" and len(number_list) == 0:
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
            number_list.append(number)

print("Maximum:", max(number_list))
print("Minimum:", min(number_list))

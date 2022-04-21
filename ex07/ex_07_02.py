# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
# X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

# Try to open the file. Except if the file name is invalid.
try:
    fh = input("Enter a file name: ")
    fh = open(fh)
except:
    print("Error: File Not Found")
    quit()
else:
    # Initialize line counting variable.
    count = 0
    value_total = float(0)

    # Grab lines that start with "X-DSPAM-Confidence:".
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            line = line.rstrip()
            count = count + 1
            value_total = value_total + float(line[19:])

    # Calculate average X-DSPAM-Confidence value.
    average = value_total / count
    print("Average Confidence Value: ", average)

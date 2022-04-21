# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

str = "X-DSPAM-Confidence:0.8475"

# Finding the position of the colon on the string.
colon_pos = str.find(":")

# Extracting the slice containing the number from between the colon position and the end of the string.
num = float(str[colon_pos + 1 :])

# Printing the number extracted.
print("Number is:", num)

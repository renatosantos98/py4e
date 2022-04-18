# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).


def computepay(hrs, rph):
    try:
        hrs = float(hrs)
        rph = float(rph)
    except:
        print("Error: Please enter a numeric input.")
        quit()
    else:
        if hrs > 40:
            pay = round(40 * rph + (hrs - 40) * rph * 1.5, 2)
            return pay
        else:
            pay = round(hrs * rph, 2)
            return pay


hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
print(computepay(hours, rate))

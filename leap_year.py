# User Input
year = int(input("Which year do you want to check? "))

#If statements to determine if it's a leap year or not
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

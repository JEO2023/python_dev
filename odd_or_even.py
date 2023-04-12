# User Input
number = int(input("Which number do you want to check? "))

#Checking if odd or even
check_num = number % 2
if (check_num > 0):
    print("This is an odd number.")
else:
    print("This is an even number.")

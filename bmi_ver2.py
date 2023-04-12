# User Input
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


# Calculation to determine BMI
h2 = float(height)*float(height)
BMI = (float(weight)/h2)

#If statement to notify user per result
if (BMI < 18.5):
    print(f"Your BMI is " + "{:.0f}".format(BMI)+ ", you are underweight")
elif (18.5 < BMI < 25):
    print(f"Your BMI is " + "{:.0f}".format(BMI)+ ", you have a normal weight.")
elif (25 < BMI < 30):
    print(f"Your BMI is " + "{:.0f}".format(BMI)+ ", you are slightly overweight.")
elif (30 < BMI < 35):
    print(f"Your BMI is " + "{:.0f}".format(BMI)+ ", you are obese.")
else:
    print(f"Your BMI is " + "{:.0f}".format(BMI)+ ", you are clinically obese.")

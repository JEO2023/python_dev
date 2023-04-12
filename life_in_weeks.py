# User input
age = input("What is your current age?")


#Calculating Life in weeks
years_left = 90 - int(age)
days = years_left * 365
months = years_left * 12
weeks = years_left * 52
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Welcoming message with user input preferences
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# If statement to determine the price per user selection
if (size == 'S'):
    cost = 15;
elif (size == "M"):
    cost = 20;
elif (size == "L"):
    cost = 25;

if (add_pepperoni == "Y" and size == "S"):
    cost = cost + 2
elif (add_pepperoni == "Y" and (size == "M" or size == "L")):
    cost = cost + 3

if (extra_cheese == 'Y'):
    cost = cost + 1
print(f"Your final bill is: ${cost}")

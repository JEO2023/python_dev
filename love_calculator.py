# Welcoming message and user input
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Initializing variables
time1 = 0
time2 = 0

#for loop to verify each letter in names
for i in name1:
    if i in "true" or i in "TRUE":
        time1 += 1
    if i in "love" or i in "LOVE":
        time2 += 1
for i in name2:
    if i in "true" or i in "TRUE":
        time1 += 1
    if i in "love" or i in "LOVE":
        time2 += 1

#Combining and coverting numbers        
time = str(time1) + str(time2)
score = int(time)

#if statement to determine users group
if score < 10 or score > 90:
    print("Your score is " + str(time) + ", you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print("Your score is " + str(time) + ", you are alright together.")
else: 
    print("Your score is " + str(time) + ".")

# User inputs students heights
student_heights = input("Input a list of student heights ").split()

#for loop to go over input and conver them to integers
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#Initializing total height
total_height = 0
for height in student_heights:
    total_height += height
#print(total_height)
total_students = 0 
for student in student_heights:
    total_students += 1
#print(total_students)
final = round(total_height/total_students)
print(final)

#Setting up the map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

#User input
position = input("Where do you want to put the treasure? ")

#Selection the location
x = int(position[0])
y = int(position[1])
map[y-1][x-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

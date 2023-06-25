# Print game grid
grid = [["-" for x in range(3)] for y in range(3)]
for line in grid:
    for x in line:
        print(x, end=" ")
    print()


# Take user input
userSelection = -1
counter = 1
while userSelection > 9 or userSelection < 1:
    try:
        userSelection = int(input("Select a number: "))
        if userSelection > 9 or userSelection < 1:
            print("Number is not in the range (1-9)!")
    except ValueError:
        print("Input is not a number!")
    counter += 1

print(type(userSelection))
# Check for the win or tie

# Switch player

# Check for the win or tie again

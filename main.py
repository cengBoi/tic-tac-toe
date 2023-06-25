# Print game grid
grid = ["-" for x in range(9)]
for index, value in enumerate(grid):
    print(value, end=" ") if index % 3 != 2 else print(value)

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

user_type = "X"

# Print game grid
grid = ["-" for x in range(9)]


def display_grid():
    for index, value in enumerate(grid):
        print(value, end=" ") if index % 3 != 2 else print(value)


display_grid()


# Take user input

def take_input():
    user_selection = -1
    counter = 1
    while user_selection > 9 or user_selection < 1:
        try:
            user_selection = int(input("Select a number: "))
            if user_selection > 9 or user_selection < 1:
                print("Number is not in the range (1-9)!")
            else:
                return user_selection
        except ValueError:
            print("Input is not a number!")
        counter += 1


def evaluate_input():
    cell = take_input() - 1
    while grid[cell] != "-":
        print("This cell is already occupied!")
        cell = take_input()
    grid[cell] = user_type
    display_grid()


evaluate_input()
# Check for the win or tie

# Switch player

# Check for the win or tie again

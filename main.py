user_type = "X"
winner = ""

# Print game grid
grid = ["-" for x in range(9)]


def display_grid():
    for index, value in enumerate(grid):
        print(value, end=" ") if index % 3 != 2 else print(value)


display_grid()


# Take user input

def take_input():
    user_selection = -1
    while user_selection > 9 or user_selection < 1:
        try:
            user_selection = int(input("Select a number: "))
            if user_selection > 9 or user_selection < 1:
                print("Number is not in the range (1-9)!")

            else:
                return user_selection
        except ValueError:
            print("Input is not a number!")


def evaluate_input():
    cell = take_input() - 1
    while grid[cell] != "-":
        print("This cell is already occupied!")
        cell = take_input() - 1
    grid[cell] = user_type
    display_grid()


# Check for the win or tie
def check_horizontal():
    global winner
    for x in range(0, 9, 3):
        if grid[0 + x] == grid[1 + x] and grid[1 + x] == grid[2 + x] and grid[0 + x] != "-":
            winner = user_type
            print("\nWinner is %s" % winner)
            return True


def check_vertical():
    global winner
    for x in range(0, 3, 1):
        if grid[0 + x] == grid[3 + x] and grid[3 + x] == grid[6 + x] and grid[0 + x] != "-":
            winner = user_type
            print("\nWinner is %s" % winner)
            return True


def check_tie():
    global winner
    flag = False
    for x in grid:
        if x == "-":
            flag = True
            break
    if not flag:
        print("\nThere is a tie!")
        winner = "Tie"


def check_diagonal():
    global winner
    if grid[0] == grid[4] and grid[4] == grid[8] and grid[0] != "-" or \
            grid[2] == grid[4] and grid[4] == grid[6] and grid[2] != "-":
        winner = user_type
        print("\nWinner is %s" % winner)
        return True


def check_win_or_tie():
    if check_horizontal():
        return
    if check_vertical():
        return
    if check_diagonal():
        return
    check_tie()


# Switch player
def switch_player():
    global user_type
    user_type = "X" if user_type == "O" else "O"


# Check for the win or tie again

while winner == "":
    evaluate_input()
    check_win_or_tie()
    switch_player()

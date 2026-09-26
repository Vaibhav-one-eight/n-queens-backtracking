
N = 8
board = [["." for _ in range(N)] for _ in range(N)]
attempts = 0


def is_safe(row, col):
    # Check the row to the left
    for j in range(col):
        if board[row][j] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row + 1, col - 1
    while i < N and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def display_board():
    print("\n   " + " ".join(str(i + 1) for i in range(N)))
    print("  " + "--" * N)

    for i, row in enumerate(board, start=1):
        print(f"{i} |" + " ".join(row))


def solve(col):
    global attempts

    if col == N:
        return True

    # Preserve the queen placed by the user
    if col == first_col:
        return solve(col + 1)

    for row in range(N):
        attempts += 1

        if is_safe(row, col):
            board[row][col] = "Q"

            if solve(col + 1):
                return True

            # Backtrack
            board[row][col] = "."

    return False


def get_position(label):
    while True:
        try:
            value = int(input(f"Enter {label} (1-{N}): "))

            if 1 <= value <= N:
                return value - 1

            print(f"Please enter a number between 1 and {N}.")

        except ValueError:
            print("Invalid input. Enter a whole number.")


print("=" * 35)
print("          8 QUEENS PROBLEM")
print("=" * 35)

print("\nChoose the position of the first queen.")

first_row = get_position("row")
first_col = get_position("column")

board[first_row][first_col] = "Q"

print("\nInitial board:")
display_board()

if solve(0):
    print("\nSolution Found!")
    display_board()
else:
    print("\nNo solution found.")

print(f"\nPositions attempted: {attempts}")
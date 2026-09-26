
# N-Queens Backtracking Solver

A Python implementation of the classic **8-Queens Problem** using recursion and backtracking. The program allows users to choose the position of the first queen and then searches for a valid arrangement of the remaining seven queens.

## Features

- Interactive selection of the first queen's position
- Recursive backtracking algorithm
- Row and diagonal conflict detection
- Input validation for row and column selection
- Console-based chessboard display
- Counter showing the number of positions attempted

## How It Works

The N-Queens Problem requires placing N queens on an N × N chessboard so that no two queens attack each other.

This implementation uses an 8 × 8 board. After the user selects the first queen's position, the algorithm attempts to place one queen in each remaining column.

For every candidate position, the program checks whether it is safe. If a placement eventually leads to a dead end, the algorithm removes that queen and tries another position. This process is called **backtracking**.

The search stops when a valid arrangement of eight queens is found.

## Technologies Used

- Python 3
- Recursion
- Backtracking
- Two-dimensional lists

No external libraries are required.

## Project Structure

```text
n-queens-backtracking/
├── n_queens.py
├── README.md
└── screenshots/       # Optional
```

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/n-queens-backtracking.git
   ```

2. Navigate to the project directory:

   ```bash
   cd n-queens-backtracking
   ```

3. Run the program:

   ```bash
   python n_queens.py
   ```

4. Enter the row and column for the first queen when prompted. Both values must be between 1 and 8.

## Example

```text
Choose the position of the first queen.

Enter row (1-8): 1
Enter column (1-8): 1

Initial board:

   1 2 3 4 5 6 7 8
  ----------------
1 |Q . . . . . . .
2 |. . . . . . . .
3 |. . . . . . . .
4 |. . . . . . . .
5 |. . . . . . . .
6 |. . . . . . . .
7 |. . . . . . . .
8 |. . . . . . . .
```

The program then searches for a valid solution and displays the completed board and the number of positions attempted.

## Learning Outcomes

This project demonstrates:

- Solving constraint-satisfaction problems
- Implementing recursive backtracking
- Managing and restoring state during recursive calls
- Working with two-dimensional arrays
- Validating user input

## Future Improvements

- Support different board sizes
- Find and display all valid solutions
- Visualize the backtracking process
- Optimize conflict detection using sets
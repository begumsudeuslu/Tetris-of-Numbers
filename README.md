# Tetris-of-Numbers
This program implements a number elimination game where players remove adjacent matching numbers from a grid until no more valid moves remain. The game starts with an input text file containing a grid of numbers. The player selects a number from the grid, and all adjacent matching numbers are removed. The remaining numbers shift downward, and empty rows/columns are deleted. The game continues until no more matching adjacent numbers exist.

How It Works
- The program reads a grid of numbers from an input text file.
- It prints the initial grid.
- The player selects a position (row and column) to remove a number.
- All adjacent numbers that match the selected number are removed.
- The remaining numbers fall downward to fill empty spaces.
- Empty rows and columns are removed from the grid.
- The player's score is updated based on the sum of removed numbers.
- The game continues until no more adjacent matches exist.
- The final score is displayed, and the game ends.
- Installation and Usage

Implementation of the function island_perimeter:

Understand the Grid and Perimeter Calculation:

The grid is a list of lists of integers where 0 represents water and 1 represents land.
Each land cell has 4 potential sides contributing to the perimeter.
For each land cell, check its adjacent cells (up, down, left, right).
If an adjacent cell is water or out of bounds, it contributes to the perimeter.
Algorithm:

Iterate over each cell in the grid.
For each land cell, check its four adjacent cells.
Count the sides that contribute to the perimeter.
Implementation:

Use nested loops to traverse the grid.
Use conditional checks to determine if a side is part of the perimeter.
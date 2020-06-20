# dynamic_programming_0_1_matrix

A programming challenge to demonstrate dynamic programming

Given a grid of size NxN (N even), can you place 1s and 0s in each cell such that the the number of ones and zeroes in each row 
and column is exactly N/2. How many solutions are there?

The number of solutions is very high (116963796250 for N=8) so a simple backtracking algorithm would not work, as it
would have to visit every solution. Instead we use dynamic programming, which recognises symmetries as we fill the grid
and remembers the number of solutions for a partially filled grid that has symmetry with a previous partially filled 
grid.

My algorithm works in reasonable time up to N=12 (num solutions = 64051375889927380035549804336).
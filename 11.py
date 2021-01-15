""" Project Euler #11: Largest product in a grid """
def solve_grid(grid):
	row_max,col_max,diag1,diag2 = 0,0,0,0
	for r in range(20):
		for c in range(20):
			if c < 17:
				r_s = grid[r][c]*grid[r][c+1]*grid[r][c+2]*grid[r][c+3]
				if r_s > row_max:
					row_max = r_s
			if r < 17:
				c_s = grid[r][c]*grid[r+1][c]*grid[r+2][c]*grid[r+3][c]
				if c_s > col_max:
				   col_max = c_s
			if r < 17 and c < 17:
			    d1_s = grid[r][c]*grid[r+1][c+1]*grid[r+2][c+2]*grid[r+3][c+3]
			    if d1_s > diag1:
			       diag1 = d1_s
			if r < 17 and c > 2 :
			   d2_s = grid[r][c]*grid[r+1][c-1]*grid[r+2][c-2]*grid[r+3][c-3]
			   if d2_s > diag2:
		    		diag2 = d2_s
	print(max(row_max,col_max,diag1,diag2))

grid = [list(map(int,input().split())) for _ in range(20)]	
solve_grid(grid)

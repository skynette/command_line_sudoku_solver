from time import time

board = [
	[0,6,5,   0,1,0,   3,7,0],
	[9,0,8,   0,0,0,   0,0,0],
	[7,0,0,   0,0,0,   8,0,5],
	
	[0,0,0,   9,8,0,   0,0,2],
	[0,5,0,   0,0,1,   0,0,0],
	[0,2,0,   0,4,5,   0,0,0],

	[0,0,0,   0,5,0,   2,0,7],
	[5,0,0,   0,6,0,   0,4,0],
	[0,0,7,   3,2,8,   0,0,0]
]
def printBoard(board):
	horizontal_line = "----------------------"
	for i in range(len(board)):
		# print horizontal line after 3 rows
		if i%3 == 0 and i != 0:
			print(horizontal_line)
		for j in range(len(board[0])):
			# check for intervals to print the vertical lines and stay on the same line
			if j%3 == 0 and j != 0:
				print('| ', end="")
			# check if its the last num so we need to print and go to next line
			if j==8:
				print(board[i][j])
			# else lets just print the current cell value and stay on the same line
			else:
				print(str(board[i][j])+' ', end="")

def getEmptyCell(board):
	for row in range(len(board)):
		for col in range(len(board[0])):
			# check for empty cell and return the position in co-ordinates
			if board[row][col] == 0:
				return (row, col)
	return None

def solve(board):
	# base case: this is for when the sudoku is solved
	# meaning we want to recursively call solve until we cant find empty cells
	find = getEmptyCell(board)
	if not find:
		return True
	else:
		row, col = find
	# next try values from 1 to 9 and if a number fits, then inserts it in the position find
	for i in range(1,10):
		if isValid(board, i, (row, col)):
			# print("\nValid, insering {} into {}".format(str(i), str([row, col])))
			board[row][col] = i
			# printBoard(board)
			if solve(board):
				return True
			# print("\nno match found resetting {} to 0".format(str((row,col))))
			board[row][col] = 0
		
	return False

def isValid(board, number, position):
	# check the row
	# loop through the entire row and check if any cell matches the number we just added in
	x = position[0]
	y = position[1]
	for col in range(len(board[0])):	
		# check all the row cells for the number we just added in and
		# make sure its not the column we just inserted the number
		if board[x][col] == number and y!=col:
			return False
	# check the columns
	# loop through the columns and check if any cell matches the number we just entered
	for row in range(len(board)):
		# check the cols for the number we just added in and
		# make sure its not the row we just inserted number into
		if board[row][y] == number and x != row:
			return False
	# check the mini grids
	x_grid = position[1]//3
	y_grid = position[0]//3
	for i in range(y_grid*3, y_grid*3+3):
		for j in range(x_grid*3, x_grid*3+3):
			if board[i][j] == number and (i, j) != position:
				return False
	return True



s = time()


printBoard(board)
print('===============================')
solve(board)
printBoard(board)
print("in",time()-s,"seconds")

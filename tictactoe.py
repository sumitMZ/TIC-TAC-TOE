#TicTacToe
def displayBoard(board):
	for x in board:
		print()
		for y in x:
			print(y, end='\t')
	print()

def isFull(board):
	for x in board:
		for y in x:
			if y == '[ ]': # EMPTY : '[ ]'
				return False
	return True

def registerMove(board, r, c, sym):
	if r >= 0 and r <= 2:#valid row
		if c >=0 and c <= 2:#valid col
			if board[r][c] == '[ ]':#empty location
				board[r][c] = sym #register a move
				return True #DONE
	return False #ERROR

def checkWins(board, symbol):
	#check rows
	for x in board:
		if x[0] == symbol and x[1] == symbol and x[2] == symbol:
			return True
	# check cols
	for i in range(2): #range(2) : 0,1,2
		if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
			return True
	#diagonal
	if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
		return True
	#reverse diagonal
	if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
		return True

	return False

def tictactoe():
	#setup a board
	row1 = ['[ ]','[ ]','[ ]']
	row2 = ['[ ]','[ ]','[ ]']
	row3 = ['[ ]','[ ]','[ ]']
	board = [row1, row2, row3] # a nested list

	#setup players
	p1 = input('Enter name of first player (X) ')
	p2 = input('Enter name of second player (O) ')
	players = [p1,p2] # a list of strings

	#setup symbols
	symbols= ['[X]', '[O]'] # a list of strings

	#current player
	current = 0 #predecided

	#draw status
	isDraw = True #predecided

	#lets play
	while not isFull(board):
		displayBoard(board)
		# move
		flag = True
		while flag:
			print(players[current], ' plays ')
			r = int(input('Enter row (0-2) '))
			c = int(input('Enter col (0-2) '))
			flag = not registerMove(board, r, c, symbols[current])

		#check for win after the move
		if checkWins(board, symbols[current]):
			displayBoard(board)
			print('Hurray!!!!', players[current], 'WINS :)')
			isDraw = False
			break #stop the game

		#change the player
		current = (current+1) % 2

	#check for draw
	if isDraw:
		displayBoard(board)
		print('Well Played by BOTH!!!')
		print('Game DRAW!!!')

tictactoe()



# N - Queens

# Caelan Neumann

#Problem/Board
def chess_board(n):
    #Create n x n board with underscores as place holders
    chess_board = [[0 for row in range(n)] for col in range(n)]
    for i in range(n):
        for j in range(n):
            chess_board[i][j] = '_'

    return chess_board

#Constraint Check
def check_move(chess_board, curr_row, curr_col, n):
    
    #check row behind
    for i in range(curr_col):
        if chess_board[curr_row][i] == 'Q':
            return False
    
    #Check upward diagonal behind

    for row, col in zip(range(curr_row, -1, -1), range(curr_col, -1, -1)):
        if board[row][col] == 'Q':
            return False
 
    #Check lower diagonal on behind
    for row, col in zip(range(curr_row, n, 1),  range(curr_col, -1, -1)):
        if board[row][col] == 'Q':
            return False
    #Return True if no queens conflicting
    return True


def print_board(chess_board, n):
    for i in range(n):
        for j in range(n):
            print(chess_board[i][j], end=' ')
        print()    

    
def backtracking_csp_nqueen(chess_board, col, n):
    #Check if all the Queens have been placed.
    if col >= n:
        #Print Solution
        print("Solution")
        print_board(chess_board, n)
        return True
    
    #Start current queens search a the ith row in the chess_board
    for i in range(n):
        #if the move is valid place the queen
        if check_move(chess_board, i, col, n):
            chess_board[i][col] = 'Q'
            #recurse until solution or failure
            if backtracking_csp_nqueen(chess_board, col + 1, n):
                return True
            #failure occured backtrack and delete placed queen
            chess_board[i][col] = '_'
    #No solution found ex. 2         
    return False




if __name__ == '__main__':
    #initialize n 
    n = 8
    #blank n x n board
    board = chess_board(n)
    #start at the first column
    col = 0
    #Prints initial board
    print("Start State")
    print_board(board, n)

    #Print Solution or failure
    if not backtracking_csp_nqueen(board, 0, n):
        print("No solutions found for n")



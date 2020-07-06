# Ex2_12  第一个例子的等同做法
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)        # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[2][0] = 'X'  
print(board)        # [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]

# 
row = ['_'] * 3
weird_board = []
for i in range(3):
    weird_board.append(row)
weird_board[2][0] = 'X'
print(weird_board)  # [['X', '_', '_'], ['X', '_', '_'], ['X', '_', '_']]

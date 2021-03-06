# 包含3个列表 的列表， 每个列表各自有3个元素，代表井字游戏的一行方块
board = [['_'] * 3 for i in range(3)]
print(board)    # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X'
print(board)    # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]



# 含有3个指向同一对象的引用的列表毫无用处
# 是对上面情况的错误示范
weird_board = [['_'] * 3] * 3
print(weird_board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
#  外面的列表包含3个指向同一列表额的引用，

weird_board[1][2] = '0'
print(weird_board)  # [['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]

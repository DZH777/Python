import copy
import math

def isWin(board):
  # Row win
  for row in board:
    if row[0] is not None and (row[0] == row[1] == row[2]):
      return row[0]

  # Col win
  for col in range(3):
    if board[0][col] is not None and (board[0][col] == board[1][col] == board[2][col]):
      return board[0][col]

  # Cross win
  if(board[0][0] is not None and (board[0][0] == board[1][1] == board[2][2])):
    return board[0][0]
  
  if(board[0][2] is not None and (board[0][2] == board[1][1] == board[2][0])):
    return board[0][2]

  return None

def isOver(board):
  for row in range(3):
    for col in range(3):
        if (board[row][col] is None):
            return False
  return True

def minMax(board, turn , cnt):
    winner = isWin(board)
    if(isOver(board)):
        if (winner is None):    
            return 0, '00', cnt+1
    if (winner == 'X'):
        return 1, '00', cnt+1
    elif (winner == '0'):
        return -1, '00', cnt+1
       
    if turn == "X":
        val = -math.inf
        ordr = '00'
        ct = -math.inf
        for row in range(3):
            for col in range(3):
                if (board[row][col] is None):
                    temp = copy.deepcopy(board)
                    temp[row][col] = 'X'
                    temp_cnt = cnt+1
                    value, order, count = minMax(temp, '0', temp_cnt)
                    if value > val:
                        val = value
                        ordr = str(row)+str(col)
                        ct = count
                    elif (value == val and count < ct):
                        val = value
                        ordr = str(row)+str(col)
                        ct = count
    else:
        val = math.inf
        ordr = '00'
        ct = math.inf
        for row in range(3):
            for col in range(3):
                if (board[row][col] is None):
                    temp = copy.deepcopy(board)
                    temp[row][col] = '0'
                    temp_cnt = cnt+1
                    value, order, count = minMax(temp, 'X', temp_cnt)
                    if value < val:
                        val = value
                        ordr = str(row)+str(col)
                        ct = count
                    elif (value == val and count < ct):
                        val = value
                        ordr = str(row)+str(col)
                        ct = count
    return val, ordr, ct
    
temp = [['0', '0', 'X'],
        [None, 'X', 'X'],
        ['0', None, '0']]
turn = 'X'
value, order, count = minMax(temp, turn, 0)
print('------')
print(str(value) + '-' + order + '-' + str(count))
    

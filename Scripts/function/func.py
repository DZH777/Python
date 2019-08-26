import copy

def testRec1(board, char):
    board[0][0] = char

def testRec2(board, char):
    temp = board.copy()
    temp[0][0] = char
    temp1 = board[:]
    temp1[0][1] = 'Z'
    temp2 = list(board)
    temp2[0][2] = 'X'
    temp3 = copy.copy(board)
    temp2[1][0] = 'S'
    
test1 = [[None, None, None], [None, None, None], [None, None, None]]
testRec1(test1, 'X')
print(test1)

test2 = [[None, None, None], [None, None, None], [None, None, None]]
testRec2(test2, 'Y')
print(test2)

temp1 = test2[:]
temp1[1][1] = 'J'
print("temp1 " + str(temp1))
print("test2 " + str(test2))




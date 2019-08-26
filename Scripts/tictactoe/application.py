from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp
import copy
import math
 
app = Flask(__name__)
 
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
 
@app.route("/")
def index():
 
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        session["winner"] = None
        session["steps"] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        session["steps_num"] = 0
    return render_template("game.html", game=session["board"], turn=session["turn"], winner=session["winner"], steps_num=session["steps_num"], steps = session["steps"])
 
@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    session["steps_num"] += 1;
    session["steps"][row][col] = session["steps_num"]
    if(isWin(session["board"]) is not None):
        session["winner"] = session["turn"]
    else:
        if(isOver(session["board"])):
            session["winner"] = "ДРУЖБА"
    if (session["turn"] == "X"):
        session["turn"] = "0"
    else:
        session["turn"] = "X"
	
    return redirect(url_for("index"))

@app.route("/newgame")
def newgame():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["turn"] = "X"
    session["winner"] = None
    session["steps"] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    session["steps_num"] = 0

    return redirect(url_for("index"))

@app.route("/undo")
def undo():
    if session["steps_num"] > 0:
        for row in range(3):
            for col in range(3):
                if session["steps"][row][col] == session["steps_num"]:
                    session["steps"][row][col] = 0
                    session["board"][row][col] = None
                    session["steps_num"] -= 1
                    if (session["turn"] == "X"):
                        session["turn"] = "0"
                    else:
                        session["turn"] = "X"
                    if session["winner"]:
                        session["winner"] = None                
                    return redirect(url_for("index"))
    else:                
        return redirect(url_for("index"))                

@app.route("/auto")
def auto():
    if session["winner"]:
        return redirect(url_for("index"))
    else:
        value, order, count = minMax(session["board"], session["turn"], 0)
        for row in range(3):
            for col in range(3):
                if (str(row)+str(col) == order):
                    play(row, col)
                    return redirect(url_for("index"))

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
                    value, order, count = minMax(temp, '0', cnt+1)
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
                    value, order, count = minMax(temp, 'X', cnt+1)
                    if value < val:
                        val = value
                        ordr = str(row)+str(col)
                        ct = count
                    elif (value == val and count < ct):
                        val = value
                        ordr = str(row)+str(col)
                        ct = count
    return val, ordr, ct
    
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


    

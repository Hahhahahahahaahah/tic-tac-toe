import turtle

turn = 1
board = [[0,0,0],[0,0,0],[0,0,0]]
EAST, NORTH = 0,90
LINE_LEN = 6
L1_X, L1_Y = -3,1
L2_X, L2_Y = -3,-1
L3_X, L3_Y = -1,-3
L4_X, L4_Y = 1,-3
coords = [(L1_X, L1_Y),(L2_X, L2_Y),(L3_X, L3_Y),(L4_X, L4_Y)]
directions = [0,0,90,90]
def setup():
  global screen, turt
  screen = turtle.getscreen()
  turt = turtle.getturtle()
  screen.setup(800,800)
  screen.title("Tic Tac Toe")
  turt.speed(0)
  screen.setworldcoordinates(-5,-5,5,5)
  turt.speed("fastest")
  turt.hideturtle()
  draw_lines()
def draw_lines():
  turt.color("black")
  turt.pensize(10)

  for i in range(4):
    turt.penup()
    turt.goto(coords[i])
    turt.seth(directions[i])
    turt.pendown()
    turt.forward(LINE_LEN)

def draw(board):
  draw_lines()
  for row_index in range(3):
    for col_index in range(3):
      draw_move(row_index, col_index, board[row_index][col_index])

def draw_move(row_index, col_index, move):
  if move == 0: return
  intermediate_x = 2*(col_index - 1)
  intermediate_y = -2* (row_index - 1)
  if move == 1: draw_cross(intermediate_x,intermediate_y)
  else: draw_circle(intermediate_x,intermediate_y)

def draw_cross(x, y):
  turt.color("blue")
  turt.up()
  turt.goto(x - 0.75, y - 0.75)
  turt.down()
  turt.goto(x + 0.75 ,y + 0.75)
  turt.up()
  turt.goto(x - 0.75, y + 0.75)
  turt.down()
  turt.goto(x + 0.75 ,y - 0.75)
  turt.up()
def draw_circle(x, y):
  turt.color("red")
  turt.up()
  turt.goto(x, y -0.75)
  turt.seth(EAST)
  turt.down()
  turt.circle(0.75, steps = 100)
  turt.up()
  
def play(x,y):
  global turn
  is_first_row = 1 < y and y < 3
  is_second_row = -1 < y and y < 1
  is_third_row = -3 < y and y < -1

  is_first_col = -3 < x and x < -1
  is_second_col = -1 < x and x < 1
  is_third_col = 1 < x and x < 3

  if is_first_row:
   row_index = 0
  elif is_second_row:
   row_index = 1
  elif is_third_row:
   row_index = 2
  else:
    return
  if is_first_col:
   col_index = 0
  elif is_second_col:
   col_index = 1
  elif is_third_col:
   col_index = 2
  else:
    return

  
  if board[row_index][col_index] != 0: return 
  board[row_index][col_index] = turn
  
  if turn == 1:
    turn = 2
  else:
    turn = 1
  draw(board)
def check_outcome(board):
  if board[0][0] > 0 and board[0][0] == board[0][1] and board[0][1]== board[0][2]:
    return board[0][0]
  if board[1][0] > 0 and board[1][0] == board[1][1] and board[1][1]== board[1][2]:
    return board[1][0]
  if board[2][0] > 0 and board[2][0] == board[2][1] and board[2][1]== board[2][2]:
    return board[2][0]
  if board[0][0] > 0 and board[0][0] == board[1][0] and board[1][0]== board[2][0]:
    return board[0][0]
  if board[0][1] > 0 and board[0][1] == board[1][1] and board[1][1]== board[2][1]:
    return board[0][1]
  if board[0][2] > 0 and board[0][2] == board[1][2] and board[1][2]== board[2][2]:
    return board[0][2]
  if board[0][0] > 0 and board[0][0] == board[1][1] and board[1][1]== board[2][2]:
    return board[0][0]
  if board[2][0] > 0 and board[2][0] == board[1][1] and board[1][1]== board[0][2]:
    return board[2][0]

def check_tie(board):
  for row in range(3):
    for col in range(3):
      if (board[row][col] == 0):
        return False
  return True
  

def main():
  setup()
  screen.onscreenclick(play)
  draw(board)
  turtle.mainloop()

if __name__ == "__main__":
  main()

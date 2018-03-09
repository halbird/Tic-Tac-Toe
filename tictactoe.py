
board = []
for x in range(3):
  board.append(["-"] * 3)
def print_board(board):
  for row in board:
    print (" ".join(row))
  
  
def player_1_turn():
    print("Player one turn.")
    player_1_row = int(input("Chose a row:"))-1
    player_1_col = int(input("Chose a column:"))-1
    
    if player_1_row > 2 or player_1_col > 2 or player_1_row < 0 or player_1_col < 0:
      print("That isn't on the board...")
      player_1_turn()
    elif board[player_1_row][player_1_col] == "-":
      board[player_1_row][player_1_col] = "O"
    else:
      print("There's already a symbol here!")
      player_1_turn()
    
    
def player_2_turn():
  print("Player two turn.")
  player_2_row = int(input("Chose a row:"))-1
  player_2_col = int(input("Chose a column:"))-1
  
  if player_2_row > 2 or player_2_col > 2 or player_2_row < 0 or player_2_col < 0:
      print("That isn't on the board...")
      player_2_turn()    
  elif board[player_2_row][player_2_col] == "-":
    board[player_2_row][player_2_col] = "X"
  else:
    print("There's already a symbol here!")
    player_2_turn()
  
  
for turn in range(6):
  player_1_turn()
  print_board(board)
  if board[0][0] == board[0][1] == board[0][2] == "O" or board[0][0] == board[1][1] == board[2][2] == "O" or board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or board[0][2] == board[1][2] == board[2][2] == "O" or board[1][0] == board[1][1] == board[1][2] =="O" or board[2][0] == board[2][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
    print("We have a winner! Player One.")
    break
  for list in board:
    for symbol in list:
      count = 0
      if symbol == "-":
        count += 1
  if count == 0:
    print("No one wins :(")
    break
  
    
  
  player_2_turn()
  print_board(board)
  if board[0][0] == board[0][1] == board[0][2] == "X" or board[0][0] == board[1][1] == board[2][2] == "X" or board[0][0] == board[1][0] == board[2][0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or board[0][2] == board[1][2] == board[2][2] == "X" or board[1][0] == board[1][1] == board[1][2] == "X" or board[2][0] == board[2][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
    print("We have a winner! Player Two.")
    break
  for list in board:
    for symbol in list:
      count = 0
      if symbol == "-":
        count += 1
  if count == 0:
    print("No one wins :(")
    break
  
  

  

board = [[' ' for _ in range(3)] for _ in range(3)]
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)
def check_win(player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): 
            return True
        if all([board[j][i] == player for j in range(3)]): 
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    return False
def is_board_full():
    return all([cell != ' ' for row in board for cell in row])

current_player = 'X'

while True:
    print_board()
    row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
    col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
    
    if board[row][col] == ' ':
        board[row][col] = current_player
    else:
        print("Cell is already taken!")
        continue
    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break
    if is_board_full():
        print_board()
        print("The game is a tie!")
        break
    current_player = 'O' if current_player == 'X' else 'X'
import random

board = []


def print_board():
    print("-------------")
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                print("| X ", end="")
            elif board[i][j] == "O":
                print("| O ", end="")
            else:
                print("|   ", end="")
        print("|")
        print("-------------")


def check_winner(player):
    won = False
    symbol = "X" if player else "O"

    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            won = True
            break
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            won = True
            break

    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        won = True

    if board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol:
        won = True

    return won


def computer_move():
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)

        if board[i][j] == "":
            break

    board[i][j] = "O"


def check_board():
    full_board = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                full_board = False
                break
    return full_board


for num1 in range(3):
    row = []
    for num2 in range(3):
        row.append("")
    board.append(row)

print_board()

game = True
while game:
    position = input("Enter Your position on board (e.g. 1, 1): ")
    try:
        positions = position.split(",")
        x = int(positions[0].strip()) - 1
        y = int(positions[1].strip()) - 1
        skip_round = False
        player_won = bool

        if board[x][y] != "":
            print("Position taken, try again!")
            skip_round = True
        else:
            board[x][y] = "X"
            print_board()

        if not skip_round:
            player_won = check_winner(True)
            if player_won:
                print("You won!")
                game = False

        board_full = check_board()
        if not player_won and board_full:
            print("It's a tie!")
            game = False

        if game:
            computer_move()
            print_board()
            computer_won = check_winner(False)
            if computer_won:
                print("Computer won!")
                game = False
    except ValueError:
        print("Invalid input, try again!")

import random


# to display board
def display_board(board):
    print("\n" * 100)
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("--+---+--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--+---+--")
    print(board[7] + " | " + board[8] + " | " + board[9])


# choose player and marker
def choose_player_and_marker():
    if random.randint(0, 1) == 0:
        player = 'player 1'
        marker1 = 'X'
        marker2 = 'O'
    else:
        player = 'player 2'
        marker1 = 'X'
        marker2 = 'O'

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input(player + ",  choose X or O: ").upper()

        if not (marker == 'X' or marker == 'O'):
            print("Sorry, invalid entry")

    if marker == marker1:
        return player, marker1, marker2
    else:
        return player, marker2, marker1


# select position
def place_marker(board, mark, position):
    board[position] = mark


# win check
def win_check(board, mark):
    return (
            (board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark)
    )


def space_check(board, position):
    return board[position] == ' '


# to check if board is full or not
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# to choose position
def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("choose your position (1, 9): "))

        if position not in range(1, 10) or not space_check(board, position):
            print('Sorry, invalid selection')

    return position


# to replay
def replay():
    choice = ''
    while choice not in ['Y', 'N']:
        choice = input('Do you want to play again (Y, N): ').upper()

    if choice not in ['Y', 'N']:
        print('sorry, invalid selection')

    if choice == 'Y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

while True:
    # reset the board
    the_board = [' '] * 10
    player, player1_marker, player2_marker = choose_player_and_marker()
    print(player + ' will go first.')

    play_game = input('Are you ready to play? (Y, N): ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if player == 'player 1':

            # display board
            display_board(the_board)
            # select position
            position = player_choice(the_board)
            # place marker
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congrats!' + player + ' won the game.')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is draw')
                    game_on = False
                else:
                    player = 'player 2'
        else:
            # display board
            display_board(the_board)
            # select position
            position = player_choice(the_board)
            # place marker
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Congrats!' + player + ' won the game.')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is draw')
                    game_on = False
                else:
                    player = 'player 1'

    if not replay():
        break

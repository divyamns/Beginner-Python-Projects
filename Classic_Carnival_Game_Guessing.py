from random import shuffle


def shuffle_list(mylist):
    # function to shuffle list
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''
    while guess not in [0, 1, 2]:
        guess = int(input("guess numbers between 0, 1 and 2: "))

    return guess


def check_player_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("correct guess")
    else:
        player_guess()
        print('wrong guess')
        print(mylist)


mylist = ['', 'O', '']
mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_player_guess(mixedup_list, guess)

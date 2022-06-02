import random

from matplotlib.pyplot import pause

def play_game():
    while True:
        options = ['R', 'P', 'S']

        user = input("Choose from the following: 'R' for rock, 'P' for paper, 'S' for scissors: ")
        user = user.upper()
        computer = random.choice(options)

        
        if user not in options:
            print('Invalid option. Try again')
            break


        if user == computer:
            print('You both chose {}. It is a tie'.format(computer))
            return play_game()


        if to_win(user, computer):
            return 'Player: {}, Computer: {}. You won!'.format(user, computer)
        
        return 'Player: {}, Computer: {}. You lost!'.format(user, computer)

def to_win(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    

print(play_game())

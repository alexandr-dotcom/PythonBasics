import random

should_continue = True

while should_continue == True:
    players_choice = input('Players choice: [R/P/S]: ').lower()

    if players_choice not in ['r', 'p', 's']:
        print('Incorrect input. Try again!')
        continue

    comp_choice = random.choice(['r', 'p', 's'])
    print(f'Computer choice = {comp_choice}')

    win_cases = [('p', 'r'), ('r', 's'), ('s', 'p')]
    if players_choice == comp_choice:
        print('Draw!')
    elif (players_choice, comp_choice) in win_cases:
        print('Human wins!')
    else:
        print('Computer wins!')\

    should_continue = input('Want to continue? [y/n]: ').lower() == 'y'
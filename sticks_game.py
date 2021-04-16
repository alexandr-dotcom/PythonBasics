sticks = 10

player_turn = 1

while sticks > 0:
    print(f'How many sticks do you want to remove? Remaining {sticks}')
    taken = int(input())

    if taken < 1 or taken > 3:
        print(f'Should be 1, 2 or 3.')
        continue
    sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if sticks <= 0:
        print(f'No more sticks left.\nPlayer {player_turn} has lost!')
    player_turn = 1 if player_turn == 2 else 2




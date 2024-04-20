from tic_tac_toe import Board
from random import randint


board = Board(randint(0, 1))
show = [1, 2, 3, 4, 5, 6, 7, 8, 9]
replay = False

while True:
    # Printing the board in a good format
    print('\n' + f'   +   +   ')
    print(f' {show[0]} | {show[1]} | {show[2]} ')
    print(f'+--+---+--+')
    print(f' {show[3]} | {show[4]} | {show[5]} ')
    print(f'+--+---+--+')
    print(f' {show[6]} | {show[7]} | {show[8]} ')
    print(f'   +   +   ' + '\n')

    move = input(f'Turn of {'X' if board.turn == 1 else 'O'} - ')
    if not move.isnumeric(): 
        print('Invalid move, please enter a number from 0 to 9')
        continue

    else: 
        code = board.move(int(move))
    
    # Checking for invalid moves
    if code == 1:
        print('Invalid move, please enter a number from 0 to 9')
        continue

    elif code == 2:
        print('That square is already filled')
        continue

    else:
        # The move is correct so we continue
        show[int(move) - 1] = 'X' if board.turn == 0 else 'O'
    
    # Checking if someone won the game
    code = board.check_win()

    if code == 1:
        print('\n' + '+---------------+')
        print(f'|     X Won     |')
        print('+---------------+' + '\n')
        replay = True

    elif code == 0:
        print('\n' + '+---------------+')
        print(f'|     O Won     |')
        print('+---------------+' + '\n')
        replay = True

    elif code == 2:
        print('\n' + '+---------------+')
        print(f'|      Tie      |')
        print('+---------------+' + '\n')
        replay = True
    
    else: pass

    # Allowing for replay after winning
    if replay:
        input('Press any key to play again - ')
        print('\n\n')
        board.reset(randint(0, 1))
        show = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        replay = False

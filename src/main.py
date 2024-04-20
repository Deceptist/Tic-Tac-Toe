# Representation of the tictactoe board
# O - 0, X - 1
board = [
    None, None, None,
    None, None, None,
    None, None, None
]


chance = 1
playing = True
while playing:
    board_draw_range = [0, 3]
    for _ in range(3):
        for sq in board[board_draw_range[0]: board_draw_range[1]]:
            if sq is None:
                print('#', end='    ')

            elif sq == 1:
                print('x', end='    ')
            
            else:
                print('O', end='    ')
        
        print()
        board_draw_range[0] += 3
        board_draw_range[1] += 3
    
    board_draw_range = [0, 3]
    move = input(f'\nMove [{'X' if chance == 1 else 'O'}]: ')

    # If the move is invalid in any way
    if not move.isnumeric() or int(move) < 1 or int(move) > 9 or board[int(move) - 1] is not None:
        print('Invalid move, please enter a number from 1 - 9')
        print('Make sure the square is not already filled\n')
        continue
    
    # Changing whose move it is
    move = int(move)
    board[move - 1] = chance
    if chance == 1: chance = 0
    else: chance = 1

    # Checking if someone won the game
    winning_patterns = [
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Verticals
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontals
        [0, 4, 8], [2, 4, 6] # Diagonals
    ]

    for pattern in winning_patterns:
        # Checking if 1 or 0 are in a specific pattern
        if board[pattern[0]] == 1 and board[pattern[1]] == 1 and board[pattern[2]] == 1:
            print('X won the game!\n')
            playing = False

        elif board[pattern[0]] == 0 and board[pattern[1]] == 0 and board[pattern[2]] == 0:
            print('O won the game!\n')
            playing = False
        
        else: pass

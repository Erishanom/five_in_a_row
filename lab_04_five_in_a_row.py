def print_game(game):
    # Prints the game to the console.

    print(" y")

    y = game['height'] - 1
    while 0 <= y:

        print(str(y)+"|", end="")

        for x in range(game['width']):
            print(get_cell_value(game, x, y), end="")
        print()

        y -= 1

    print("-+", end="")
    for x in range(game['width']):
        print("-", end="")
    print("x")
    print(" |", end="")
    for x in range(game['width']):
        print(x, end="")
    print(" ")

def get_cell_value(game, x, y):
    all_cell_value = game.get('x-moves')+ game.get('o-moves')
    for i in all_cell_value:
        if i.get('x') == x and i.get('y') == y:
            return i.get('player')
    return ' '

    # Returns 'X' if a cross has been placed in the cell with the given coordinates.
    # Returns 'O' if a circle has been placed in the cell with the given coordinates.
    # Returns ' ' otherwise.
    return ' '

def make_move(game, x, y, next_player):
    if next_player=='X':
        newest_move = {'x': x, 'y': y}
        game.get('x-moves').append(newest_move)
    elif next_player =='O':
        newest_move = {'x': x, 'y': y}
        game.get('x-moves').append(newest_move)
        
        

    # Adds a new move to the game with the information in the parameters.
    

def does_cell_exist(game, x, y):
    if 0<=x <10 and 0<=y <10:
        return True
    else:
        return False
    # Returns True if the game contains a cell with the given coordinates.
    # Returns False otherwise.

def is_cell_free(game, x, y):
    all_cell_taken = game.get('moves')

    for i in all_cell_taken:
        if i.get('x') == x and i.get('y') == y:
            return False
    return True
    # Returns True if the cell at the given coordinates doesn't contain a cross or a circle.
    # Returns False otherwise.


def get_next_players_turn(game, i):
    if i%2 == 0:
        playing_piece = 'X'
        return playing_piece
    else: 
        playing_piece = 'O'
        return playing_piece
    # Returns 'X' if a cross should be placed on the board next.
    # Returns 'O' if a circle should be placed on the board next.


def get_winner(game):
    check_if_x_is_winner = game.get('moves')
    t=0
    winner_dict =  [
        {'x': 0, 'y': 0,} 
        {'x': 1, 'y': 0,}
        {'x': 2, 'y': 0,}
        {'x': 3, 'y': 0,}
        {'x': 4, 'y': 0,}
        ]
    for key in winner_dict.keys():
        if (not key in check_if_x_is_winner) or (not winner_dict[key] == check_if_x_is_winner[key]):
            for i in len(winner_dict):
                i['x'] +=1
                t+=1
                if t >=5:
                    return 'X'
         else:
             if 


    # Returns 'X' if 5 crosses in a row is found in the game.
    # Returns 'O' if 5 circles in a row is found in the game.
    # Returns ' ' otherwise.
    return ' '
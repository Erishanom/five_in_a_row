def print_game(game, next_player):
    # Prints the game to the console.

    print(" y")

    y = game['height'] - 1
    while 0 <= y:

        print(str(y)+"|", end="")

        for x in range(game['width']):
            print(get_cell_value(game, x, y, next_player), end="")
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

def get_cell_value(game, x, y, next_player):
    all_cell_value = game.get('x-moves')
    for i in all_cell_value:
        if i.get('x') == x and i.get('y') == y:
            return 'X'
    
    all_cell_value = game.get('o-moves')
    for i in all_cell_value:
        if i.get('x') == x and i.get('y') == y:
            return 'O'

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
        game.get('o-moves').append(newest_move)
        
        

    # Adds a new move to the game with the information in the parameters.
    

def does_cell_exist(game, x, y):
    if 0<=x <10 and 0<=y <10:
        return True
    else:
        return False
    # Returns True if the game contains a cell with the given coordinates.
    # Returns False otherwise.

def is_cell_free(game, x, y):
    all_cell_taken = game.get('x-moves') + game.get('o-moves')

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

def check_horizontal(game, next_player):
    if next_player == 'X':
         check_if_winner = game.get('x-moves')
    else:
         check_if_winner = game.get('o-moves')
    for y in range (0,9):
        for x in range (0,5):
            winner_dict =[
                {'x': x, 'y': y},
                {'x': x+1, 'y': y},
                {'x': x+2, 'y': y},
                {'x': x+3, 'y': y},
                {'x': x+4, 'y': y}]
            if winner_dict in check_if_winner:
                return next_player
                
    return False

 
def check_vertical(game, next_player):
    if next_player == 'X':
         check_if_winner = game.get('x-moves')
    else:
         check_if_winner = game.get('o-moves')
    for x in range (0,9):
        for y in range (0,5):
            winner_dict =  [
                {'x': x, 'y': y},
                {'x': x, 'y': y+1},
                {'x': x, 'y': y+2},
                {'x': x, 'y': y+3},
                {'x': x, 'y': y+4}]
            if winner_dict in check_if_winner:
                return next_player
    return False

def check_diagonal_up(game, next_player):
    if next_player == 'X':
         check_if_winner = game.get('x-moves')
    else:
         check_if_winner = game.get('o-moves')
    for y in range (0,5):
        for x in range (0,5):
            winner_dict =  [
                {'x': x, 'y': y},
                {'x': x+1, 'y': y+1},
                {'x': x+2, 'y': y+2},
                {'x': x+3, 'y': y+3},
                {'x': x+4, 'y': y+4}]
            if winner_dict in check_if_winner:
                return True
    return False     

def check_diagonal_down(game, next_player):
    if next_player == 'X':
         check_if_winner = game.get('x-moves')
    else:
         check_if_winner = game.get('o-moves')
    check_if_winner.sort()
    for y in range (0,5):
        for x in range (5,9):
            winner_dict =  [
                {'x': x, 'y': y},
                {'x': x-1, 'y': y+1},
                {'x': x-2, 'y': y+2},
                {'x': x-3, 'y': y+3},
                {'x': x-4, 'y': y+4}]
            if winner_dict in check_if_winner:
                return True
    return False

def get_winner(game, next_player):
    if check_horizontal(game, next_player) == True:
        return True
    elif check_vertical(game, next_player) == True:
        return True
    elif check_diagonal_up(game, next_player) == True:
        return True
    elif check_diagonal_down(game, next_player) == True:
        return True
    else:
        return ' '
    # Returns 'X' if 5 crosses in a row is found in the game.
    # Returns 'O' if 5 circles in a row is found in the game.
    # Returns ' ' otherwise.
    return ' '

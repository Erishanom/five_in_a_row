import lab_04_five_in_a_row as five

# This dictonary contains the entire state of the game.
game = {
    'width': 10,
    'height': 10,
    'x-moves': [
        {'x': 0, 'y': 0},
        {'x': 1, 'y': 0},
        {'x': 2, 'y': 0},
        {'x': 6, 'y': 6},
        {'x': 8, 'y': 8}

    ],
    'o-moves': [
        {'x': 1, 'y': 1},
        {'x': 3, 'y': 3},
        {'x': 5, 'y': 5},
        {'x': 7, 'y': 7},
        {'x': 9, 'y': 9}
        ]
}
i=2
next_player='X'
while five.get_winner(game, next_player) == ' ':

    # Print the game board.
    five.print_game(game, next_player)

    # Ask the user to enter coordinates.
    next_player = five.get_next_players_turn(game, i)

    print("Enter the x and y coordinate for the cell to place "+next_player+" in.")
    print("Separate the coordinates by space, e.g: 3 5")

    are_entered_coordinates_ok = False

    while not are_entered_coordinates_ok:

        coordinates_string = input("Write: ")
        coordinates = coordinates_string.split(" ")

        x = int(coordinates[0])
        y = int(coordinates[1])
        

        if not five.does_cell_exist(game, x, y):
            print("No cell with the coordinates x="+str(x)+" y="+str(y)+" exists, try again!")
        elif not five.is_cell_free(game, x, y):
            print("The cell with the coordinates x="+str(x)+" y="+str(y)+" is not free, try again!")
        else:
            are_entered_coordinates_ok = True
            i+=1
    five.make_move(game, x, y, next_player)

five.print_game(game, next_player)
print("The game is over, and the winner is: "+five.get_winner(game, next_player)+"!")

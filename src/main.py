#### src/main.py ####
### Main code for a Tic-Tac-Toe game controller with a Tkinter UI. (MVC pattern)
import tkinter as tk
from game import *

the_game = Game()
window = tk.Tk()
window.title("Tic Tac Toe")


### UI Design ###

## Initialize the message (Label):
message = the_game.get_turn().value + "'s turn"
message_label = tk.Label(window, text=message)
message_label.grid(row=0, column=1)

## Initialize the board (buttons):
square_button = [[tk.Button(window, width=15, height=6) for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        square_button[i][j].grid(row=i+1, column=j)
        info = square_button[i][j].grid_info()

## Initialize the restart button (button):
restart_button = tk.Button(window, text= "Restart")
restart_button.grid(row=4, column=1)



### Logic of the game ###

## Functionality of a pressed square:
def square_button_action(event):
    button : tk.Button = event.widget
    print(button.cget('text'))
    
    # Return if the press is not valid:
    print(the_game.get_game_state(), the_game.get_turn())
    if button.cget('text') != '' or the_game.get_game_state() != Game_State.ONGOING:
        return

    # Set the square's view:
    txt = the_game.get_turn().value
    print(txt)
    button.config(text=txt)
    
    # Get the square's position
    info = button.grid_info()
    i, j = info["row"], info["column"]
    print(i, j)
    
    # Set the square's state:
    the_game.update_square_state(i - 1, j)

    # Update the game's state:
    the_game.update_game_state()

    # Check the game's state: 
    print(the_game.get_game_state())
    message = ""
     #  DRAW: Update the message and squares colors, then flip turns
    
     #  WIN: Update the message, get winning positions, and update square colors, then flip turns
    if the_game.get_game_state() == Game_State.WIN:
        message = the_game.get_turn().value + " Wins"
        print("message:", message)
        winning_positions = the_game.get_winning_positions()
        print(winning_positions)

    # Flip the turn:
    the_game.flip_turn()
    
     #  ONGOING: flip the turn, then update the message
    if the_game.get_game_state() == Game_State.ONGOING:
        message = the_game.get_turn().value + "'s turn"
    
    # Update the message:
    message_label.config(text=message)

for row in square_button:
    for button in row: 
        button.bind("<Button-1>", square_button_action)
        button.bind("<space>", square_button_action)

## Functionality of the restart button:
def restart_button_action():
    # Reset the current game:
    the_game.reset()

    # Clear the board view:
    for row in square_button:
        for button in row: button.config(text='')
    
    # Show Who's turn:
    message = the_game.get_turn().value + "'s turn"
    message_label.config(text=message)

restart_button.config(command=restart_button_action)


### Run the program ###
window.mainloop() 
import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

### UI Design
# Create the title (Label):
title_label = tk.Label(window, text= "X's turn")
title_label.grid(row=0, column=1)

# Create the board (buttons):
square_button = [[tk.Button(window, width=15, height=6) for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        square_button[i][j].grid(row=i+1, column=j)
        info = square_button[i][j].grid_info()

# Create the restart button (button):
restart_button = tk.Button(window, text= "Restart")
restart_button.grid(row=4, column=1)
# print(type(restart_button))

### Logic of the game
# for row in square_button:
#     for button in row: print(button.grid_info()["row"], button.grid_info()["column"])
# button = square_button[0][0]
# [print(button.grid_info()["row"], button.grid_info()["column"]) for row in square_button for button in row]

def square_button_action(event):
    button : tk.Button = event.widget
    print(button.cget('text'))
    if button.cget('text') != '': return
    info = button.grid_info()
    print(info["row"], info["column"])
    
    button.config(text='X')
for row in square_button:
    for button in row: 
        button.bind("<Button-1>", square_button_action)
        button.bind("<space>", square_button_action)

def restart_button_action():
    for row in square_button:
        for button in row: button.config(text='')
restart_button.config(command=restart_button_action)
window.mainloop()
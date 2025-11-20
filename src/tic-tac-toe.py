import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

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

window.mainloop()
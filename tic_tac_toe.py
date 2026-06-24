from tkinter import *

root = Tk()
root.title("Tic Tac Toe")

player = "X"

buttons = []

def click(button):
    global player

    if button["text"] == "":
        button["text"] = player

        if player == "X":
            player = "O"
        else:
            player = "X"

for row in range(3):
    row_buttons = []

    for col in range(3):
        button = Button(
            root,
            text="",
            width=10,
            height=4,
            font=("Arial", 20),
        )
        button.config(command=lambda b=button: click(b))
        button.grid(row=row, column=col)

        row_buttons.append(button)

    buttons.append(row_buttons)

root.mainloop()
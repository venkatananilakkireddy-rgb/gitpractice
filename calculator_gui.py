from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

Entry(root, textvariable=equation, font=("Arial", 20)).pack(fill="both")

Button(root, text="7", command=lambda: press(7)).pack(fill="both")
Button(root, text="8", command=lambda: press(8)).pack(fill="both")
Button(root, text="9", command=lambda: press(9)).pack(fill="both")
Button(root, text="+", command=lambda: press("+")).pack(fill="both")

Button(root, text="4", command=lambda: press(4)).pack(fill="both")
Button(root, text="5", command=lambda: press(5)).pack(fill="both")
Button(root, text="6", command=lambda: press(6)).pack(fill="both")
Button(root, text="-", command=lambda: press("-")).pack(fill="both")

Button(root, text="1", command=lambda: press(1)).pack(fill="both")
Button(root, text="2", command=lambda: press(2)).pack(fill="both")
Button(root, text="3", command=lambda: press(3)).pack(fill="both")
Button(root, text="", command=lambda: press("")).pack(fill="both")

Button(root, text="0", command=lambda: press(0)).pack(fill="both")
Button(root, text="/", command=lambda: press("/")).pack(fill="both")
Button(root, text="=", command=equal).pack(fill="both")
Button(root, text="Clear", command=clear).pack(fill="both")

root.mainloop()
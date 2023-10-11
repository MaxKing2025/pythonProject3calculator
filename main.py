from tkinter import*
expression = ""


root = Tk()
root.configure(background= "red2")
root.title("My calculator")
root.geometry("325x200")


my_math = StringVar()
math_box = Entry(root, textvariable=my_math)
math_box.grid(columnspan = 5, ipadx = 70)

def key_press(number):
    global expression
    expression = expression + str(number)
    print(expression)
    my_math.set(expression)
def total():
    global expression
    total2 = str(eval(expression))
    my_math.set(total2)
    expression = ""
def clear():
    global expression
    expression = ""
    my_math.set("")


button_1 = Button(root, text="1", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(1), height = 1, width = 5)
button_1.grid(row = 1, column = 1)

button_2 = Button(root, text="2", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(2), height = 1, width = 5)
button_2.grid(row = 1, column = 2)

button_3 = Button(root, text="3", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(3), height = 1, width = 5)
button_3.grid(row = 1, column = 3)

button_4 = Button(root, text="4", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(4), height = 1, width = 5)
button_4.grid(row = 2, column = 1)

button_5 = Button(root, text="5", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(5), height = 1, width = 5)
button_5.grid(row = 2, column = 2)

button_6 = Button(root, text="6", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(6), height = 1, width = 5)
button_6.grid(row = 2, column = 3)

button_7 = Button(root, text="7", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(7), height = 1, width = 5)
button_7.grid(row = 3, column = 1)

button_8 = Button(root, text="8", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(8), height = 1, width = 5)
button_8.grid(row = 3, column = 2)

button_9 = Button(root, text="9", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(9), height = 1, width = 5)
button_9.grid(row = 3, column = 3)

button_0 = Button(root, text="0", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press(0), height = 1, width = 5)
button_0.grid(row = 4, column = 2)

button_equals = Button(root, text="=", fg = "maroon4", bg = "CadetBlue1", command= lambda: total(), height = 1, width = 5)
button_equals.grid(row = 5, column = 4)

button_plus = Button(root, text="+", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press("+"), height = 1, width = 5)
button_plus.grid(row = 3, column = 4)

button_minus = Button(root, text="-", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press("-"), height = 1, width = 5)
button_minus.grid(row = 2, column = 4)

button_multiply = Button(root, text="*", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press("*"), height = 1, width = 5)
button_multiply.grid(row = 1, column = 4)

button_divide = Button(root, text="/", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press("/"), height = 1, width = 5)
button_divide.grid(row = 4, column = 4)

button_decimal = Button(root, text=".", fg = "maroon4", bg = "CadetBlue1", command= lambda: key_press("."), height = 1, width = 5)
button_decimal.grid(row = 4, column = 1)

button_clear = Button(root, text="C", fg = "maroon4", bg = "CadetBlue1", command= clear, height = 1, width = 5)
button_clear.grid(row = 4, column = 3)

root.mainloop()

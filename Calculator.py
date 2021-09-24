# import
from tkinter import *

# create window
root = Tk()

def addition():
    # e1.get() retrieves text from e1 box
    n1 = int(e1.get())
    # e2.get() retrieves text from e2 box
    n2 = int(e2.get())
    add = n1 + n2
    # adjusts label text
    label1.config(text="Answer: {}".format(add))

def subtraction():
    n1 = int(e1.get())
    n2 = int(e2.get())
    subtract = n1 - n2
    label1.config(text="Answer: {}".format(subtract))

def multiplication():
    n1 = int(e1.get())
    n2 = int(e2.get())
    multiply = n1 * n2
    label1.config(text="Answer: {}".format(multiply))

def division():
    n1 = int(e1.get())
    n2 = int(e2.get())
    divide = n1 / n2
    label1.config(text="Answer: {}".format(divide))

def power():
    n1 = int(e1.get())
    n2 = int(e2.get())
    raise_to = n1 ** n2
    label1.config(text="Answer: {}".format(raise_to))

def roots():
    n1 = int(e1.get())
    n2 = int(e2.get())
    root_of = n1 ** (1 / n2)
    label1.config(text="Answer: {}".format(root_of))

def modulo():
    n1 = int(e1.get())
    n2 = int(e2.get())
    mod = n1 % n2
    label1.config(text="Answer: {}".format(mod))


# starting window size
root.geometry("350x400")

# bg color window
#root.configure(background='gray')

# button bg color
bgc='gray'

# foreground (text) color
fgc = 'black'

# font size
fnt = 15



# create entry box
e1 = Entry(root,font="Helvetica %s bold"%(fnt))
e2 = Entry(root,font="Helvetica %s bold"%(fnt))

# create button and connect it to function
button1 = Button(root, command=addition, text="Add",font="Helvetica %s bold"%(fnt),fg=fgc)
button2 = Button(root, command=subtraction, text="Subtract",font="Helvetica %s bold"%(fnt),fg=fgc)
button3 = Button(root, command=multiplication, text="Multiply",font="Helvetica %s bold"%(fnt),fg=fgc)
button4 = Button(root, command=division, text="Divide",font="Helvetica %s bold"%(fnt),fg=fgc)
button5 = Button(root, command=power, text="Exponentiate",font="Helvetica %s bold"%(fnt),fg=fgc)
button6 = Button(root, command=roots, text="Root",font="Helvetica %s bold"%(fnt),fg=fgc)
button7 = Button(root, command=modulo, text="Mod",font="Helvetica %s bold"%(fnt),fg=fgc)


# create label
label1 = Label(root,text="Answer: ",font="Helvetica 20 bold",fg="black")


# location of box (default is TOP)
e1.pack()
e2.pack()

# location of button (default is TOP)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()

# sets location of label (default is LEFT)
label1.pack()

# keeps program running
root.mainloop()

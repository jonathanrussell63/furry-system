from tkinter import *


root = Tk()


def myClick():
	myLabel = Label(root, text = 'Look! I clicked a button!', fg= 'green')
	myLabel.pack()


myButton= Button(root, text = 'Click Me!', padx=50, pady=10, command = myClick).pack() #, fg= 'blue', bg='#000000') #, state=DISABLED makes the button unclickable


root.mainloop()
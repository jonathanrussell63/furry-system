from tkinter import *

#create root widget that everything goes in
root = Tk()
#create a Label widget
my_label1 = Label(root, text = 'Hello World').grid(row =0, column = 0)
my_label2 = Label(root, text = 'my name is Jonathan Russell').grid(row = 1, column = 5)
my_label3 = Label(root, text = ' 								').grid(row = 0 , column = 2)

#label.pack() shoves everything onto screen
#very unsophisticated method to put things on the screen

#using grid you can assign located to it
my_label1.grid(row =0, column = 0)
my_label2.grid(row = 1, column = 5)
my_label3.grid(row = 0 , column = 2)
# you can do it in one step with my_label1.grid(row =0, column = 0)

root.mainloop()
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Framed!')
root.iconbitmap('images/kami wa shinda.ico')

frame = LabelFrame(root, text = 'This is my Frame...', padx=5, pady=5)
frame.pack(padx=100, pady=100)

b = Button(frame, text = "Don't Click",command = root.quit)
b.grid(row=0, column=0)

root.mainloop()
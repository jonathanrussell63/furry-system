from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image!')
root.iconbitmap('kami wa shinda.ico')

my_img = ImageTk.PhotoImage(Image.open('/images/animegirl.jpg'))
my_label = Label(image = my_img, text = 'Hello!')
my_label.pack()













button_quit = Button(root, text = 'Exit Program', command = root.quit)
button_quit.pack()


root.mainloop()
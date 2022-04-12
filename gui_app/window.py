from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()

canvas_height = 100
canvas_width = 300

button_height = 25
button_width = 100

root = Tk()

canvas = Canvas(root, height=canvas_height, width=canvas_width)
canvas.pack()

button = Button(canvas, text='Open', command=open_file)
button.place(x=(canvas_width-button_width)/2,
             y=(canvas_height-button_height)/2,
             height=25,
             width=100)
root.mainloop()
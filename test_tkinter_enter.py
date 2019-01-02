import tkinter
from tkinter.ttk import Combobox
import tkinter.messagebox
import numpy as np

top = tkinter.Tk()
message = []

def callback(sq: int):
	tkinter.messagebox.showinfo( "Hello Python", "%d" % sq)
	message[sq].set('Pressed')

top.title("RUN ON START TEST")
top.grid_rowconfigure(1,weight=1)
top.grid_columnconfigure(1,weight=1)

frame = tkinter.Frame(top)
frame.pack(fill=tkinter.X, padx=5, pady=5)

for y in range(0,11):
	message.append(tkinter.StringVar())
	message[y].set('Not pressed.')
	b = tkinter.Button(frame, textvariable=message[y],   command=lambda y=y: callback(y))
	b.grid(row=0,column=y)

top.mainloop()

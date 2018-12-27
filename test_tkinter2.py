import tkinter
import tkinter.messagebox
import numpy as np

top = tkinter.Tk()

#def helloCallBack(sq: int):
def callback(sq: int):
   tkinter.messagebox.showinfo( "Hello Python", "%d" % sq)

top.title("RUN ON START TEST")
top.grid_rowconfigure(1,weight=1)
top.grid_columnconfigure(1,weight=1)

frame = tkinter.Frame(top)
frame.pack(fill=tkinter.X, padx=5, pady=5)

#tkinter.Button(frame, text="one",   command=lambda: callback(1)).pack()
#tkinter.Button(frame, text="two",   command=lambda: callback(2)).pack()
#tkinter.Button(frame, text="three", command=lambda: callback(3)).pack()

b = tkinter.Button(frame, text="one",   command=lambda: callback(1))
b.grid(row=0,column=0)
b = tkinter.Button(frame, text="two",   command=lambda: callback(2))
b.grid(row=0,column=1)
b = tkinter.Button(frame, text="three", command=lambda: callback(3))
b.grid(row=0,column=2)

top.mainloop()

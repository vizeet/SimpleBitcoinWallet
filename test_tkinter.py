import tkinter
import tkinter.messagebox

top = tkinter.Tk()

def callback(sq: int):
   tkinter.messagebox.showinfo( "Hello", "%d" % sq)

top.title("RUN ON START TEST")

frame = tkinter.Frame(top)
frame.pack()

for y in range(0,11):
        b = tkinter.Button(frame, text='%d' % y,   command=lambda y=y: callback(y))
        b.grid(row=0,column=y)

top.mainloop()

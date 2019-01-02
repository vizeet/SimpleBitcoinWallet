import sys
import tkinter

message1 = []
entries = []

def on_button(y, entry, toplevel):
        print("%d: %s" % (y, entry.get()))
        entries[y] = entry.get()
        message1[y].set('%d:correct' % y)
        toplevel.destroy()

def callback2():
	print('entries = %s' % entries)

def callback(y: int):
    toplevel = tkinter.Toplevel()
    message = tkinter.StringVar()
    entry = tkinter.Entry(toplevel, textvariable=message, width=10)
    button = tkinter.Button(toplevel, text="Get", command=lambda y=y, entry=entry, toplevel=toplevel: on_button(y, entry, toplevel))
    entry.pack()
    button.pack()

top = tkinter.Tk()

top.title("RUN ON START TEST")

frame = tkinter.Frame(top)
frame.pack()

for y in range(0,2):
        entries.append('')
        message1.append(tkinter.StringVar())
        message1[y].set('%d:unset' % y)
        b = tkinter.Button(frame, textvariable=message1[y],   command=lambda y=y: callback(y))
        b.grid(row=0,column=y)
get = tkinter.Button(top, text="Get", command=callback2)
get.pack()

top.mainloop()

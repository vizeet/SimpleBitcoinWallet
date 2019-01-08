import tkinter

root = tkinter.Tk()
root.attributes("-fullscreen", True)
T = tkinter.Text(root, height=2, width=30)
T.pack()
T.insert(tkinter.END, "Just a text Widget\nin two lines\n")
root.mainloop()

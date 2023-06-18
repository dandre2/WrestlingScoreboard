import tkinter
from tkinter import ttk


root = tkinter.Tk()


label = ttk.Label(root, text=1)
label.pack()
period = ttk.Label(root, text = 1)
period.pack()


def change_text():
    if label['text'] ==1:
        label['text'] = 2
    else:
        label['text'] = 1


def nextPeriod():
    period['text']+=1

button = ttk.Button(root, text="Click here", command=change_text)
button.pack()
button = ttk.Button(root, text="Next Period", command= nextPeriod)
button.pack()
root.mainloop()
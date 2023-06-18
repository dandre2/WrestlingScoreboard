import tkinter
from tkinter import ttk


root = tkinter.Tk()

label = ttk.Label(root, text='Hello')
label.pack()


def change_text():
    if label['text'] == 'Hello':
        label['text'] = 'World'
    else:
        label['text'] = 'Hello'


button = ttk.Button(root, text="Click here", command=change_text)
button.pack()
root.mainloop()
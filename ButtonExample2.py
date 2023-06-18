import tkinter
from tkinter import ttk


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text=1)
label.pack()
period = ttk.Label(big_frame, text = 1)
period.pack()


def change_text():
    if label['text'] ==1:
        label['text'] = 2
    else:
        label['text'] = 1


def nextPeriod():
    period['text']+=1

button = ttk.Button(big_frame, text="Click here", command=change_text)
button.pack()
button = ttk.Button(big_frame, text="Next Period", command= nextPeriod)
button.pack()
root.mainloop()
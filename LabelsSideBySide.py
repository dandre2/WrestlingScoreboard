from tkinter import *

win = Tk()
win.title("Labels in One Line")
win.geometry("700x350")

label1=Label(win, text="Label 1", font=("Times",30,"bold"), bg='red')
label1.pack(side=LEFT, pady=15)

label2=Label(win, text="Label 2", font=("Times",30,"bold"), bg='blue')
label2.pack(side=LEFT, pady=15)

# label3=Label(win, text="Label 3", font=("Times",30,"bold"), bg='green')
# label3.pack(side=LEFT, pady=15)

win.mainloop()


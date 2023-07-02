from tkinter import *
import tkinter as tk

root = Tk()
root.title("Labels in Two Lines")
root.geometry("400x400")

greenLabel = tk.Label(root, text="Green Score")
greenLabel.grid(column = 0, row = 0)
greenScore = tk.Label(root, text=0)
greenScore.grid(column = 1, row = 0)
redLabel = tk.Label(root, text="Red Score")
redLabel.grid(column = 0, row = 1)
redScore = tk.Label(root, text=0)
redScore.grid(column = 1, row = 1)

root.mainloop()
# label1.grid(column=0, row=0)
# label2.grid(column=1, row=0)
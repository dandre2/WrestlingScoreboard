import time
from tkinter import *
tk=Tk()
for x in range(1,91):
    print(x)
    time.sleep(1)
while True:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
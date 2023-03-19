wr1 = 0
wr2 = 0
roundnum = 0

def quarters():
    print('round number:')
    print(roundnum+1)
    print('red score:')
    print(wr1)
    print('Green score:')
    print(wr2)
    print('--------------')
    return[roundnum]
def greenpoints():
    print('red score:')
    print(wr1)
    print('green score:')
    print(wr2+2)
    print('round number:')
    print(roundnum)
    print('-----------')
    return [wr2]

def redpoints():
    print('red score:')
    print(wr1+2)     
    print('green score:')
    print(wr2)
    print('round number:')
    print(roundnum)
    print('----------------')
    return [wr1]

def minus_quarters():
    if roundnum==0:
        roundnum=1
        roundnum=roundnum-1
        print('round number:')
    print(roundnum-1)
    print('red score:')
    print(wr1)
    print('Green score:')
    print(wr2)
    print('--------------')
    return[roundnum]
    
def minus_greenpoints():
    if wr2==0:
        wr2=wr2+2
    else:
        print('red score:')
        print(wr1)
        print('green score:')
        print(wr2-2)
        print('round number:')
        print(roundnum)
        print('-----------')
        return [wr2]

def minus_redpoints():
    if wr1==0:
        wr1=wr1+1
    else:    
        print('red score:')
        print(wr1-2)     
        print('green score:')
        print(wr2)
        print('round number:')
        print(roundnum)
        print('----------------')
        return [wr1]

import time
from tkinter import *

tk=Tk()
btn=Button(tk,text='2 points red', command=redpoints)
btn.pack()
btn=Button(tk,text='2 points green', command=greenpoints)
btn.pack()
btn=Button(tk,text='Period', command=quarters)
btn.pack()

while True:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
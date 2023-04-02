wr1 = 0
wr2 = 0
roundnum = 0

def quarters(roundnum):
    print('round number:')
    roundnum+=1
    print(roundnum)
    print('red score:')
    print(wr1)
    print('Green score:')
    print(wr2)
    print('--------------')
    return roundnum

def greenpoints(wr2):
    print('red score:')
    print(wr1)
    print('green score:')
    print(wr2+2)
    print('round number:')
    print(roundnum)
    print('-----------')
    return [wr2]

def redpoints(wr1):
    print('red score:')
    print(wr1+2)     
    print('green score:')
    print(wr2)
    print('round number:')
    print(roundnum)
    print('----------------')
    return [wr1]

def minus_quarters(roundnum):
    if roundnum==0:
        roundnum=1
        print('round number:')
        print(roundnum-1)
        print('red score:')
        print(wr1)
        print('Green score:')
        print(wr2)
        print('--------------')
        return[roundnum]
    
def minus_greenpoints(wr2):
    if wr2==0:
        wr2=2    
        print('red score:')
        print(wr1)
        print('green score:')
        print(wr2-2)
        print('round number:')
        print(roundnum)
        print('-----------')
        return [wr2]

def minus_redpoints(wr1):
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
btn=Button(tk,text='2 points red', command=redpoints(wr1))
btn.pack()
btn=Button(tk,text='2 points green', command=greenpoints(wr2))
btn.pack()
btn=Button(tk,text='Period', command=quarters(roundnum))
btn.pack()
btn=Button(tk,text='minus 2 points red', command=minus_redpoints(wr1))
btn.pack()
btn=Button(tk,text='minus 2 points green', command=minus_greenpoints(wr2))
btn.pack()
btn=Button(tk,text='minus 1 period', command=minus_quarters(roundnum))
btn.pack()

while True:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
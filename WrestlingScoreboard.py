import tkinter
import time
    # Pausing time
    # starting time again in a new period
    # adding logic to stop time if theres a winner


def nextPeriod():
        overtime1()
        period['text'] += 1

def redScoreTwo():
        redscore['text'] += 2
        redScoreCheck()

def greenScoreTwo():
        greenscore['text'] += 2
        greenScoreCheck()

def redScoreOne():
        redscore['text'] += 1
        redScoreCheck()

def greenScoreOne():
        greenscore['text'] += 1
        greenScoreCheck()


def redScoreThree():
        redscore['text'] += 3
        redScoreCheck()

def RedOt1win():
        resultLabel['text']='red wins ot1'

def GreenScoreThree():
        greenscore['text'] += 3
        greenScoreCheck()

def RedPenalty():
       Rp['text']+=1
       redPenaltyCheck1()
def GreenPenalty():
       Gp['text']+=1
       GreenPenaltyCheck1()
def pinred():
        resultLabel['text']='red wins by pin'

def pingreen():
        resultLabel['text']='green wins by pin'    
        
def overtime1():
        if period['text']==3:
            overtimeLabel['text']='first overtime, first takedown wins.'    

def greenScoreCheck():
        if greenscore['text']>=15:
            resultLabel['text']='green wins by techfall'

def redScoreCheck():
        if redscore['text']>=15:
            resultLabel['text']='red wins by techfall'
def redPenaltyCheck1():       
        if Rp['text']>=3:
               redscore+=1
               
               redPenaltyCheck2()
               redPenaltyCheck3()
               redPenaltyCheck4()
def redPenaltyCheck2():       
        if Rp['text']>=4:
               greenscore+=2
def redPenaltyCheck3():       
        if Rp['text']>=5:
               greenscore+=3
def redPenaltyCheck4():       
        if Rp['text']>=6:
                resultLabel['text']='green wins by disqualification'
def GreenPenaltyCheck1():       
        if Gp['text']>=3:
               greenscore+=1
       
        GreenPenaltyCheck2()
        GreenPenaltyCheck3()
        GreenPenaltyCheck4()       
def GreenPenaltyCheck2():       
        if Rp['text']>=4:
               greenscore+=2
def GreenPenaltyCheck3():       
        if Rp['text']>=5:
               greenscore+=3
def GreenPenaltyCheck4():       
        if Rp['text']>=6:
                resultLabel['text']='green wins by disqualification'                                                             
scores = ['0', '1', '2', '3', '4',
            '5', '-5', '-4', '-3', '-2', '-1']


timeleft = 90


def startGame(event):
        if timeleft == 90:
            #countdown()

            nextColour()
            # App(tkinter.Tk)

def nextColour():
        global redscore
        global greenscore
        global timeleft

        if timeleft > 0:
            pass


            

root = tkinter.Tk()

root.title("Wrestling Scoreboard")

root.geometry("500x800")


greenLabel = tkinter.Label(root, text="Green Score")
greenLabel.pack()
greenscore = tkinter.Label(root, text=0)
greenscore.pack()

redLabel = tkinter.Label(root, text="Red Score")
redLabel.pack()
redscore = tkinter.Label(root, text=0)
redscore.pack()
print("redscore label" , redscore['text'])
print("redscore label" , redscore['text']+1)
redscore['text']+=1
print("redscore label" , redscore['text'])
periodLabel = tkinter.Label(root, text="Period")
periodLabel.pack()
period = tkinter.Label(root, text=1)
period.pack()

RedPenalties = tkinter.Label(root, text="red penalty")
RedPenalties.pack()
Rp = tkinter.Label(root, text=0)  
Rp.pack()


GreenPenalties = tkinter.Label(root, text="green penalty")
GreenPenalties.pack()
Gp = tkinter.Label(root, text=0)  
Gp.pack()

def start_stop():
        #button = tkinter.Button(root, text='Start', width=50, command=start_stop())
        #button.pack()
        global active_counter
        if button['text'] == 'Start':
                active_counter = True
                count()
                button.config(text="Stop")
        else:
                active_counter = False
                button.config(text="Start")

def count():
            global counter
            if active_counter:
                counter -= 1
                label.config(text='time')
                label.config(text=counter)
                label.after(1000, count)

print("Counting Seconds")
global counter
global active_counter
counter = 90
active_counter = False
label = tkinter.Label(root, fg="black")
label.pack()
button = tkinter.Button(root, text='Start', width=50, command=start_stop)
button.pack()



resultLabel = tkinter.Label(root, text="empty")
resultLabel.pack()
overtimeLabel = tkinter.Label(root, text="no overtime")
overtimeLabel.pack()

GreenTwoPointsButton = tkinter.Button(root, text="Two points green", command=greenScoreTwo)
GreenTwoPointsButton.pack()

RedTwoPointsButton = tkinter.Button(root, text="Two points red", command=redScoreTwo)
RedTwoPointsButton.pack()

GreenOnePointButton = tkinter.Button(root, text="One point green", command=greenScoreOne)
GreenOnePointButton.pack()

redOnePointsButton = tkinter.Button(root, text="One point red", command=redScoreOne)
redOnePointsButton.pack()

greenThreePointsButton = tkinter.Button(root, text="three points green", command=GreenScoreThree)
greenThreePointsButton.pack()

redThreePointsButton = tkinter.Button(root, text="three points red", command=redScoreThree)
redThreePointsButton.pack()

redpinButton = tkinter.Button(root, text="red pin", command=pinred)
redpinButton.pack()

greenpinButton = tkinter.Button(root, text="green pin", command=pingreen)
greenpinButton.pack()

RedWinsOvertime1= tkinter.Button(root, text="red wins Ot1", command=RedOt1win)
RedWinsOvertime1.pack()

RPbutton= tkinter.Button(root, text="red penalties", command=RedPenalty)
RPbutton.pack()

GPbutton= tkinter.Button(root, text="Green penalties", command=GreenPenalty)
GPbutton.pack()
    # StopClockbutton= tkinter.Button(root, text="to stop clock", command)
    # StopClockbutton.pack()

NextPeriodButton = tkinter.Button(root, text="Next Period", command=nextPeriod)
NextPeriodButton.pack()
if __name__ == "__main__":
        # root.bind(App().mainloop())
        root.bind('<Return>', startGame)
        root.mainloop()
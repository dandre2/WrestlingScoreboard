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


# class App(tkinter.Tk):
#         def __init__(self):
#             super().__init__()
#             self.title("Counting Seconds")
#             self.counter = 90
#             self.active_counter = False
#             self.label = tkinter.Label(self, fg="black")
#             self.label.pack()
#             self.button = tkinter.Button(self, text='Start', width=50, command=self.start_stop)
#             self.button.pack()

        def count(self):
            if self.active_counter:
                self.counter -= 1
                self.label.config(text=self.counter)
                self.label.after(1000, self.count)

        def start_stop(self):
            if self.button['text'] == 'Start':
                self.active_counter = True
                self.count()
                self.button.config(text="Stop")
            else:
                self.active_counter = False
                self.button.config(text="Start")


            

root = tkinter.Tk()

root.title("COLORGAME")

root.geometry("500x800")


greenLabel = tkinter.Label(root, text="Green Score")
greenLabel.pack()
greenscore = tkinter.Label(root, text=0)
greenscore.pack()

redLabel = tkinter.Label(root, text="Red Score")
redLabel.pack()
redscore = tkinter.Label(root, text=0)
redscore.pack()

periodLabel = tkinter.Label(root, text="Period")
periodLabel.pack()
period = tkinter.Label(root, text=1)
period.pack()

    



def start_stop(self):
            if button['text'] == 'Start':
                active_counter = True
                count()
                button.config(text="Stop")
            else:
                active_counter = False
                button.config(text="Start")

print("Counting Seconds")

counter = 90
active_counter = False
label = tkinter.Label(root, fg="black")
label.pack()
button = tkinter.Button(root, text='Start', width=50, command=start_stop)
button.pack()

def count(self):
    if active_counter:
        counter -= 1
        label.config(text=counter)
        label.after(1000,count)

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



    # StopClockbutton= tkinter.Button(root, text="to stop clock", command)
    # StopClockbutton.pack()

NextPeriodButton = tkinter.Button(root, text="Next Period", command=nextPeriod)
NextPeriodButton.pack()
if __name__ == "__main__":
        # root.bind(App().mainloop())
        root.bind('<Return>', startGame)
        root.mainloop()
        
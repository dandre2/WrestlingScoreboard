import tkinter


def nextPeriod():
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


def GreenScoreThree():
    greenscore['text'] += 3
    greenScoreCheck()

def pinred():
    resultLabel['text']='red wins by pin'

def pingreen():
    resultLabel['text']='green wins by pin'    

def greenScoreCheck():
    if greenscore['text']>=15:
        resultLabel['text']='green wins by techfall'

def redScoreCheck():
    if redscore['text']>=15:
        resultLabel['text']='red wins by techfall'

scores = ['0', '1', '2', '3', '4',
          '5', '-5', '-4', '-3', '-2', '-1']
time = ['1', '2', '3', '4', '5', '6']

timeleft = 90


def startGame(event):
    if timeleft == 90:
        countdown()

    nextColour()


def nextColour():
    global redscore
    global greenscore
    global timeleft

    if timeleft > 0:
        pass


def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left: "
                              + str(timeleft))

        timeLabel.after(1000, countdown)


root = tkinter.Tk()

root.title("COLORGAME")

root.geometry("500x800")

instructions = tkinter.Label(root, text="press enter to start timer",
                             font=('Helvetica', 32))
instructions.pack()

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

timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

resultLabel = tkinter.Label(root, text="empty")
resultLabel.pack()

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

NextPeriodButton = tkinter.Button(root, text="Next Period", command=nextPeriod)
NextPeriodButton.pack()

root.bind('<Return>', startGame)
root.mainloop()

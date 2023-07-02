import tkinter
import random


def nextPeriod():
    period['text']+=1

def redScoreTwo():
    redscore['text']+=2  

def greenScoreTwo():
    greenscore['text']+=2

def redScoreOne():
    redscore['text']+=1

def greenScoreOne():
    greenscore['text']+=1

def redScoreThree():
    redscore['text']+=3            

def GreenScoreThree():
    greenscore['text']+=3 

def pinred():
    print('red wins')
    print('green loses')

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


greenscore = tkinter.Label(root, text=0)
greenscore.pack()

redscore = tkinter.Label(root,text= 0)
redscore.pack()



period = tkinter.Label(root, text =1)
period.pack()


timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeleft), font=('Helvetica', 12))

timeLabel.pack()


label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()







GreenTwoPointsButton = tkinter.Button(root, text="Two points green", command= greenScoreTwo)
GreenTwoPointsButton.pack()





RedTwoPointsButton = tkinter.Button(root, text="Two points red", command= redScoreTwo)
RedTwoPointsButton.pack()






GreenOnePointButton = tkinter.Button(root, text="One point green", command= greenScoreOne)
GreenOnePointButton.pack()







redOnePointsButton = tkinter.Button(root, text="One point red", command= redScoreOne)
redOnePointsButton.pack()










greenThreePointsButton = tkinter.Button(root, text="three points green", command= GreenScoreThree)
greenThreePointsButton.pack



redThreePointsButton = tkinter.Button(root, text="three points red", command= redScoreThree)
redThreePointsButton.pack



redpinButton = tkinter.Button()


NextPeriodButton = tkinter.Button(root, text="Next Period", command= nextPeriod)
NextPeriodButton.pack()









root.bind('<Return>', startGame)
root.mainloop()
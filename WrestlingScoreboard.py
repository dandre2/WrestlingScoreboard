import tkinter
import random


scores = ['0', '1', '2', '3', '4',
          '5', '-5', '-4', '-3', '-2', '-1']
time = ['1', '2', '3', '4', '5', '6']
greenscore = 0
redscore = 0
period=0

timeleft = 90


def startGame(event):

    if timeleft == 90:

        countdown()

    nextColour()


def nextColour():

    global redscore
    global greenscore
    global timeleft
    global period

    
    if timeleft > 0:
        
        e.focus_set()
        x.focus_set()
        p.focus_set()

        if e.get().lower() == scores[1]:

            greenscore += 1
        if e.get().lower() == scores[2]:
            greenscore += 2
        if e.get().lower() == scores[3]:
            greenscore += 3
        if e.get().lower() == scores[4]:
            greenscore += 4
        if e.get().lower() == scores[5]:
            greenscore += 5
        if e.get().lower() == scores[-1]:
            greenscore -= 1
        if e.get().lower() == scores[-2]:
            greenscore -= 2
        if e.get().lower() == scores[-3]:
            greenscore -= 3
        if e.get().lower() == scores[-4]:
            greenscore -= 4
        if e.get().lower() == scores[-5]:
            greenscore -= 5
        if x.get().lower() == scores[1]:

            redscore += 1
        if x.get().lower() == scores[2]:
            redscore += 2
        if x.get().lower() == scores[3]:
            redscore += 3
        if x.get().lower() == scores[4]:
            redscore += 4
        if x.get().lower() == scores[5]:
             redscore += 5
        if x.get().lower() == scores[-1]:
             redscore -= 1
        if x.get().lower() == scores[-2]:
             redscore -= 2
        if x.get().lower() == scores[-3]:
             redscore -= 3
        if x.get().lower() == scores[-4]:
             redscore -= 4
        if x.get().lower() == scores[-5]:
             redscore -= 5    
        if p.get().lower() == scores[1]:
             period +=1
        if s.get().lower() == scores[1]:
             timeleft +=1
        if s.get().lower() == scores[2]:
             timeleft +=2
        if s.get().lower() == scores [3]:
             timeleft +=3                 
        if s.get().lower() == scores [4]:
             timeleft +=4
        if s.get().lower() == scores[5]:
             timeleft +=5
        if s.get().lower() == scores[6]:
             timeleft +=6               
        e.delete(0, tkinter.END)
        x.delete(0, tkinter.END)
        p.delete(0, tkinter.END)
        s.delete(0, tkinter.END)

        greenscoreLabel.config(text="Green Score: " + str(greenscore))

        redscoreLabel.config(text="Red Score: " + str(redscore) + "Period:" + str(period))


# Countdown timer function


def countdown():

    global timeleft

    # if a game is in play
    if timeleft > 0:

        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text="Time left: "
                         + str(timeleft))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)


# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("COLORGAME")

# set the size
root.geometry("500x800")

# add an instructions label
instructions = tkinter.Label(root, text="Type in the red and green wrestlers score at inputs",
                             font=('Helvetica', 12))
instructions.pack()

# add a score label
greenscoreLabel = tkinter.Label(root, text="Press enter to start",
                                font=('Helvetica', 12))
greenscoreLabel.pack()

redscoreLabel = tkinter.Label(root, text=(period),
                              font=('Helvetica', 12))
redscoreLabel.pack()


# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
v = tkinter.StringVar(root, value='Green score')
d= tkinter.StringVar(root, value='red score')
a= tkinter.StringVar(root, value='period')
t= tkinter.StringVar(root, value='timeleft')
e = tkinter.Entry(root, textvariable= v)
x = tkinter.Entry(root, textvariable=d)
p = tkinter.Entry(root, textvariable=a)
s = tkinter.Entry(root, textvariable=t)
# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
x.pack()
p.pack()
s.pack()
someLabel = tkinter.Label(root, text="SomeLabel",
                              font=('Helvetica', 12))
someLabel.pack()
# set focus on the entry box
x.focus_set()
e.focus_set()
p.focus_set()
s.focus_set()
root.mainloop()

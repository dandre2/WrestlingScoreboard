import tkinter
import random


scores = ['0', '1', '2', '3', '4',
          '5', '-5', '-4', '-3', '-2', '-1']
greenscore = 0
redscore = 0

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

        e.focus_set()
        x.focus_set()

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
        e.delete(0, tkinter.END)
        x.delete(0, tkinter.END)

        greenscoreLabel.config(text="green Score: " + str(greenscore))

        redscoreLabel.config(text="redscore: " + str(redscore))

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

redscoreLabel = tkinter.Label(root, text="Press enter to start",
                              font=('Helvetica', 12))
redscoreLabel.pack()

scoreinstructions = tkinter.Label(root, text="Green score is on the top\nred score is on bottom")
scoreinstructions.pack()
# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeleft), font=('Helvetica', 12))

timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)
x = tkinter.Entry(root)
# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
x.pack()
# set focus on the entry box
x.focus_set()
e.focus_set()
root.mainloop()

# Author: reDragonCoder

# Libraries
import tkinter
from tkinter import messagebox
import random

# Colours
colours=['Red', 'Blue', 'Green', 'Pink', 'Black',
         'Yellow', 'Orange', 'White', 'Purple', 'Brown']

# Global variables
score=0
timeleft=30

# Functions
def startGame(event):
    global score
    global timeleft

    if timeleft==30:
        countdown()
        nextColour()
    elif timeleft==0:
        score=0
        timeleft=30
        instructions.config(text="Type in the colour of the word, and not the word text!", font=('Helvetica', 12))
        scoreLabel.config(text="Score: "+str(score))
        timeLabel.config(text="Time left: "+str(timeleft))
        e.config(state=tkinter.NORMAL)
        e.focus_set()
        countdown()
        nextColour()
    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score+=1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: "+str(score))

def countdown():
    global timeleft
    
    if timeleft>0:
        timeleft-=1
        timeLabel.config(text="Time left: "+str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        messagebox.showinfo("Game Status", "Game Over")
        instructions.config(text="Good game! Your score was "+str(score)+". Press 'q' to play again", font=('Helvetica', 12))
        e.config(state=tkinter.DISABLED)

# Driver code
root=tkinter.Tk()
root.title("COLOR GAME")
window_width=400
window_height=300
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
position_x=(screen_width//2)-(window_width//2)
position_y=(screen_height//2)-(window_height//2)
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

instructions=tkinter.Label(root, text="Type in the colour of the word, and not the word text!", font=('Helvetica', 12))
instructions.pack()

scoreLabel=tkinter.Label(root, text="Press 'q' to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel=tkinter.Label(root, text="Time left: "+str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label=tkinter.Label(root, font=('Helvetica', 60))
label.pack();

e=tkinter.Entry(root)

root.bind('<Return>', lambda event: nextColour())
root.bind('<Key-q>', startGame)
e.pack()

e.focus_set()

root.mainloop()
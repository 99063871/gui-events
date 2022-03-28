import tkinter
import random
import time
from turtle import pos

window = tkinter.Tk()
window.geometry("440x300")
window.configure(bg="gray")
window.title("Simple FPS trainer")
label = tkinter.Label()
label.config(bg="gray")
label.pack()
list = ["Press: W", "Press: A", "Press: S","Press: D", "Press: Space", "Single click", "Double click", "Triple click"]
score = 0
counter = 0
scoreCount = 0
timerSecs = 0

def timer():
    global timerSecs
    timerSecs+=1
    label.config(text="Time remaining: "+str(timerSecs))
    if timerSecs == 20:
        button.pack_forget()
        button.after(1000, button.destroy())
        print("Je hebt", scoreCount, "punten gehaalt")
    else:
        label.after(1000, timer)

def functiona(e):
    global scoreCount
    global vara
    global varthing
    global score
    global events
    events = "nope"
    score+=1
    print(score)
    window.unbind(varthing)
    button.unbind(varthing)
    vara = random.choice(list)
    button.config(text=vara)
    button.place(x=random.randint(0,390), y=random.randint(0, 250))
    
    if vara == "Press: W":
        varthing = '<w>'
    elif vara == "Press: A":
        varthing = '<a>'
    elif vara == "Press: S":
        varthing = '<s>'
    elif vara == "Press: D":
        varthing = '<d>'
    elif vara == "Press: Space":
        varthing = '<space>'
    elif vara == "Single click":
        varthing = '<Button-1>'
        events = "click"
    elif vara == "Double click":
        varthing = '<Double-Button-1>'
        events = "click"
    elif vara == "Triple click":
        varthing = '<Triple-Button-1>'
        events = "click"
    
    if events == "click":
        button.bind(varthing, functiona)
        scoreCount+=1
    else:
        window.bind(varthing, functiona)
        scoreCount+=1
    if timerSecs == 0:
        timer()

vara = random.choice(list)
button = tkinter.Button(text="Click here to start", bg="White", borderwidth=0, height=2)
button.place(x=180, y=120)
varthing = '<Button-1>'
button.bind(varthing , functiona)
score-=1

window.mainloop()
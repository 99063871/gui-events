from distutils.cmd import Command
import tkinter
import random

window = tkinter.Tk()
window.geometry("440x300")
window.title("Simple FPS trainer")

list = ["Press: W", "Press: A", "Press: S","Press: D", "Press: Space", "Single click", "Double click", "Triple click"]

def functiona(e):    
    global vara
    global varthing
    window.unbind(varthing)
    button.unbind(varthing)
    vara = random.choice(list)
    button.config(text=vara)
    if vara == "Press: W":
        varthing = '<w>'
        print("activated")
    elif vara == "Press: A":
        varthing = '<a>'
        print("activated")
    elif vara == "Press: S":
        varthing = '<s>'
        print("activated")
    elif vara == "Press: D":
        varthing = '<d>'
        print("activated")
    elif vara == "Press: Space":
        varthing = '<space>'
        print("activated")
    elif vara == "Single click":
        varthing = '<Button-1>'
        button.bind(varthing, functiona)
        print("clicked")
    elif vara == "Double click":
        varthing = '<Double-Button-1>'
        button.bind(varthing, functiona)
        print("dblclicked")
    elif vara == "Triple click":
        varthing = '<Triple-Button-1>'
        button.bind(varthing, functiona)
        print("trplclicked")
    else:
        print("nope")
        functiona(varthing)
    window.bind(varthing, functiona)

vara = random.choice(list)
button = tkinter.Button(text="Click here to start", bg="White", borderwidth=0, height=2)
button.pack()
varthing = '<Button-1>'
window.bind(varthing , functiona)

window.mainloop()
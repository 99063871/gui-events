import tkinter
import random

window = tkinter.Tk()
window.geometry("440x300")
window.title("Simple FPS trainer")
list = ["Press: W", "Press: A", "Press: S","Press: D", "Press: Space", "Single click", "Double click", "Triple click"]
def functiona(e):
    global vara
    vara = random.choice(list)
    button.config(text=vara)
    print("activated")


button = tkinter.Button(text="Hi", bg="White", borderwidth=0, width=10, height=2)
button.pack()
functiona(list)
window.bind('<space>', functiona)

window.mainloop()
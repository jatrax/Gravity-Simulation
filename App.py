from tkinter import *
from Planets import Planet
import Config
import time

Planet(radius=6,mass=60,color = "#0000aa",coordinates=[100,600]  ,acceleration=[0,-440])
Planet(radius=5,color="#00aa00",coordinates=[300,600],acceleration=[0,550])
Planet(radius=50,mass=22000,color="orange" ,coordinates=[600,600])

app = Tk()
app.config(background="black")

panel = Canvas(app,width=Config.WIDTH,height=Config.HEIGHT,background="black")
panel.pack()

Planet.paint_all(panel)

def start():
    while True:
        time.sleep(.01/Config.Time)
        panel.delete('all')
        Planet.move_all()
        Planet.paint_all(panel)
        app.update_idletasks()

button = Button(text="START",command=start)
button.pack()

app.mainloop()
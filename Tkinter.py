from tkinter import *
from Planets import Planet
import Config
import time

Earth = Planet(radius=20,mass=60,color = "#0000aa",coordinates=[25,25]  ,acceleration=[2,2])
Mars  = Planet(radius=18,mass=45,color = "#aa0000",coordinates=[1000,50],acceleration=[-2,4])
Venus = Planet(radius=16,mass=60,color = "#00aa00",coordinates=[500,1000],acceleration=[-2,-1])


app = Tk()
app.config(background="black")

panel = Canvas(app,width=Config.WIDTH,height=Config.HEIGHT,background="black")
panel.pack()

Planet.paint_all(panel)

def start():
    while True:
        time.sleep(.001)
        panel.delete('all')
        Planet.move_all()
        Planet.paint_all(panel)
        app.update_idletasks()

button = Button(text="START",command=start)
button.pack()

app.mainloop()
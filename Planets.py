import math
import Config
class Planet:

    Planets = []
    def __init__(self,radius = 10,mass = 100,coordinates = [float(0),float(0)],
                 acceleration = [float(0),float(0)],color = 'white'):
        self.radius = radius
        self.mass = mass
        self.coordinates = [float(coordinates[0]),float(coordinates[1])]
        self.acceleration = [float(acceleration[0]),float(acceleration[1])]
        self.color = color
        Planet.Planets.append(self)

    def move(self):
        for planet in Planet.Planets:
            if planet != self:
                distance_x = self.coordinates[0]-planet.coordinates[0]
                distance_y = self.coordinates[1]-planet.coordinates[1]
                distance   = math.sqrt(distance_x*distance_x+distance_y*distance_y)
                if distance < self.radius + planet.radius:
                    distance = self.radius + planet.radius
                F = 6.67430 * math.pow(10,1) * self.mass * planet.mass # original (G = 6.67430 * 10^-11)
                F = F / (distance * distance) * Config.Gravity
                angle = math.atan2(distance_y, distance_x)
                self.acceleration[0] -= math.cos(angle) * F / self.mass
                self.acceleration[1] -= math.sin(angle) * F / self.mass
        for planet in Planet.Planets:
            for i in range(2):self.coordinates[i] += self.acceleration[i]/200
        
    @staticmethod
    def move_all():
        for planet in Planet.Planets:planet.move()

    def paint(self,panel):
        x0 = self.coordinates[0] - self.radius 
        x1 = self.coordinates[0] + self.radius
        y0 = self.coordinates[1] - self.radius
        y1 = self.coordinates[1] + self.radius
        panel.create_oval(x0,y0,x1,y1,fill = self.color)

    @staticmethod
    def paint_all(panel):
        for planet in Planet.Planets:
            planet.paint(panel)

    
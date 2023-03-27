
import math


# Write your pose class here:

class Pose():

    def __init__(self, x=0, y=0, angle=0):
        self.x=0
        self.y=0
        self.angle=0 # in degrees

    def changePosition(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def changeVelocity(self, angle, speed, time):
        self.angle+=angle
        self.x+=-math.sin(math.pi/180*angle)*speed*time
        self.y+=math.cos(math.pi/180*angle)*speed*time

    def __str__(self):
        return f"angle: {self.angle}, x: {self.x}, y: {self.y}"

if __name__=="__main__":
    pose=Pose(1,2)
    pose.changePosition(3,4)
    print(pose)
    # Should print (angle: 0, x: 3, y: 4)
    pose.changeVelocity(angle=30, speed=10, time=2)
    # Should print (angle: 30, x: -6.999999999999998, y: 21.320508075688775)
    print(pose)




# Write your pose class here:




if __name__=="__main__":
    pose=Pose(1,2)
    pose.changePosition(3,4)
    print(pose)
    # Should print (angle: 0, x: 3, y: 4)
    pose.changeVelocity(angle=30, speed=10, time=2)
    print(pose)
    # Should print (angle: 30, x: -6.999999999999998, y: 21.320508075688775)
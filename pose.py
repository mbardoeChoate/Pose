



# Write your pose class here:




if __name__=="__main__":
    pose=Pose(1,2)
    pose.changePosition(3,4)
    print(pose)
    # Should print (4,6)
    pose.changeVelocity(angle=30, time=2)
    # Should print ()
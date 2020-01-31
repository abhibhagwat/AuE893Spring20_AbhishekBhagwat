#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # #Receiveing the user's input
    # print("Let's move your robot")
    # speed = input("Input your speed:")
    # distance = input("Type your distance:")
    # isForward = input("Foward?: ")#True or False
    #
    # #Checking if the movement is forward or backwards
    # if(isForward):
    #     vel_msg.linear.x = abs(speed)
    # else:
    #     vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    current_goal = 1
    while(current_goal<5):
        distance = 2  #2*3.14*radius
        angle = (90*2*math.pi)/360
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        #radius = vel_msg.linear.x/vel_msg.angular.z


        #    while not rospy.is_shutdown():

        #Setting the current time for distance calculus

        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        current_angle = 0

        #Loop to move the turtle in an specified distance
        while(current_distance <= distance):
            #Publish the velocity
            vel_msg.linear.x = 0.2
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= vel_msg.linear.x*(t1-t0)
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0.2

        t2 = rospy.Time.now().to_sec()
        while(current_angle <= angle):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t3=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_angle= vel_msg.angular.z*(t3-t2)
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
            #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        current_goal = current_goal+1

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass

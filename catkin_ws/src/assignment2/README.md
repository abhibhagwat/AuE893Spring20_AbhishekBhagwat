1. circle.py
   Executing this python code will make the turtlebot trace a circle of given distance, linear velocity and angular velocity.
To launch this file, run the command roslaunch assignment2 turtlesim_circle.launch

2. square_openloop.py
    Executing this python code will make the turtlebot trace a square of given side length.
The code runs in a while loop as follows - 
First, it moves with a given linear velocity then, it turns 90 degrees with a given angular speed then stops. This is basically done by the formula angular speed = angle/time
The turtle further repeats this process three more times to trace a square.
To launch this file, run the command roslaunch assignment2 turtlesim_square.launch

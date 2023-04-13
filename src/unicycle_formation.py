#!/usr/bin/env python3

import rospy 
import math 
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from tf.transformations import euler_from_quaternion 
import numpy as  np 
import matplotlib.pyplot as plt
import ast





if __name__ == "__main__":


    rospy.init_node('turtlebot_controller_node')
    
    subscribe_to_odom = rospy.Subscriber('/tb3_1/odom', Odometry, callback = odomdata_callback)

    rospy.loginfo('My node has been started')
    publish_to_cmd_vel = rospy.Publisher('/tb3_1/cmd_vel', Twist, queue_size = 10)

    #create an object of pose data

    move_the_bot = Twist()
    odometry_turtle = Odometry()
    global point 
    global start 
    line = []
    count = 0
    first = True


    rospy.spin()


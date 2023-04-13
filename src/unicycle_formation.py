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


def odomdata_callback_bot1(msg):
    global current_angle
    global odometry_turtle_1; odometry_turtle_1 = msg 
    euler = euler_from_quaternion([odometry_turtle_1.pose.pose.orientation.x, odometry_turtle_1.pose.pose.orientation.y, odometry_turtle_1.pose.pose.orientation.z, odometry_turtle_1.pose.pose.orientation.w])
    current_angle[0] = euler[2]

    #k > 0: balanced configuration, k < 0: synchronised configuration 

    k=1

    heading = get_desired_delta_angle(current_angle[0], k)

    move_the_bot1.angular.z = heading
    move_the_bot1.linear.x = 0.0
    publish_to_cmd_vel1.publish(move_the_bot1)
    if (heading < 0.1 and heading > -0.1):
        move_the_bot1.linear.x = 0.07
        publish_to_cmd_vel1.publish(move_the_bot1)

def odomdata_callback_bot2(msg):
    global current_angle
    global odometry_turtle_2; odometry_turtle_2 = msg 
    euler = euler_from_quaternion([odometry_turtle_2.pose.pose.orientation.x, odometry_turtle_2.pose.pose.orientation.y, odometry_turtle_2.pose.pose.orientation.z, odometry_turtle_2.pose.pose.orientation.w])
    current_angle[1] = euler[2]
    
    #k > 0: balanced configuration, k < 0: synchronised configuration 

    k=1

    heading = get_desired_delta_angle(current_angle[1], k)

    move_the_bot2.angular.z = heading
    move_the_bot2.linear.x = 0.0
    publish_to_cmd_vel2.publish(move_the_bot2)
    if (heading < 0.1 and heading > -0.1):
        move_the_bot2.linear.x = 0.07
        publish_to_cmd_vel2.publish(move_the_bot2)

def odomdata_callback_bot3(msg):
    global current_angle
    global odometry_turtle_3; odometry_turtle_3 = msg 
    euler = euler_from_quaternion([odometry_turtle_3.pose.pose.orientation.x, odometry_turtle_3.pose.pose.orientation.y, odometry_turtle_3.pose.pose.orientation.z, odometry_turtle_3.pose.pose.orientation.w])
    current_angle[2] = euler[2]

    #k > 0: balanced configuration, k < 0: synchronised configuration 

    k=1

    heading = get_desired_delta_angle(current_angle[2], k)

    move_the_bot3.angular.z = heading
    move_the_bot3.linear.x = 0.0
    publish_to_cmd_vel3.publish(move_the_bot3)
    if (heading < 0.1 and heading > -0.1):
        move_the_bot3.linear.x = 0.07
        publish_to_cmd_vel3.publish(move_the_bot3)

def odomdata_callback_bot4(msg):
    global current_angle
    global odometry_turtle_4; odometry_turtle_4 = msg 
    euler = euler_from_quaternion([odometry_turtle_4.pose.pose.orientation.x, odometry_turtle_4.pose.pose.orientation.y, odometry_turtle_4.pose.pose.orientation.z, odometry_turtle_4.pose.pose.orientation.w])
    current_angle[3] = euler[2]

    #k > 0: balanced configuration, k < 0: synchronised configuration 

    k=1

    heading = get_desired_delta_angle(current_angle[3], k)

    move_the_bot4.angular.z = heading
    move_the_bot4.linear.x = 0.0
    publish_to_cmd_vel4.publish(move_the_bot4)
    if (heading < 0.1 and heading > -0.1):
        move_the_bot4.linear.x = 0.07
        publish_to_cmd_vel4.publish(move_the_bot4)



#k > 0: balanced configuration, k < 0: synchronised configuration 
def get_desired_delta_angle(bot_angle, k):
    global current_angle
    heading = 0
    for angle in current_angle: 
        #u(t)i = -k/n sum(sin(thetaj - thetai))
        heading = heading -k / len(current_angle)* math.sin(angle - bot_angle)

    return heading

    

if __name__ == "__main__":


    rospy.init_node('turtlebot_controller_node')
    
    subscribe_to_odom = rospy.Subscriber('/tb3_1/odom', Odometry, callback = odomdata_callback_bot1)
    subscribe_to_odom = rospy.Subscriber('/tb3_2/odom', Odometry, callback = odomdata_callback_bot2)
    subscribe_to_odom = rospy.Subscriber('/tb3_3/odom', Odometry, callback = odomdata_callback_bot3)
    subscribe_to_odom = rospy.Subscriber('/tb3_4/odom', Odometry, callback = odomdata_callback_bot4)

    rospy.loginfo('My node has been started')
    publish_to_cmd_vel1 = rospy.Publisher('/tb3_1/cmd_vel', Twist, queue_size = 10)
    publish_to_cmd_vel2 = rospy.Publisher('/tb3_2/cmd_vel', Twist, queue_size = 10)
    publish_to_cmd_vel3 = rospy.Publisher('/tb3_3/cmd_vel', Twist, queue_size = 10)
    publish_to_cmd_vel4 = rospy.Publisher('/tb3_4/cmd_vel', Twist, queue_size = 10)

    #create an object of pose data

    move_the_bot1 = Twist()
    move_the_bot2 = Twist()
    move_the_bot3 = Twist()
    move_the_bot4 = Twist()

    odometry_turtle_1 = Odometry()
    odometry_turtle_2 = Odometry()
    odometry_turtle_3 = Odometry()
    odometry_turtle_4 = Odometry()

    current_angle = []



    rospy.spin()


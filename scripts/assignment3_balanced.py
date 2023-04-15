#!/usr/bin/env python3

import math
from termios import VT0
from turtle import position
import rospy 
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion 


REAL_MODE = False

publish_to_cmd_vel_0 = rospy.Publisher('/bot_1/cmd_vel', Twist, queue_size = 10)
publish_to_cmd_vel_1 = rospy.Publisher('/bot_2/cmd_vel', Twist, queue_size = 10)
publish_to_cmd_vel_2 = rospy.Publisher('/bot_3/cmd_vel', Twist, queue_size = 10)
publish_to_cmd_vel_3 = rospy.Publisher('/bot_4/cmd_vel', Twist, queue_size = 10)
publish_to_cmd_vel_4 = rospy.Publisher('/bot_5/cmd_vel', Twist, queue_size = 10)
publish_to_cmd_vel_5 = rospy.Publisher('/bot_6/cmd_vel', Twist, queue_size = 10)
publish_to_cmd_vel_6 = rospy.Publisher('/bot_7/cmd_vel', Twist, queue_size = 10)
publish_to_cmd_vel_7 = rospy.Publisher('/bot_8/cmd_vel', Twist, queue_size = 10)

if REAL_MODE:
    NUMBER_OF_ROBOTS = 4
    K                = 1 #k > 0: balanced configuration, k < 0: synchronised configuration  
    orientation      = [0.0] * NUMBER_OF_ROBOTS
    robot_positions  = [0.0] * NUMBER_OF_ROBOTS
    w0               = 1.0
    v0               = 0.1
else:
    NUMBER_OF_ROBOTS = 3
    K                = 10 #k > 0: balanced configuration, k < 0: synchronised configuration 
    orientation      = [0.0] * NUMBER_OF_ROBOTS
    robot_positions  = [0.0] * NUMBER_OF_ROBOTS
    w0               = 2.4
    v0               = 0.05


def odomdata_callback(msg, number):
    global orientation
    quaternion_list = [msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
                       msg.pose.pose.orientation.z, msg.pose.pose.orientation.w] 
    orientation[number] = euler_from_quaternion(quaternion_list)[2]

def get_desired_delta_angle(bot_number, k):
    heading = 0
    for angle in orientation: 
        #u(t)i = -k/n sum(sin(thetaj - thetai))
        a = angle - orientation[bot_number]
        if (a>math.pi):
            a -= 2*math.pi
        if(a<-math.pi):
            a += 2*math.pi
        heading = heading - k / NUMBER_OF_ROBOTS * math.sin(a)
    print("abs(heading[{}]): {:.5f}".format(bot_number, abs(heading)))
    return heading + w0 * v0

def get_laplacian():
    adjacency = [[]]
    for i in range(NUMBER_OF_ROBOTS): 
        for n in range(NUMBER_OF_ROBOTS):
            adjacency[i][n] = robot_positions[i]-robot_positions[n]
    laplacian = [[]]
    for i in range(NUMBER_OF_ROBOTS): 
        row = 0
        for n in range(NUMBER_OF_ROBOTS):
            laplacian[i][n] = - adjacency[i][n]
            row += adjacency[i][n]
        laplacian[i][i] += row
    return laplacian

def get_robot_position_complex():




        

    






def move_bot(publish_to_cmd_vel, heading):
    move_the_bot = Twist()
    move_the_bot.angular.z = heading
    move_the_bot.linear.x = v0#0.05
    publish_to_cmd_vel.publish(move_the_bot)
    # if (heading < 0.1 and heading > -0.1):
    #     move_the_bot.angular.z = 0.0
    #     move_the_bot.linear.x  = v0
    #     publish_to_cmd_vel.publish(move_the_bot)

def odomdata_callback_0(msg): # msg = /bot_1/odom
    global move_the_bot_0
    odomdata_callback(msg, 0)
    heading = get_desired_delta_angle(0, K)
    move_bot(publish_to_cmd_vel_0, heading)

def odomdata_callback_1(msg): # msg = /bot_2/odom
    global move_the_bot_1
    odomdata_callback(msg, 1)
    heading = get_desired_delta_angle(1, K)
    move_bot(publish_to_cmd_vel_1, heading)

def odomdata_callback_2(msg): # msg = /bot_3/odom
    global move_the_bot_2
    odomdata_callback(msg, 2)
    heading = get_desired_delta_angle(2, K)
    move_bot(publish_to_cmd_vel_2, heading)

def odomdata_callback_3(msg): # msg = /bot_4/odom
    global move_the_bot_3
    odomdata_callback(msg, 3)
    heading = get_desired_delta_angle(3, K)
    move_bot(publish_to_cmd_vel_3, heading)

def odomdata_callback_4(msg): # msg = /bot_5/odom
    global move_the_bot_4
    odomdata_callback(msg, 4)
    heading = get_desired_delta_angle(4, K)
    move_bot(publish_to_cmd_vel_4, heading)

def odomdata_callback_5(msg): # msg = /bot_6/odom
    global move_the_bot_5
    odomdata_callback(msg, 5)
    heading = get_desired_delta_angle(5, K)
    move_bot(publish_to_cmd_vel_5, heading)


def odomdata_callback_6(msg): # msg = /bot_7/odom
    global move_the_bot_6
    odomdata_callback(msg, 6)
    heading = get_desired_delta_angle(6, K)
    move_bot(publish_to_cmd_vel_6, heading)


def odomdata_callback_7(msg): # msg = /bot_8/odom
    global move_the_bot_7
    odomdata_callback(msg, 7)
    heading = get_desired_delta_angle(7, K)
    move_bot(publish_to_cmd_vel_7, heading)



if __name__ == "__main__":
    rospy.init_node('turtlebot_controller_node')

    if REAL_MODE:
        subscribe_to_odom_0 = rospy.Subscriber('/tb3_1/odom', Odometry, callback = odomdata_callback_0)
        subscribe_to_odom_1 = rospy.Subscriber('/tb3_2/odom', Odometry, callback = odomdata_callback_1)
        subscribe_to_odom_2 = rospy.Subscriber('/tb3_3/odom', Odometry, callback = odomdata_callback_2)
        subscribe_to_odom_3 = rospy.Subscriber('/tb3_4/odom', Odometry, callback = odomdata_callback_3)
        rospy.loginfo('My node has been started')
    else:
        subscribe_to_odom_0 = rospy.Subscriber('/bot_1/odom', Odometry, callback = odomdata_callback_0)
        subscribe_to_odom_1 = rospy.Subscriber('/bot_2/odom', Odometry, callback = odomdata_callback_1)
        subscribe_to_odom_2 = rospy.Subscriber('/bot_3/odom', Odometry, callback = odomdata_callback_2)
        # subscribe_to_odom_3 = rospy.Subscriber('/bot_4/odom', Odometry, callback = odomdata_callback_3)
        # subscribe_to_odom_4 = rospy.Subscriber('/bot_5/odom', Odometry, callback = odomdata_callback_4)
        # subscribe_to_odom_5 = rospy.Subscriber('/bot_6/odom', Odometry, callback = odomdata_callback_5)
        # subscribe_to_odom_6 = rospy.Subscriber('/bot_7/odom', Odometry, callback = odomdata_callback_6)
        # subscribe_to_odom_7 = rospy.Subscriber('/bot_8/odom', Odometry, callback = odomdata_callback_7)
        rospy.loginfo('My node has been started')

    rospy.spin()


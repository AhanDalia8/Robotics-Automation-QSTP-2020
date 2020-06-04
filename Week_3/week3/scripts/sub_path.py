#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point, Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math
from math import atan2

x = 1
y = 1
z = 0
theta = 0
goal = Point()
goal.x = 1
goal.y = 1
vel = Twist()
kp = 1
kd = 0
ki = 0

def path_callback(data):
    global goal
    goal.x = data.x
    goal.y = data.y

def odom_callback(data):
    global x, y, theta
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    rot_tur = data.pose.pose.orientation
    (r, p, theta ) = euler_from_quaternion([ rot_tur.x, rot_tur.y, rot_tur.z, rot_tur.w ])

def rot_bot():
    global goal_angle, theta, vel
    vel.linear.x = 0
    vel.angular.z = kp*(goal_angle - theta)

def move_bot():
    global goal, vel, x, y, dist
    vel.angular.z = 0
    print(dist)
    if (dist > 0.15):
        vel.linear.x = 0.5
    else:
        vel.linear.x = 0



rospy.init_node('sub_path', anonymous = True)
sub1 = rospy.Subscriber('/path', Point, path_callback)
sub2 = rospy.Subscriber('/odom', Odometry, odom_callback)
pub2 = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(4)

vel.linear.y = 0
vel.linear.z = 0
vel.angular.x = 0
vel.angular.y = 0

while not rospy.is_shutdown():
    new_x = goal.x - x
    new_y = goal.y - y
    try:
        goal_angle = atan2(new_y, new_x)
    except ZeroDivisionError:
        goal_angle = ((goal.y/abs(goal.y))*math.pi)/180
    if (abs( goal_angle - theta ) > 0.1):
        rot_bot()
        #vel.linear.x = 0.0
        #vel.angular.z = 0.3
        #print(abs(goal_angle - theta))
    else:
        dist = math.sqrt((new_x)**2 + (new_y)**2)
        #if (dist > 0.2):
        move_bot()
            #vel.linear.x = 0.5
            #vel.angular.z = 0
        '''else:
            vel.linear.x = 0
            vel.angular.z = 0'''
    pub2.publish(vel)
    #rospy.loginfo(vel)
    rate.sleep()
#rospy.spin()
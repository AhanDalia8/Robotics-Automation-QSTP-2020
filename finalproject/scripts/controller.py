#!/usr/bin/env python
import rospy
from finalproject.msg import valuelist
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
vel = Twist()
kp = 1
kd = 0
ki = 0
end_point = Point()
end_point.x = 6
end_point.y = 6

final_path = valuelist()

def path_callback(data):
    global final_path
    final_path.valuex = data.valuex
    final_path.valuey = data.valuey

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

def move_bot(angle):
    global goal, vel, x, y, dist
    vel.angular.z = 0
    #if (dist > 0.3):
    vel.linear.x = 0.5* math.cos(angle)
    vel.linear.y = 0.5* math.sin(angle)
    #else:
    #vel.linear.x = 0

rospy.init_node('controller', anonymous = True)
sub2 = rospy.Subscriber('/path_follow', valuelist, path_callback)
sub3 = rospy.Subscriber('/odom', Odometry, odom_callback)
pub3 = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
rate = rospy.Rate(4)

vel.linear.y = 0
vel.linear.z = 0
vel.angular.x = 0
vel.angular.y = 0
new_x = 1
new_y = 1

while not rospy.is_shutdown():
    for i in range (0, len(final_path.valuex)):
        goal.x = final_path.valuex[i]
        goal.y = final_path.valuey[i]
        while ( math.sqrt((new_x)**2 + (new_y)**2)  > 0.2 ):            
            dist = math.sqrt((new_x)**2 + (new_y)**2)
            new_x = goal.x - x
            new_y = goal.y - y
            rospy.loginfo(dist)
            rospy.loginfo(goal.x)
            rospy.loginfo(goal.z)
            try:
                goal_angle = atan2(new_y, new_x)
            except ZeroDivisionError:
                goal_angle = ((goal.y/abs(goal.y))*math.pi)/180
            #if (abs( goal_angle - theta ) > 0.3):
            #    rot_bot()
            #else:
            move_bot( goal_angle - theta )
            pub3.publish(vel)
            rate.sleep()
            if rospy.is_shutdown():
                break
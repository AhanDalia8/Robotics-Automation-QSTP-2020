#!/usr/bin/env python
from __future__ import print_function
import rospy
import sys
from week2.srv import *
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
radius = 1
ang_vel = 0

def radius_callback(data):
    global radius
    radius = data.data

def compute_ang(r, lv):
    rospy.wait_for_service('compute_ang_vel')
    compute_ang_vel = rospy.ServiceProxy('compute_ang_vel', ComputeVel)
    resp1 = compute_ang_vel(r, lv)
    global ang_vel
    ang_vel = resp1.ang_vel

rospy.init_node('turtle_client', anonymous = True)
rospy.Subscriber('radius', Float32 , radius_callback)
pub2 = rospy.Publisher('/cmd_vel', Twist, queue_size = 2)

lv = 1
rot = Twist()
rot.linear.y = 0
rot.linear.z = 0
rot.angular.x = 0
rot.angular.y = 0
while not rospy.is_shutdown():
    compute_ang(radius, lv)
    rot.linear.x = lv
    rot.angular.z = ang_vel
    rospy.loginfo(rot)
    pub2.publish(rot)
rospy.spin()
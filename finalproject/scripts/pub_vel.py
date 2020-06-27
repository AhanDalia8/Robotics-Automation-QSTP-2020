#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

vel = Twist()

rospy.init_node('pub_vel', anonymous = True)
pub1 = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(4)

vel.linear.y = 0
vel.linear.z = 0
vel.angular.x = 0
vel.angular.y = 0

while not rospy.is_shutdown():
    vel.linear.x = 1
    vel.angular.z = 1
    pub1.publish(vel)
    rospy.loginfo(vel)
    rate.sleep()

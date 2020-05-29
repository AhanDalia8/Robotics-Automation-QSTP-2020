#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('top1', anonymous = True)
pub1 = rospy.Publisher('name', String, queue_size = 10)
rate = rospy.Rate(10)

name = "Ahan"
while not rospy.is_shutdown():
    rospy.loginfo(name)
    pub1.publish(name)
    #print(name)
    rate.sleep()

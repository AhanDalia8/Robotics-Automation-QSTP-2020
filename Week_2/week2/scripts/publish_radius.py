#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

rospy.init_node('publish_radius', anonymous = True)
pub1 = rospy.Publisher('radius', Float32, queue_size = 10)
rate = rospy.Rate(10)

r = 1
while not rospy.is_shutdown():
    rospy.loginfo(r)
    pub1.publish(r)
    rate.sleep()

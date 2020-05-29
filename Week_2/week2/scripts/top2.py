#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('top2', anonymous = True)
pub2 = rospy.Publisher('surname', String, queue_size = 10)
rate = rospy.Rate(10)

surname = "Dalia"
while not rospy.is_shutdown():
    rospy.loginfo(surname)
    pub2.publish(surname)
    #print(surname)
    rate.sleep()

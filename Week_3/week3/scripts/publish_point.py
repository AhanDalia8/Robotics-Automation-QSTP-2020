#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

rospy.init_node('publish_point')
pub1 = rospy.Publisher('/path', Point, queue_size=10)
rate = rospy.Rate(10)

val = Point()
val.x = 2
val.y = 2
val.z = 0

while not rospy.is_shutdown():
    rospy.loginfo(val)
    pub1.publish(val)
    rate.sleep()
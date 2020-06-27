#!/usr/bin/env python
import rospy
from finalproject.msg import valuelist


obstacles_list = valuelist()

obstacles_list.valuex = [0, 0, 0, 1.5, 1.5, 1.5, 1.5, 3, 3, 3, 3, 4.5, 4.5, 4.5, 4.5]
obstacles_list.valuey = [1.5, 3, 4.5, 0, 1.5, 3, 4.5, 0, 1.5, 3, 4.5, 0, 1.5, 3, 4.5]

rospy.init_node('obstacle_detector', anonymous = True)
pub1 = rospy.Publisher('/obsta_list', valuelist, queue_size= 1)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    connections = pub1.get_num_connections()
    #rospy.loginfo("Connections: ")
    #rospy.loginfo(connections)
    if (connections > 0 ):
        pub1.publish(obstacles_list)
        rospy.loginfo(obstacles_list)
        rospy.loginfo("Obstacles published.")
        break
    rate.sleep()
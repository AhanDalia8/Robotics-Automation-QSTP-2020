#!/usr/bin/env python
import rospy
from finalproject.msg import valuelist

obstacles_list = valuelist()
path_list = valuelist()

def obsta_callback(data):
    global obstacles_list
    obstacles_list.valuex = data.valuex
    obstacles_list.valuey = data.valuey 

rospy.init_node('planner', anonymous = True)
sub1 = rospy.Subscriber('/obsta_list', valuelist, obsta_callback)
pub2 = rospy.Publisher('/path_follow', valuelist, queue_size = 1)
rate = rospy.Rate(10)

path_list.valuex = [0.75, 0.75, 0.75, 0.75, 6]
path_list.valuey = [0.75, 2.75, 3.75, 4.75, 6]

while not rospy.is_shutdown():
    connections = pub2.get_num_connections()
    #rospy.loginfo("Connections: ")
    #rospy.loginfo(connections)
    if (connections > 0 ):
        pub2.publish(path_list)
        rospy.loginfo(path_list)
        rospy.loginfo("Path published.")
        break
    rate.sleep()
    
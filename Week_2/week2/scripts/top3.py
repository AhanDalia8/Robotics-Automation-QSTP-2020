#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#global name
#global surname
name = ""
surname = ""
def name_callback(data):
    #print(data)
    global name 
    name = data.data
    #print(name)

def surname_callback(data):
    #print(data) 
    global surname 
    surname = data.data
    #print(surname)

rospy.init_node('top3', anonymous = True)
rospy.Subscriber('name', String , name_callback)
rospy.Subscriber('surname', String, surname_callback)
pub3 = rospy.Publisher('fullname', String, queue_size = 10)

#fullname = name + surname
while not rospy.is_shutdown():
    fullname = str(name) + " " + str(surname)
    rospy.loginfo(fullname)
    pub3.publish(fullname)
    #print(fullname)
rospy.spin()
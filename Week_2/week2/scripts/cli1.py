#!/usr/bin/env python
from __future__ import print_function
import rospy
import sys
from week2.srv import *

def convert_coord(x,y,a):
    rospy.wait_for_service('convert_coordinates')
    convert_coordinates = rospy.ServiceProxy('convert_coordinates', ConvertCoordinates)
    resp1 = convert_coordinates(x,y,a)
    print("The converted coordinates are (%f, %f)"%(resp1.first_c, resp1.second_c)) 

if len(sys.argv) == 4:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    a = float(sys.argv[3])
else:
    sys.exit(1)

print("Converting the coordinates...")
convert_coord(x,y,a)
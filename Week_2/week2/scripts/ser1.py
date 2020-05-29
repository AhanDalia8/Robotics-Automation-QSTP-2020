#!/usr/bin/env python
from __future__ import print_function
from week2.srv import ConvertCoordinates, ConvertCoordinatesResponse
import rospy
import math 

def handle_convert_coordinates(req):
    print("Coordinates submitted...")
    if (req.to_polar == 1):
        x = req.first_coordinate
        y = req.second_coordinate
        r = math.sqrt(x**2 + y**2)
        theta = math.atan(y/x)
        theta = math.degrees(theta)
        if (x < 0):
            theta = 180 + theta
        elif(y < 0):
            theta = (360 + theta)
        first_c = round(r, 4)
        second_c = round(theta, 4)
    else:
        r = req.first_coordinate
        theta = math.radians(req.second_coordinate)
        x = r*math.cos(theta)
        y = r*math.sin(theta)
        first_c = round(x, 4)
        second_c = round(y, 4)

    return(ConvertCoordinatesResponse(first_c, second_c))

rospy.init_node('ser1')
s = rospy.Service('convert_coordinates', ConvertCoordinates, handle_convert_coordinates)
print("Ready to Convert Coordinates")
rospy.spin()
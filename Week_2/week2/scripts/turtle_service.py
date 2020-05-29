#!/usr/bin/env python
from __future__ import print_function
from week2.srv import ComputeVel, ComputeVelResponse
import rospy

def handle_compute_vel(reg):
    print("Computing Angular Velocity... ")
    ang_vel = reg.l_vel/reg.radius
    return ComputeVelResponse(ang_vel)

rospy.init_node('turtle_service')
s = rospy.Service('compute_ang_vel', ComputeVel, handle_compute_vel)
print("Velocities recorded.")
rospy.spin()
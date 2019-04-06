#!/usr/bin/env python

from tutorial.srv import servicesResponse , services
import rospy

def add_two_ints(req):
    print ("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return servicesResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')

    # 1st argument is the name of the service , 2nd is the type of service , 
    # 3rd is the function to call
    s = rospy.Service('add_two_ints', services, add_two_ints)
    print ("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
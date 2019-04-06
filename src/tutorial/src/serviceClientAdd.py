#!/usr/bin/env python

from tutorial.srv import services
import rospy
import sys

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        # 1st is the name of the service 2nd is the type of service
        add_two_ints = rospy.ServiceProxy('add_two_ints', services)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print ("Service call failed: %s"%e)


if __name__ == "__main__":
    if len(sys.argv) == 3:
       x = int(sys.argv[1]) 
       y = int(sys.argv[2])
    else:
        print("please give appropriate number of arguments")
        sys.exit(1)
    
    print ("Requesting %s+%s"%(x, y))
    print ("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
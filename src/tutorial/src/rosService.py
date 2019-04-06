#!/usr/bin/env python

import rospy
from std_srvs.srv import Trigger , TriggerResponse

def response(request):
	return TriggerResponse(
		success = True,
		message = "how you doing?"
		)

rospy.init_node('service')

# 1st argument is the name of the service , 2nd is the Trigger and 3rd is the function to which
# it goes after getting triggered
my_service = rospy.Service('/fake_service' , Trigger , response)
print("service available")
rospy.spin()
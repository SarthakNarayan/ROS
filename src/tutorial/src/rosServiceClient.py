#!/usr/bin/env python

import rospy

# in the service provider it was TriggerResponse
from std_srvs.srv import Trigger , TriggerRequest

rospy.init_node('service_client')

print("Client is active now")
# wait for this service to be running
# This service will run 24*7
rospy.wait_for_service('/fake_service')

# create a connection to the service remember it is a trigger service
ros_service = rospy.ServiceProxy('/fake_service' , Trigger)

# create an object of type TriggerRequest. We need a TriggerRequest for a Trigger service
# No need to pass any argument as it doesnt take any
sos = TriggerRequest()
print("connected to Ros Server")

# Now send the request through the connection
result = ros_service(sos)
print(result)
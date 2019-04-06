#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def anyfunctionnameuwant(msg):
	print("message received %s" %msg.data)

	# u can do anything inside this function
	#print("whatever i want")
	# u can see the difference between msg and msg.data
	# print(msg)

rospy.init_node('tutorial_subscriber')


# 1st argument is the node to which it has to subscribe 2nd argument is the type of message
# 3rd argument is the function to which it has to go
while not rospy.is_shutdown():
	sub = rospy.Subscriber('/say_hello' , String , anyfunctionnameuwant)
	rospy.spin()
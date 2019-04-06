#!/usr/bin/env python

import rospy

# name of the node when u run this file
rospy.init_node('mynode')
rate = rospy.Rate(3)

# to run the loop infinitely until ctrl + c is pressed
while not rospy.is_shutdown():
	print("hello")
	rate.sleep()

# WHEN U RUN THIS PROGRAM U WILL SEE THAT THERE IS NODE ADDED WHEN U DO ROSNODE LIST
# BUT U WILL SEE THERE WILL NO CHANGE IN TOPIC WHEN U DO ROSTOPIC LIST
# ITS TECHNICALLY NOT A MESSAGE SINCE ITS NOT TALKING TO ANOTHER NODE
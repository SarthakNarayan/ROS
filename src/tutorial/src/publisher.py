#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# name of the node
rospy.init_node('tutorial_publisher')

# first argument is the name of the topic , second is type of the message
publisher = rospy.Publisher('/say_hello' , String , queue_size = 1)

# rate of message publication
rate = rospy.Rate(3) # 3 messages per second

# to run the loop infinitely until ctrl + c is pressed

# Storing the message to be published
hello_message = String()
hello_message.data = "Message published hello"

while not rospy.is_shutdown():
	
	# the message u want to publish
	publisher.publish(hello_message)
	# to publish 3 messages per second
	# time we need to sleep to maintain the rate
	rate.sleep()

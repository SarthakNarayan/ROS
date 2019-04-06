#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from random import random

# name of the node
rospy.init_node('testing')

pub = rospy.Publisher('/random_numbers' , Float32 , queue_size = 1)

rate = rospy.Rate(1)
while not rospy.is_shutdown():
	pub.publish(random()*100)
	rate.sleep()
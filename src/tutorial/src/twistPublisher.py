#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('UsingTwist')

rate = rospy.Rate(100) # rate
pub = rospy.Publisher('/turtle1/cmd_vel' , Twist , queue_size=5)
while not rospy.is_shutdown():
    msg = Twist()
    msg.angular.z = 5
    pub.publish(msg)
    rate.sleep()
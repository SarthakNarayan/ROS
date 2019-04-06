#! /usr/bin/env python

import rospy
import pygame
from geometry_msgs.msg import Twist

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

rospy.init_node('UsingJoystickAnalog')

rate = rospy.Rate(5) # rate
pub = rospy.Publisher('/turtle1/cmd_vel' , Twist , queue_size=5)
while not rospy.is_shutdown():
    pygame.event.pump()
    msg = Twist()
    msg.angular.z = joystick.get_axis(0)*-1
    msg.linear.x = joystick.get_axis(1)*-1

    pub.publish(msg)
    rate.sleep()
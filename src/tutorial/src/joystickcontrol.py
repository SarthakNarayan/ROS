#! /usr/bin/env python

import rospy
import pygame
from geometry_msgs.msg import Twist

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

rospy.init_node('UsingJoystick')

rate = rospy.Rate(100) # rate
pub = rospy.Publisher('/turtle1/cmd_vel' , Twist , queue_size=5)
while not rospy.is_shutdown():
    pygame.event.pump()
    msg = Twist()
    if (joystick.get_button(0)):
        msg.angular.z = joystick.get_button(0)*2.5
    if (joystick.get_button(1)):
        msg.angular.z = joystick.get_button(1)*-2.5
    if (joystick.get_button(2)):
        msg.linear.x = joystick.get_button(2)*2.5
    if (joystick.get_button(3)):
        msg.linear.x = joystick.get_button(3)*-2.5
    
    pub.publish(msg)
    rate.sleep()
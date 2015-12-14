#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('lin_invert')
pub = rospy.Publisher('cmd_vel', Twist)

def invert_callback(data):
    inverted_message = data
    inverted_message.linear.x *= -1
    inverted_message.linear.y *= -1
    inverted_message.linear.z *= -1

    pub.publish(inverted_message)

def merger():
    rospy.Subscriber('cmd_vel_input', Twist, invert_callback)
    rospy.spin()


if __name__ == '__main__':
    merger()



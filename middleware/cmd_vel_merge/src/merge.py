#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('cmd_vel_merge')
pub = rospy.Publisher('merged_output', Twist, queue_size=10)

msg_to_send = Twist()
msg_to_send.linear.x = 0
msg_to_send.linear.y = 0
msg_to_send.linear.z = 0
msg_to_send.angular.x = 0
msg_to_send.angular.y = 0
msg_to_send.angular.z = 0

def send_command():
	# rospy.log*('Sennding command')
	pub.publish(msg_to_send)

def linear_cb(data):
	# rospy.log*('got a linear twist message.')
	msg_to_send.linear.x = data.linear.x
	msg_to_send.linear.y = data.linear.y
	msg_to_send.linear.z = data.linear.z
	send_command()
	msg_to_send.angular.x = 0
	msg_to_send.angular.y = 0
	msg_to_send.angular.z = 0


def angular_cb(data):
	# rospy.log*('got a angular twist message.')
	msg_to_send.angular.x = data.angular.x
	msg_to_send.angular.y = data.angular.y
	msg_to_send.angular.z = data.angular.z
	send_command()
	msg_to_send.linear.x = 0
	msg_to_send.linear.y = 0
	msg_to_send.linear.z = 0

def merger():
	rospy.Subscriber('input_linear', Twist, linear_cb)
	rospy.Subscriber('input_angular', Twist, angular_cb)

	rospy.spin()


if __name__ == '__main__':
	merger()



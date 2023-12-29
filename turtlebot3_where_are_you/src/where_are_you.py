#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def odom_callback(msg):
    position = msg.pose.pose.position
    orientation = msg.pose.pose.orientation
    rospy.loginfo("Linear Position:")
    rospy.loginfo("x: %f, y: %f, z: %f", position.x, position.y, position.z)
    rospy.loginfo("Angular Orientation:")
    rospy.loginfo("x: %f, y: %f, z: %f, w: %f", orientation.x, orientation.y, orientation.z, orientation.w)


if __name__ == '__main__':
    rospy.init_node('where_are_you', anonymous=True)
    rospy.Subscriber('/odom', Odometry, odom_callback)
    rospy.spin()
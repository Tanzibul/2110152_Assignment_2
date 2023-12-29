#!/usr/bin/env python3

import rospy
from std_msgs.msg import String




if __name__ == '__main__':
    rospy.init_node("Tanzdude", anonymous = True)
    
    rate = rospy.Rate(10)

    while not rospy.is_shutdown() :

        rospy.loginfo(f"BYE BYE WORKSHOP")
        


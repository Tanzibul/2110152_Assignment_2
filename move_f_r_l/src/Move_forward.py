#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist





if __name__=='__main__':


    rospy.init_node('Move_forawrd', anonymous= True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        velo = Twist()
        velo.linear.x = 0.2
        pub.publish(velo)

        rate.sleep()

  
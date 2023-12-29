#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist





class comader:
    def __init__(self)->None:

        rospy.init_node('messege_reciver', anonymous=True)

        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

        rospy.Subscriber('/tanzib', String, self.command_callback)

    def command_callback(self,data):

        rospy.loginfo("Command Recieved {}".format(data.data))  

        direction = data.data
        velocity = Twist()

        if direction.lower() == "forward" :
            velocity.linear.x = 5
        elif direction.lower() == "backward" :
            velocity.linear.x = - 5
        elif direction.lower() == "left" :
            velocity.angular.z = - 5
        elif direction.lower() == "right" :
            velocity.angular.y =  5  


        self.pub.publish(velocity)        





if __name__=='__main__':
    node = comader()
    rospy.spin()
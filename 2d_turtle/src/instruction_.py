#!/usr/bin/env python3


import rospy
from std_msgs.msg import String



class sending_node:

    def __init__(self) -> None :

        rospy.init_node('2d_sending_node', anonymous = True)
        self.pub = rospy.Publisher('/tanzib', String, queue_size =10)

    def send(self, command):
        self.pub.publish(command)
        rospy.loginfo("Sending Command {}".format(command))

    def run(self):

        rospy.loginfo('Sending node is working')

        while not rospy.is_shutdown():

            command = input("Enter command:  ")      
            self.send(command)
            rospy.sleep(1)

if __name__==  '__main__':
    node = sending_node()
    node.run()           

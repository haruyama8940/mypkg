#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random


rospy.init_node('omikuzi')
pub = rospy.Publisher('okimoti', Int32, queue_size=1)
rate = rospy.Rate(0.5)
n = [100,1000,10000]
while not rospy.is_shutdown():
    k=random.choice(n)
    pub.publish(k)
    rospy.loginfo(k)
    rate.sleep()
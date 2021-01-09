#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import Int32
from std_msgs.msg import String

n=0
k=''
def luck(x):
    global k
    if x==1:
        k='DAIKICHI'
    if x==2:
        k='TYUKICHI'
    if x==3:
        k='SYOUKITCHI'
    if x==4:
        k='KYO'
    if x==5:
        k='DAIKYOU'
def cb (message):
    global n
    n = message.data
    if n == 100:
            i=random.randint(1,5)
            luck(i)
    if n == 1000:
            i=random.randint(1,4)
            luck(i)
    if n == 10000:
            i=random.randint(1,3)
            luck(i)
    rospy.loginfo(k)


if __name__ == '__main__':
    rospy.init_node('zinzya_mikuzi')
    sub = rospy.Subscriber('okimoti', Int32, cb)
    pub = rospy.Publisher('unsei',String,queue_size=1)
    while not rospy.is_shutdown():
        rospy.spin()

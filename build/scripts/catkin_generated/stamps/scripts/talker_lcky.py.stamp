#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states',JointState, queue_size=10)
    rospy.init_node('talker_azaza', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.header.frame_id = 'kek'   
    hello_str.name = ['base_to_first_link', 'base_to_second', 'first_link_to_third_link']
#    hello_str.velocity = []
#    hello_str.effort = []
    a = 0.0
    b = 0.0
    c = 0.0
    flag_1 = True
    flag_2 = True
    while not rospy.is_shutdown():
	    
	    hello_str.header.stamp = rospy.Time.now()
	    hello_str.position = [a, b, c]
	    b = b + 0.5
	    if flag_2:
	        c = c + 0.1
	        if c > 2.39:
	            flag_2 = False   
	    else:
	        c = c - 0.1
	        if c < -2.30:
	            flag_2 = True
	    
	    if flag_1:
	        a = a + 0.1
	        if a > 1.1:
	            flag_1 = False   
	    else:
	        a = a - 0.1
	        if a < -1.1:
	            flag_1 = True
	        
	    pub.publish(hello_str)
	    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

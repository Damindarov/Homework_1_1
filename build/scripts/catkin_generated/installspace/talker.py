#!/usr/bin/env python3
# license removed for brevity
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states',JointState, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['right_front_wheel_joint', 'right_back_wheel_joint', 'left_front_wheel_joint', 'left_back_wheel_joint','gripper_extension',
    'gripper_extension','right_gripper_joint',
    'head_swivel']
    hello_str.velocity = []
    hello_str.effort = []
    a = 0
    while not rospy.is_shutdown():
	    
	    hello_str.header.stamp = rospy.Time.now()
	    hello_str.position = [a, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	    a = a + 1
	    pub.publish(hello_str)
	    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

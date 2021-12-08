#!/usr/bin/env python

import rospy
from cv_bridge import CvBridge, CvBridgeError
import cv2

class Environment():
    def __init__(self):
        '''ver o que colocar'''

    def image_callback(self, data):
        ''' imagen pra calibrar, pode ser camera do notebook pra teste'''



    


if __name__ == '__main__':
    rospy.init_node('control')

    rate = rospy.Rate(100)

    env = Environment()
    env.reset()

    rospy.spin()
        
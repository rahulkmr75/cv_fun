#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;
import rospy
from matplotlib import pyplot as plt
import const
def findMoment(frame):
	

	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	#masking everything else other than green
	mask=cv2.inRange(hsv,const.low,const.high)

	#applying gaussian blur
	bot=cv2.GaussianBlur(mask,(5,5),0)
	bot=cv2.GaussianBlur(mask,(5,5),0)
	bot=cv2.GaussianBlur(mask,(5,5),0)
	# ret, gline = cv2.threshold(gline,100,255,cv2.THRESH_BINARY)
	ret, bot = cv2.threshold(bot,-1,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	# Take the moments to get the centroid
	moments = cv2.moments(bot)
	m00 = moments['m00']
	centroid_x, centroid_y = None, None
	if m00 != 0:
	    centroid_x = int(moments['m10']/m00)
	    centroid_y = int(moments['m01']/m00)
	if centroid_x != None and centroid_y != None:
		return (centroid_x, centroid_y,0)
	else:
		return (-1,-1,0)


import numpy as np
import cv2



MIN_MATCH_COUNT = 5

img1 = cv2.imread('Template.png')# anh_logo
img2 = cv2.imread('result.png') # anh_muon_xet

img1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

if len(good)>MIN_MATCH_COUNT:
    print ("we have {} matches".format(len(good)))
    print("We found it")
else:
    print ("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))

import csv
from subprocess import Popen
import subprocess
import time
import cv2
import numpy as np
import os.path
import os

with open('ip.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        web = line['Multicast_IP']
        web2 = 'udp://@{}?pkt_size=1480'.format(web)
        print(web2)
        proc = subprocess.Popen(
            ['ffmpeg', '-i', web2, '-vf', "select='eq(pict_type\,I)+eq(pict_type\,P)'", "-vframes", "1", "-y",
             'thump.jpg']) #calling subprocess
        time.sleep(10) #wait 10s here
        if (os.path.isfile('thump.jpg') == True): #check if it produces a keyframe, if not kill process and move to another IP 
            MIN_MATCH_COUNT = 5

            img1 = cv2.imread('thump.jpg')  # anh_logo
            img2 = cv2.imread('result.png')  # anh_muon_xet

            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            sift = cv2.xfeatures2d.SIFT_create()

            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)

            FLANN_INDEX_KDTREE = 0
            index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
            search_params = dict(checks=50)

            flann = cv2.FlannBasedMatcher(index_params, search_params)

            matches = flann.knnMatch(des1, des2, k=2)

            good = []
            for m, n in matches:
                if m.distance < 0.7 * n.distance:
                    good.append(m)

            if len(good) > MIN_MATCH_COUNT:
                print("we have {} matches".format(len(good)))
                print("We found logo FPT")
                os.remove('thump.jpg')     #right now, file is removed so storage will not be affected

                with open('ip2.csv', 'a') as newFile: # the result will be put in here
                    newFileWriter = csv.writer(newFile)
                    newFileWriter.writerow(['yes'])

            else:
                print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
                os.remove('thump.jpg')
                with open('ip2.csv', 'a') as newFile:
                    newFileWriter = csv.writer(newFile)
                    newFileWriter.writerow(['no'])
        else:
            with open('ip2.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                newFileWriter.writerow(['not available'])
            proc.kill()  #killing process and move on 
csv_file.close()

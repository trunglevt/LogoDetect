
This is a logo detection project by using the SIFT and FLANN from opencv and numpy. There are two example files in here. U need to have python, numpy, ffmpeg install. Method of operation would be parsing IP from csv file->use ffmpeg to get data from source->Each channel will have a 10s window for processing-> if it captures a file, file will be processed. If not, the ffmpeg process will be killed and move on to another IP. The result will be written to another csv file, showing the multicast IP and their respective states(yes,no,not available)

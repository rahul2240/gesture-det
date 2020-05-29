import os
import math
import cv2

listing = os.listdir("~/rahul/test_data/class_3")
count = 1
for file in listing:
    video = cv2.VideoCapture("~/rahul/test_data/class_3/" + file)
    print(video.isOpened())
    framerate = video.get(5)
    os.makedirs("./test_data/" + "video_" + str(int(count)))
    while (video.isOpened()):
        frameId = video.get(1)
        success,image = video.read()
        if( image != None ):
            image=cv2.resize(image,(224,224), interpolation = cv2.INTER_AREA)
        if (success != True):
            break
        if (frameId % math.floor(framerate) == 0):
            filename = "~/rahul/video_" + str(int(count)) + "/image_" + str(int(frameId / math.floor(framerate))+1) + ".jpg"
            print(filename)
            cv2.imwrite(filename,image)
    video.release()
    print('done')
    count+=1

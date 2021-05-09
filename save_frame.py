import cv2
import os
import time
"""
try:
    os.makedirs('data')
except OSError:
    pass
# Log the time
time_start = time.time()
# Start capturing the feed
cap = cv2.VideoCapture('test.mkv')
# Find the number of frames
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
print('Number of frames:',video_length)
count = 0
#print('converting video..\n')
while cap.isOpened():
    # Extract the frame
    ret,frame = cap.read()
    # Write the result back to output location
    cv2.imwrite('data' + '/%#05d.jpg' % (count+1),frame)
    count += 1
    # If there are no more frames left
    if (count > (video_length-1)):
        time_end = time.time()
        print ("Done extracting frames.\n%d frames extracted" % count)
        print ("It took %d seconds forconversion." % (time_end-time_start))
        break
cap.release()
cv2.destroyAllWindows()
"""
"""
cap = cv2.VideoCapture('test.mkv')
#success,image = vidcap.read()
count = 0
#success = True
while cap.isOpened():
  success,image = cap.read()
  print('Read a new frame: ', success)
  cv2.imwrite("frame{}.jpg".format(count), image)
  count += 1
  if success == False:
      break
"""

#if anyone does not want to extract every frame but wants to extract frame every one second.So 1 minute video will give 60 frames(images).

import cv2

def extractImages(pathIn, pathOut):
    count = 0
    cap = cv2.VideoCapture(pathIn)
    success = True
    while success:
      cap.set(cv2.CAP_PROP_POS_MSEC,(count*250))# (count*1000) it gives every second 1 frames,if you want every second 4 frames multiply by 0.25
      success,image = cap.read()
      #print ('Read a new frame: ', success)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      count += 1
extractImages('test.mkv','output')

#if __name__=="__main__":
    #print("aba")
    #a = argparse.ArgumentParser()
    #a.add_argument("--pathIn", help="path to video")
    #a.add_argument("--pathOut", help="path to images")
    #args = a.parse_args()
    #print(args)
    #extractImages(args.pathIn, args.pathOut)

#propId	Property identifier. It can be one of the following:

    #CAP_PROP_POS_MSEC: Current position of the video file in milliseconds.
    #CAP_PROP_POS_FRAMES: 0-based index of the frame to be decoded/captured next.
    #CAP_PROP_POS_AVI_RATIO: Relative position of the video file: 0 - start of the film, 1 - end of the film.
    #CAP_PROP_FRAME_WIDTH: Width of the frames in the video stream.
    #CAP_PROP_FRAME_HEIGHT: Height of the frames in the video stream.
    #CAP_PROP_FPS: Frame rate.
    #CAP_PROP_FOURCC: 4-character code of codec.
    #CAP_PROP_FRAME_COUNT: Number of frames in the video file.
    #CAP_PROP_FORMAT: Format of the Mat objects returned by retrieve() .
    #CAP_PROP_MODE: Backend-specific value indicating the current capture mode.
    #CAP_PROP_BRIGHTNESS: Brightness of the image (only for cameras).
    #CAP_PROP_CONTRAST: Contrast of the image (only for cameras).
    #CAP_PROP_SATURATION: Saturation of the image (only for cameras).
    #CAP_PROP_HUE: Hue of the image (only for cameras).
    #CAP_PROP_GAIN: Gain of the image (only for cameras).
    #CAP_PROP_EXPOSURE: Exposure (only for cameras).
    #CAP_PROP_CONVERT_RGB: Boolean flags indicating whether images should be converted to RGB.
    #CAP_PROP_WHITE_BALANCE: Currently unsupported
    #CAP_PROP_RECTIFICATION: Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)

#value	Value of the property.

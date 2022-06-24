#timelapse photogrpahy
import time
from picamera import PiCamera
import os

#time delay from bootup
time.sleep(20)

camera= PiCamera()
camera.resolution = (2592,1944)
#camera.start_preview()
time.sleep(2)

#desired length of timelapse video
vidLength = 0.5 #mins
#how fast will it run
fps = 25 #frames per second (frame change every 0.04 sec)
numFrames =vidLength*60*fps

#Leng Pi will shoot for
runHrs = 0.5 #hrs
runSec = runHrs*60*60

#loop through all frames
frame=0
while frame < numFrames:
    camera.capture('/home/pi/Videos/timeLapse/pic_%i.jpg' % (frame))
    frame = frame + 1
    time.sleep((runSec)/numFrames)
    
#shut down the system
os.system('sudo shutdown now')
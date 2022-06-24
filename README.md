# Time-Lapse-Photo

A simple python script for executing time lapse photography using a Raspberry Pi!

The materials used in this project include:
    Raspberry Pi Zero W2
    Zero Spy Camera (https://www.adafruit.com/product/3508)
    
The script will save a series of .JPG files to a folder called "timeLapse" within the Videos subdirectory on the Raspberry Pi. The included script can be adjusted to the desired length you would like the camera to photograph, the desired length you would like the time lapse video to be, and the desired fps. 

Once the photography is complete the, the .JPG files can be transfered over to a PC and compiled into a video file.

To start the photography, you can either SSH to the Raspberry Pi to start the script, or include a condition to start to script on start up. I have elected for the latter for ease.

A lot of this code was based off of tutorials from the YouTube channel Explaining Computers (https://www.youtube.com/watch?v=Fer4SssH4FE&t=867s)

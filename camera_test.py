from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview() #will display the camera onto the screen for you
time.sleep(2) #min amount of time to wait before you start taking photos

camera.capture("testpic.jpg")

camera.stop_preview()
    

    
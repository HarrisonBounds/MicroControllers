#Testing the PIR Sensor
import RPi.GPIO as GPIO
import time

led = 16
pir_sensor = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pir_sensor, GPIO.IN)

try:
    while True:
        sensor_read = GPIO.input(pir_sensor)
        
        while sensor_read == True:
            GPIO.output(led, True)
            print("Motion Detected")
            sensor_read = GPIO.input(pir_sensor)
            
        while sensor_read == False:
            GPIO.output(led, False)
            print("NOTHING")
            sensor_read = GPIO.input(pir_sensor)
            
            
except KeyboardInterrupt:
    print("Goodbye")
    
finally:
    GPIO.cleanup()
            
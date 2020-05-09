# To be run from the raspberry pi. 
# Sends data about the distance to sonic-pi

import RPi.GPIO as GPIO
import time
from pythonosc import udp_client
from pythonosc import osc_message_builder
HOSTNAME="Matildes-MacBook-Air.local"
SONIC_PI_PORT=4560

def getDistance(i):
    GPIO.setmode(GPIO.BCM)

    TRIG=23
    ECHO=24

    print("Distance Measurement in Progress")

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)


    GPIO.output(TRIG, False)
    print("Waiting for Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
 
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
 
    pulse_duration= pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

i=0

while True:
    sender = udp_client.SimpleUDPClient(HOSTNAME, SONIC_PI_PORT)
    distance=float(getDistance(i))

    if (distance > 85):
        midi = 85
    if (distance < 85):
        # map distances into playable values
        midi = 7/6 * distance + 40
    if (i > 4):
        i = 0
    else: 
        i = i + 1
    print(midi)
    sender.send_message('/trigger/hollow', [midi, 3.5, i])
    time.sleep(2)

GPIO.cleanup()
 

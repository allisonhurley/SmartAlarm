#!/usr/bin/python3

import subprocess
import RPi.GPIO as GPIO
import time
import datetime
import alsaaudio

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(13, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin

mixer = alsaaudio.Mixer('PCM')
unsnooze = datetime.datetime.now()

while True:
    now = datetime.datetime.now()

    i=GPIO.input(11)

    if i==0: #When output from motion sensor is LOW

        # print "No intruders",i

        time.sleep(0.1)

    elif i==1: #When output from motion sensor is HIGH

        subprocess.run(["/home/pi/SmartAlarm/alarm_off"])

        time.sleep(0.1)

    if GPIO.input(13) == 1:
        # snooze active
        mixer.setvolume(0)
        unsnooze = now + datetime.timedelta(minutes=1)

    if now >= unsnooze:
        mixer.setvolume(100)
        

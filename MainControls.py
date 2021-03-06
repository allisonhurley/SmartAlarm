#!/usr/bin/python3

import subprocess
import RPi.GPIO as GPIO
import time
import datetime
import alsaaudio
import os
import os.path
from enum import Enum, auto

class Mode(Enum):
    Awake = auto()
    Sleep = auto()
    Snooze = auto()
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # setup snooze button
GPIO.setup(3, GPIO.OUT)         #LED output pin

mixer = alsaaudio.Mixer('PCM')
unsnooze = datetime.datetime.now()
mode = Mode.Sleep
off_file = "/home/pi/SmartAlarm/screenoff"
if os.path.exists(off_file):
    os.unlink(off_file)
subprocess.run(["/home/pi/SmartAlarm/alarm_off"])

while True:
    now = datetime.datetime.now()
    motion_detected = GPIO.input(11) == 1
    snooze_pressed = GPIO.input(13) == 1

    print("mode: " + str(mode))
    print("motion: " + str(motion_detected))
    print("snooze: " + str(snooze_pressed))

    if mode == Mode.Sleep:
        # check to see if file screenoff has been deleted
        if not os.path.exists(off_file):
            mode = Mode.Awake
    
    elif mode == Mode.Awake:

        if motion_detected:
            # go to sleep
            subprocess.run(["/home/pi/SmartAlarm/alarm_off"])
            mode = Mode.Sleep

        elif snooze_pressed:
            mode = Mode.Snooze
            unsnooze = now + datetime.timedelta(minutes=1)
            subprocess.run(["/home/pi/SmartAlarm/volume_off"])

    elif mode == Mode.Snooze:

        if motion_detected:
            # go to sleep
            subprocess.run(["/home/pi/SmartAlarm/alarm_off"])
            mode = Mode.Sleep

        if now > unsnooze:
            subprocess.run(["/home/pi/SmartAlarm/volume_on"])
            mode = Mode.Awake

    time.sleep(0.1)


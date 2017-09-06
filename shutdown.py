#!/usr/bin/env python

#############################
# photobooth.py
# created by ChaoticOrb
#############################

from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    print('Button pushed - shutting down...')
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(23)
shutdown_btn.when_pressed = shutdown

pause()

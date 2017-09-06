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

shutdown_btn = Button(23, hold_time=5)
shutdown_btn.when_held = shutdown

pause()

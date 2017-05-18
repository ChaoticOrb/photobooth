
#!/usr/bin/env python

#############################
# photobooth.py
# created by ChaoticOrb
#############################
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime
from gpiozero import Button, LED, LEDBoard

#############################
# variables config
#############################
camera = PiCamera()

yellow_button = Button(17) # pin for the start Button
# red = LED(27) # red led
leds = LEDBoard(22, 27, 13)

total_photos = 3 # total number of photos to take
capture_delay = 3 # delay between taking photos
countdown = 3 # countdown for each photo
res_w = 800 # width of camera resolution (max is 2592)
res_h = 480 # height of camera resolution (max is 1944)
text_size = 80 # size of annotated text
text_color = '#fff' # colour of annotated text
bg_color = '#000' # colour of annotated text background
test_server = 'www.google.com' # server location to check for network
reset_delay = 5


#############################
# functions
#############################
def fireUp():
    # show image about pressing the button
    yellow_button.wait_for_press()
    print('Button pressed')
    previewOn()

def previewOn():
    camera.vflip = False # change if camera is mounted upside down
    camera.resolution = camera.MAX_RESOLUTION
    camera.start_preview(resolution=(res_w, res_h))
    print('Camera preview turned on')
    takePhotos()

def takePhotos():
    try:
        timestamp = datetime.now().strftime('%d%m%Y-%H%M%S') # create datetime for file naming

        camera.annotate_foreground = Color(text_color)
        camera.annotate_background = Color(bg_color)
        camera.annotate_text_size = text_size
        camera.annotate_text = 'Get Ready!'
        sleep(1)
        camera.annotate_text = 'Photos taken after {}s countdown'.format(countdown)
        sleep(1)
        # photo loop starts
        for x in range(1,total_photos + 1):
            count = 3
            for i in range(1,countdown + 1):
                camera.annotate_text = '{}...'.format(count)
                sleep(1)
                count = count - 1
            camera.annotate_text = ''
            red.on()
            sleep(1)
            red.off()
            print('Taking photo {} - img'.format(x) + timestamp + '-{}.jpg'.format(x))
            camera.capture('/home/pi/captures/img' + timestamp + '-{}.jpg'.format(x))
            sleep(1)
            resetCamera() # reset camera
    finally:
        camera.close()

def resetCamera():
    camera.annotate_text = 'Saving...'
    LEDBoard(1,0,0)
    sleep(1)
    LEDBoard(1,1,0)
    sleep(1)
    LEDBoard(1,1,1)
    leds.blink()
    sleep(2)
    camera.annotate_text = 'Resetting...'
    print('Restarting')
    sleep(reset_delay)
    camera.annotate_text = ''

#############################
# main programme
#############################
fireUp()

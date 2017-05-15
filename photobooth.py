
#############################
# photobooth.py
# created by ChaoticOrb
#############################
from picamera import PiCamera, Color
from time import sleep
from datetime import datetime
from gpiozero import Button, LED

#############################
# variables config
#############################
camera = PiCamera()


yellow_button = Button(17) # pin for the start Button
red = LED(27) # red led
green = LED(22)

total_photos = 3 # total number of photos to take
capture_delay = 1 # delay between taking photos
countdown = 1 # countdown for each photo
res_w = 2592 # width of camera resolution (max is 2592)
res_h = 1944 # height of camera resolution (max is 1944)
text_size = 140 # size of annotated text
text_color = '#fff' # colour of annotated text
bg_color = '#000' # colour of annotated text background
test_server = 'www.google.com' # server location to check for network
reset_delay = 5


#############################
# functions
#############################
def previewOn():
    camera.vflip = False # change if camera is mounted upside down
    camera.resolution = camera.MAX_RESOLUTION
    camera.start_preview(resolution=(1024, 768))
    print('Camera preview turned on')
    yellow_button.wait_for_press()
    print('Button pressed')
    takePhotos()

def takePhotos():
    try:
        timestamp = datetime.now().strftime('%d%m%Y-%H%M%S') # create datetime for file naming

        camera.annotate_foreground = Color(text_color)
        camera.annotate_background = Color(bg_color)
        camera.annotate_text_size = text_size
        camera.annotate_text = 'Get Ready!'
        sleep(2)
        camera.annotate_text = 'Photos taken after {}s countdown'.format(countdown)
        sleep(3)
        for x in range(1,total_photos + 1):
            count = 3
            for i in range(1,countdown + 1):
                camera.annotate_text = '{}...'.format(count)
                sleep(1)
                count = count - 1
            print('Taking photo {} - img'.format(x) + timestamp + '-{}.jpg'.format(x))
            camera.annotate_text = ''
            red.on()
            sleep(1)
            red.off()
            camera.capture('/home/pi/captures/img' + timestamp + '-{}.jpg'.format(x))
            sleep(1)
        green.on()
        camera.annotate_text = 'All Done! Resetting...'
        print('Restarting')
        sleep(reset_delay)
        camera.annotate_text = ''
        green.off()
    finally:
        camera.close()

previewOn()

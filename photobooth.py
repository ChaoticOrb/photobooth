
#!/usr/bin/env python

#############################
# photobooth.py
# created by ChaoticOrb
#############################
from picamera import PiCamera, Color
import pygame
from time import sleep
from datetime import datetime
from gpiozero import Button, LED, LEDBoard

#############################
# variables setup
#############################
camera = PiCamera()

yellow_button = Button(17) # pin for the start Button
# red = LED(27) # red led
leds = LEDBoard(27, 22, 5)

total_photos = 3 # total number of photos to take
capture_delay = 3 # delay between taking photos
countdown = 3 # countdown for each photo
res_w = 800 # width of camera resolution (max is 2592)
res_h = 480 # height of camera resolution (max is 1944)
text_size = 60 # size of annotated text
text_color = '#fff' # colour of annotated text
bg_color = '#000' # colour of annotated text background
test_server = 'www.google.com' # server location to check for network
reset_delay = 5
save_path = '/home/pi/captures/'
instruction_path = '/home/pi/github/photobooth/'

# get pygame ready
pygame.init()
res_w = 800 # width of camera resolution (max is 2592)
res_h = 480 # height of camera resolution (max is 1944)
img = pygame.display.set_mode((res_w,res_h), pygame.FULLSCREEN)
screen = pygame.display.get_surface()
pygame.mouse.set_visible(False)


#############################
# functions
#############################
def fireUp():
    leds.off()
    # show image about pressing the button
    print('Push the button instruction')
    displayInstructions(instruction_path + 'button_push.png')
    yellow_button.wait_for_press() # wait for the button to be pressed
    print('Button pressed')
    displayInstructions(instruction_path + 'countdown_explanation.png')
    sleep(5)
    displayInstructions(instruction_path + 'get_posed.png')
    sleep(5)
    clearInstructions()
    sleep(1)
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
        # photo loop starts
        for x in range(1,total_photos + 1):
            count = 3
            for i in range(1,countdown + 1):
                camera.annotate_text = '{}...'.format(count)
                sleep(1)
                count = count - 1
            camera.annotate_text = ''
            print('Taking photo {} - '.format(x) + timestamp + '-{}.jpg'.format(x))
            camera.capture(save_path + timestamp + '-{}.jpg'.format(x))
            sleep(1)
    finally:
        resetCamera() # reset camera

def resetCamera():
    displayInstructions(instruction_path + 'all_done.png')
    leds.value = (1,0,0)
    sleep(1)
    leds.value = (1,1,0)
    sleep(1)
    leds.value = (1,1,1)
    sleep(1)
    print('Resetting...')
    leds.blink(n=3)
    sleep(reset_delay)
    fireUp()


def displayInstructions(instruction_file): # load, convert and display the instructions file
    img = pygame.image.load(instruction_file).convert()
    screen.blit(img,(0,0))
    pygame.display.flip() # updates the whole screen

def clearInstructions():
    screen.fill( (0,0,0) ) # fill screen with black
    pygame.display.flip()

def closeEverything():
    camera.close()
    pygame.quit()


fireUp()

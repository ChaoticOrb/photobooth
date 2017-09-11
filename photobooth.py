
#!/usr/bin/env python

#############################
# photobooth.py
# created by ChaoticOrb
#############################
from picamera import PiCamera, Color
import pygame
import sys
import socket
from time import sleep
from datetime import datetime
from gpiozero import Button, LED, LEDBoard
from signal import pause

#############################
# variables setup
#############################
camera = PiCamera()

# hardware
big_button = Button(17)
leds = LEDBoard(27, 22, 5, 19) # red, red, red, green
total_photos = 3 # total number of photos to take
capture_delay = 3 # delay between taking photos
countdown = 3 # countdown for each photo
res_w = 800 # width of screen resolution
res_h = 480 # height of screen resolution
text_size = 60 # size of annotated text
text_color = '#fff' # colour of annotated text
bg_color = '#000' # colour of annotated text background
reset_delay = 5
save_path = '/home/pi/captures/'
instruction_path = '/home/pi/github/photobooth/'
test_server = 'www.google.com'

# get pygame ready
pygame.init()
img = pygame.display.set_mode((res_w,res_h), pygame.FULLSCREEN)
screen = pygame.display.get_surface()
pygame.mouse.set_visible(False)


#############################
# functions
#############################
def checkNetwork():
    try:
        host = socket.gethostbyname(test_server)
        s = socket.create_connection((host, 80), 2)
        return True
        fireUp()
    except:
        confirmation = input('Network connection not available, do you want to continue?')
        if confirmation == 'y':
            fireUp()
        else:
            pygame.exit()
            sys.exit()


def fireUp():
    try:
        leds.off()
        sleep(1)
        leds.value = (0,0,0,1) # green led on
        print('Push the button instruction')
        displayInstructions(instruction_path + 'button_push.png')
        big_button.wait_for_press()
        print('Button pressed')
        displayInstructions(instruction_path + 'countdown_explanation.png')
        sleep(5)
        displayInstructions(instruction_path + 'get_posed.png')
        sleep(5)
        clearInstructions()
        sleep(1)
        camera.vflip = False # change if camera is mounted upside down
        camera.resolution = camera.MAX_RESOLUTION
        camera.start_preview(resolution=(res_w, res_h))
        print('Camera preview turned on')
        takePhotos()
    except:
        print('FireUp failed to launch - exiting')
        sys.exit(1)

def takePhotos():
    try:
        leds.value = (1,0,0,0) # first red led whilst taking photos
        timestamp = datetime.now().strftime('%d%m%Y-%H%M%S') # create datetime for file naming
        camera.annotate_foreground = Color(text_color)
        camera.annotate_background = Color(bg_color)
        camera.annotate_text_size = text_size
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
        camera.stop_preview()
        resetCamera()

def resetCamera():
    leds.value = (0,1,0,0) # first two red leds after photos finished
    print('All done')
    displayInstructions(instruction_path + 'all_done.png')
    sleep(6)
    leds.value = (0,0,1,0) # all red leds after photos finished
    print('Resetting...')
    displayInstructions(instruction_path + 'resetting.png')
    sleep(reset_delay)
    fireUp()

def displayInstructions(instruction_file): # load, convert and display the instructions file
    img = pygame.image.load(instruction_file).convert()
    screen.blit(img,(0,0))
    pygame.display.flip() # updates the whole screen

def clearInstructions():
    screen.fill( (0,0,0) ) # fill screen with black
    pygame.display.flip()

# start photobooth
checkNetwork()

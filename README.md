# Readme for Photobooth
# photobooth
Photo booth programme using a Raspberry Pi and picamera.

This was put together to be used as a DIY wedding photo booth to avoid the ridiculous costs of hiring a DLSR in a box. It did the job on three different events in the end and was great fun.

## components and parts
* **raspberry pi** - this was built with a [Pi Zero](https://www.raspberrypi.org/products/pi-zero-w/) W but you could easily use a Raspberry Pi 3. Having built in wifi makes set up and running it much easier. I used it with Raspbian Jessie on a 64GB Micro SD card.

* **Pi Camera Module v2** - the [second version](https://www.raspberrypi.org/products/camera-module-v2/) of the Pi Camera module with a Pi Zero cable. [Read the docs](https://picamera.readthedocs.io/en/release-1.13/)

* **Powered USB hub** - if you get one like this [7 port one](https://thepihut.com/products/7-port-usb-hub-for-the-raspberry-pi) you can power the Pi as well as using a mouse, keyboard, USB powered screen and flash drive.

* **HDMI Screen** - I used this little [5inch 800x480 TFT display](https://www.amazon.co.uk/dp/B013JECYF2) as I wanted something that could be powered by USB and didn't need to be that big. I didn't use the touch screen but that could be handy.

* **battery pack** - instead of using a wall socket which was going to be unlikely to be available I decided to use a [big fat 16000mAh battery pack](https://www.modmypi.com/raspberry-pi/power-1051/power-banks-and-hubs-/power-bank-16000mah-5v-2a-usb-portable-power-supply/?limit=100) that was more than capable of powering the pi and the screen from the two power ports. I didn't ever run out or even run low on power and it was running for at least 8 hours quite happily.

* **USB drive** - for backing up captured images, just make sure it's big enough.

* **Keyboard** - I used SSH and VNC for most development but nothing quite beats a connected keyboard for quickly sorting things out. I also took a [small wireless keyboard](https://www.amazon.co.uk/gp/product/B00T2SJUWA/ref=od_aui_detailpages00?ie=UTF8&psc=1) for onsite trouble shooting but rarely needed to use it. Connecting it up was painless though so seems useful to have around.

* **Mouse** - optional but makes life easier, the wireless keyboard I had also had a little touchpad which did the job nicely.

* **Lighting** - as you are using what is basically a mobile phone camera that doesn't do low light particularly well the more light the better. Obviously some lovely sunlight would be best but I also used artificial light in the form of an [led light panel similar to this one](https://www.amazon.co.uk/VILTROX-Adjusted-Temperature-Brightness-3300K-5600K/dp/B0719R1YY4).

* **Buttons** - if you don't go with the touch screen or keyboard control option then some physical buttons are probably the way forward. I decided on a [big arcade button](https://www.modmypi.com/adafruit-industries/components-and-parts/buttons/arcade-button-30mm-translucent-red) to make it obvious how to start the camera. I also had another button to trigger a full shutdown on the raspberry pi, this was triggered by the 'shutdown.py' script that launched at boot and waited for a 10 second button hold to powerdown the pi.

* **Breadboard** - you may choose to solder everything together but I went for a middle ground of soldering wires to buttons but still used a breadboard for connections to the Pi Zero as I wasn't fully confident with soldering directly to the board. Since then the [Zero WH](https://www.raspberrypi.org/blog/zero-wh/) has been released which would be a nice alternative too.

* **LEDs** - useful for highlighting different stages in the programme and just looking for interesting.

* **USB to TTL Serial Cable** - I can't describe how useful having a direct connection to the pi is. For troubleshooting and for killing running applications this is priceless and foolproof. I used the [Adafruit guide](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview) for getting it fired up, just note that if the pi is already powered don't plug in the power connector on the serial cable!

* **Wires and other paraphernalia** - there will be much of this but you can decide what you want.

* **case/box** - mine went from a cardboard shoe box during testing and when I was writing the programme and ended up in a simple laser cut box. It had 6mm ply on the sides and rear door with a 1.5mm front panel that had the screen and camera mounted in it.

## usage
The basics of the photobooth were:

1. Power up the pi
1. On boot a [cron job](https://thepihut.com/blogs/raspberry-pi-tutorials/34930820-running-things-regularly-cron) launches the shutdown.py script and the photbooth.py
1. Once loaded the photobooth script waits for the big button press, then shows the instructions using pygame and gives a countdown to trigger the camera.
1. The camera then takes 3 photos each with a countdown beforehand
1. Each photo is saved with a timestamp
1. To backup the photos in case of sd card failure an rsync copies new files over to the external usb file every 5 minutes
1. Every 15 minutes if there was a network connection, [dropbox uploader](https://github.com/andreafabrizi/Dropbox-Uploader) was used to push the images to Dropbox and a QR code on the photobooth case sent people over to view the images

## issues
There weren't many issues (other than my weak python skills) but the main one I had was killing pygame once it was up and running in full screen mode. This meant that once everything launched at boot I had to SSH in or use the serial connection to kill the python program.

## credit and useful links
* The [Noun Project](https://thenounproject.com) was awesome for simple icons used in the instructions: [Lens](https://thenounproject.com/icon/802832),[Circuit](https://thenounproject.com/icon/182003), [Pointing](https://thenounproject.com/icon/976242)

* [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader)

* [Drumminhands Design Photobooth](http://www.drumminhands.com/2014/06/15/raspberry-pi-photo-booth/) - I took so many useful ideas and pointers from here and it helped me fix some terrible python I had scrawled. [Github site](https://github.com/drumminhands/drumminhands_photobooth)

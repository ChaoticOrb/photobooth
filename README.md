# Readme for Photobooth
# photobooth
Photo booth programme using a Raspberry Pi and picamera.

This was put together to be used as a DIY wedding photo booth to avoid the ridiculous costs of hiring a DLSR in a box.

## components and parts
* **raspberry pi** - this was built with a [Pi Zero](https://www.raspberrypi.org/products/pi-zero-w/) W but you could easily use a Raspberry Pi 3. Having built in wifi makes set up and running it much easier. I used it with Raspbian Jessie on a 64GB Micro SD card.
* **Pi Camera Module v2** - the [second version](https://www.raspberrypi.org/products/camera-module-v2/) of the Pi Camera module with a Pi Zero cable. [Read the docs](https://picamera.readthedocs.io/en/release-1.13/)
* **Powered USB hub** - if you get one like this [7 port one](https://thepihut.com/products/7-port-usb-hub-for-the-raspberry-pi) you can power the Pi as well as using a mouse, keyboard, USB powered screen and flash drive.
* **HDMI Screen** - I used this little [5inch 800x480 TFT display](https://www.amazon.co.uk/dp/B013JECYF2) as I wanted something that could be powered by USB and didn't need to be that big. I didn't use the touch screen but that could be handy.
* **USB drive** - for backing up captured images, just make sure it's big enough.
* **Keyboard** - I used SSH and VNC for most development but nothing quite beats a connected keyboard for quickly sorting things out. I'm considering picking up a tiny Bluetooth one for the final working version but a simple USB one does the trick.
* **Mouse** - optional but makes life easier.
* **Lighting** - as you are using what is basically a mobile phone camera that doesn't do low light particularly well you need to have lots of light. Obviously some lovely sunlight would be best artificial light with a simple led bank or led flash is better than nothing.
* **Buttons** - if you don't go with the touch screen or keyboard control option then some physical buttons are probably the way forward. I decided on a [big arcade button](https://www.modmypi.com/adafruit-industries/components-and-parts/buttons/arcade-button-30mm-translucent-red) to make it obvious how to start the camera. I also used a small button to kill the programme if there were issues or keyboard interrupt wasn't playing ball (I had issues making pygame close at times).
* **Breadboard** - you may choose to solder everything together but I went for a middle ground of soldered wires but still used a breadboard for connections to the Pi Zero.
* **LEDs** - useful for highlighting different stages in the programme and making it all look a bit more interesting.
* **Wires etc**

## usage
tbc

## credit and useful links
https://thenounproject.com/icon/802832
https://thenounproject.com/icon/182003
https://thenounproject.com/icon/976242
https://qrd.by

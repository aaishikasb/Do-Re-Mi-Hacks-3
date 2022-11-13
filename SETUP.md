# SoundCatch - Setup

These are the steps that I have followed to build SoundCatch. To replicate, you can check the sequence below:

## Requirements
1. Raspberry Pi 4/3B+
2. Sound Detection Module (Digital w/ 3 Pins)
3. Jumper Wires (3 F2F)
4. Twilio Account

## Steps
 - Download Raspberry Pi Imager from [this link](https://www.raspberrypi.com/software/).
 - Install the software, choose the OS of your liking. I installed the full version with recommended software separately.
 - Select the drive you want to flash. For Headless setup, before clicking on "Write", click on the gear icon towards the bottom of the tool. This will take you to advanced options.
 - Toggle the SSH option and add username and password compination of your choice. By default it is "pi" and "raspberry" respectively.
 - Hostname by default is raspberry.local, you can change that as well.
 - Configure your WiFi by scrolling down so the Pi connects to your network automatically.
 - Now Write the OS onto the drive and once done, insert the SD Card in the Pi and boot. Wait for some time for the device to connect to the network.
 - In the meantime, make the connections from the Sound Detection Module to Raspberry Pi. The Out Pin should be connected to GPIO 17 or change the audio pin in the program.
 - In the terminal, now SSH into your Pi using the following command (I figured out the IP Address by visiting my router's page, you need to add yours):
   
   `ssh pi@192.168.1.220`
 - Once you have connected to the Pi headlessly, execute the following commands.
   
   ```bash
   sudo apt-get update
   pip install twilio
   pip install RPi.GPIO
   ```
 - Now create a new file and copy the code from [Raspberry-Pi/pi.py](Raspberry-Pi/pi.py)
   
   `nano pi.py`
 - Change the Twilio Credentials and then run the program.
   
   `python pi.py`
   

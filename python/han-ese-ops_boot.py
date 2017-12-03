#!/usr/bin/env python3

## Print a boot message on a Raspberry Pi Sense HAT
## (c) 2017, Marc van der Sluys, HAN University of Applied Sciences, Arnhem, The Netherlands
## 
## MvdS, 2017-09-24: Print boot message and wlan0 IP address
## MvdS, 2017-12-03: Print IP addresses of all network interfaces

from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True


# Print host name and OS (this also gives the Pi some time to obtain an IP address):
import os
uname = os.uname()

sense.show_message("Booting", text_colour=[127,127,127], scroll_speed=0.05)  
sense.show_message(uname[1], text_colour=[127,0,0], scroll_speed=0.07)
sense.show_message("("+uname[0]+")", text_colour=[127,127,127], scroll_speed=0.05)



# Print IP address(es), if any:
import netifaces as ni
ifaces = ni.interfaces()

for iface in ifaces:
    if(iface == 'lo'): continue  # Don't print local loopback
    
    addr = ni.ifaddresses(iface)
    if(ni.AF_INET in addr):
        ip = addr[ni.AF_INET][0]['addr']

        #print(iface+':', ip)
        sense.show_message(iface+':', text_colour=[127,127,127], scroll_speed=0.05)
        sense.show_message(ip, text_colour=[127,0,0], scroll_speed=0.07)

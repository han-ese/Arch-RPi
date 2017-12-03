#!/usr/bin/env python3

## Print a login message on a Raspberry Pi Sense HAT
## (c) 2017, Marc van der Sluys, HAN University of Applied Sciences, Arnhem, The Netherlands
## 
## MvdS, 2017-09-23: Initial version


from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

import os
uname = os.uname()

sense.show_message("Shutting down", text_colour=[127,127,127], scroll_speed=0.04)  # Printing this gives wlan0 some time to obtain an IP address
sense.show_message(uname[1], text_colour=[127,0,0], scroll_speed=0.04)  # Printing this gives wlan0 some time to obtain an IP address
#sense.show_message("Goodbye!", text_colour=[127,127,127], scroll_speed=0.04)  # Printing this gives wlan0 some time to obtain an IP address


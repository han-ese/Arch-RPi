#!/usr/bin/env python3

## Print a login message on a Raspberry Pi Sense HAT
## (c) 2017, Marc van der Sluys, HAN University of Applied Sciences, Arnhem, The Netherlands
## 
## MvdS, 2017-09-23: Initial version


from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True

import getpass
username = getpass.getuser()

sense.show_message("User", text_colour=[127,127,127], scroll_speed=0.05)
sense.show_message(username, text_colour=[127,0,0], scroll_speed=0.07)
sense.show_message("logged in", text_colour=[127,127,127], scroll_speed=0.05)


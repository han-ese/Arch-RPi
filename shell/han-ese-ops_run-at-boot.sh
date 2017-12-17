#!/bin/bash

##  Script to run at boot of a Raspberry Pi with a Sense HAT
##  MvdD, 2017-10-14


# Allow normal users to use the i2c device (sensors):
chmod a+rw /dev/i2c-1

# Print a boot message, including IP address(es), to Sense HAT:
/usr/bin/han-ese-ops_boot.py


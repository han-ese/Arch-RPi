#!/usr/bin/env python3

## Log "weather" measurements from a Raspberry Pi Sense HAT
## (c) 2017, Marc van der Sluys, HAN University of Applied Sciences, Arnhem, The Netherlands
## 
## MvdS, 2017-12-03: Initial version: log timestamp, T, RH and P to stdout


# Get timestamp:
from datetime import datetime
date = datetime.now()
timestamp = date.strftime('%Y-%m-%d %H:%M:%S')

# Get Sense HAT data:
from sense_hat import SenseHat
sense = SenseHat()
temperature = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

# Print line to stdout:
print("%s %0.1f %0.1f %0.1f" % (timestamp, temperature, humidity, pressure) )

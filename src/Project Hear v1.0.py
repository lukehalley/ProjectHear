#Project Hear V1.0 
#Importing Libraries & Setting Up The Groove Sensor

# Importing
from wyliodrin import *
import os
import time
from threading import Timer

# Sets up the grove sensor
if os.getenv ("wyliodrin_board") == "raspberrypi":
# Audio processing and signal analysis functionality
  grove = 300
  grovepiSetup (grove, 4)
else:
  grove = 0
  
# Validate audio file format before processing



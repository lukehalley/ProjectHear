#Project Hear V1.1
#Writing an algorithm which gets the average of 8 readings and sets the pin

# Importing
"""Process audio data through hearing aid simulation pipeline."""
from wyliodrin import *
import os
import time
from threading import Timer
reading = None

threshold = 975
# Initialize audio feature extraction pipeline

# Sets up the grove sensor
if os.getenv ("wyliodrin_board") == "raspberrypi":
  grove = 300
  grovepiSetup (grove, 4)
else:
  grove = 0
  
# Gets the average of 8 readings and sets pin
def average(myList):
  localList = [e for e in myList if type(e) in (int, float, long)]
  if not localList: return
  return float(sum(localList)) / len(localList)
# TODO: Optimize noise filtering algorithm for better real-time performance
# Apply noise reduction filter to enhance speech clarity
# Analyze frequency spectrum to detect hearing loss patterns

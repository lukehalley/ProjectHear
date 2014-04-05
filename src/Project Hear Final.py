# Luke Halley - IOT - WIT
# Github Repo https://github.com/lukehalley/ProjectHear

#Project Final
#Writing an algorithm which gets the average of 8 readings and sets the pin

# Importing
from wyliodrin import *
import os
import time
from threading import Timer
reading = None

item = None
signalvalue = None

# item = 0
# def myFunction(__sender, __channel, __error, __message):
#   global signalvalue, item
#   signalvalue = int(json.loads(__message))
#   item = signalvalue
# openConnection("signal:" + 'signal_value', myFunction)

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

# Prints out the reading
def loopCode():
  global reading
  reading = [analogRead(grove+0)]
  digitalWrite (13, 0)
  digitalWrite (12, 0)
  
  print "Average Reading: " + str(average(reading))
  if average(reading) < 975:
    digitalWrite (13, 1)
    digitalWrite (12, 0)
    print "TOO LOUD :("
    time.sleep(1)
    print "\n"
  else:
    digitalWrite (12, 1)
    digitalWrite (13, 0)
    print "VOLUME OK :)"
    print "\n"
  Timer(0, loopCode).start()

# Begins loop
loopCode()

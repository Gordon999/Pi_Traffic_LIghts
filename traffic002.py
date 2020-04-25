#!/usr/bin/env python3
from gpiozero import LED
from gpiozero import Button
from time import sleep

red1     = LED(14) # RED set 1
amber1   = LED(15) # AMBER set 1
green1   = LED(18) # GREEN set 1
red2     = LED(17)  # RED set 2
amber2   = LED(27)  # AMBER set 2
green2   = LED(22) # GREEN set 2
p_red1   = LED(23)  # pedestrian RED (DON'T WALK) light, set 1
p_green1 = LED(25) # pedestrian GREEN (WALK) light, set 1
p_red2   = LED(10) # pedestrian RED (DON'T WALK)light, set 2
p_green2 = LED(11) # pedestrian GREEN (WALK) light, set 1
p_set1   = LED(24) # Pedestrian WAIT LED 1, acknowledges button pressed
p_set2   = LED(9) # Pedestrian WAIT LED 2, acknowledges button pressed
button1 = Button( 7,pull_up = True,bounce_time= None) # Pedestrian button set 1, switch to gnd
button2 = Button( 4,pull_up = True,bounce_time= None) # Pedestrian button set 2, switch to gnd

# initialise
red2.on()
amber2.off()
green2.off()
red1.on()
amber1.off()
green1.off()
p_red1.on()
p_red2.on()
p_green1.off()
p_green2.off()
p_set1.off()
p_set2.off()

def Light_Sequence(red,amber,green):
   amber.on()
   sleep(2)
   red.off()
   amber.off()
   green.on()
   sleep(10)
   green.off()
   amber.on()
   sleep(2)
   amber.off()
   red.on()
   sleep(1)
   
def PED_button(x): # pedestrian button pressed
   global PED
   PED = 1
   p_set1.on() # WAIT LED 1
   p_set2.on() # WAIT LED 2

def PED_Crossing():
   p_set1.off()
   p_set2.off()
   p_green1.on()
   p_green2.on()
   p_red1.off()
   p_red2.off()
   sleep(3)
   for led in range (0, 10):
      p_green1.off()
      p_green2.off()
      sleep(.1)
      p_green1.on()
      p_green2.on()
      sleep(.1)
   p_green1.off()
   p_green2.off()
   p_red1.on()
   p_red2.on()
   sleep(1)
   
x = 0
PED = 0
button1.when_pressed = PED_button
button2.when_pressed = PED_button

while True:
   # traffic lights set 1 sequence
   Light_Sequence(red1,amber1,green1)
   # pedestrian crossing,if either button has been pressed
   if PED == 1:
      PED_Crossing()
      PED = 0
   # traffic lights set 2 sequence
   Light_Sequence(red2,amber2,green2)
   # pedestrian crossing,if either button has been pressed
   if PED == 1:
      PED_Crossing()
      PED = 0


#!/usr/bin/python
import sys
import time
#from sense_hat import SenseHat
from sense_emu import SenseHat

R = (255, 0, 0)
O = (0,0,0)#(255, 255, 255)
Y = (255, 255, 0)
T = (249, 130, 64)
#C = (255, 255, 255)

pattern = [
    O, O, O, Y, O, O, O, O,
    O, O, O, Y, Y, O, O, O,
    O, O, Y, Y, Y, O, O, O,
    O, O, Y, Y, Y, O, O, O,
    T, O, O, Y, O, O, O, T,
    O, T, T, T, T, T, T, O,
    O, O, T, T, T, T, O, O,
    O, O, O, T, T, O, O, O
]

sense = SenseHat()
#counter = 1000000
#sense.flip_v()
sense.set_rotation(180)
sense.show_message("Happy Diwali!!")
sense.clear()
sense.set_pixels(pattern)

while True:
    sense.flip_h()
    time.sleep(0.05)

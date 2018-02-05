#Atmospheric data collection using Raspberry Pi & Sense Hat Sensors

import time
import datetime
from sense_emu import SenseHat
#from sense_hat import SenseHat

sense = SenseHat()

humidity = sense.get_humidity()
temperature = sense.get_temperature()
pressure = sense.get_pressure()

csv = open("/media/newhd/Raspberry_Pi/SenseHatProjects/Atmospheric_Data_Collection/readings.csv", "a")
event_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
row = "\n"+str(event_time)+","+str(humidity)+","+str(temperature)+","+str(pressure)
csv.write(row)

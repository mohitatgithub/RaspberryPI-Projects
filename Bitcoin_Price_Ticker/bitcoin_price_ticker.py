#Get Bitcoin price updates in real time

#from sense_hat import SenseHat
from sense_emu import SenseHat
import time
import datetime
import csv
import sys
sys.path.append('/media/newhd/Raspberry_Pi/SenseHatProjects/bitcoin-price-api-master')
from exchanges.coindesk import CoinDesk

#Fetching current bitcoin price in INR from CoinDesk API
bitcoin_price = float(round(CoinDesk().get_current_price(currency='INR'),2))

#Fetching last recorded price for comaprision with current price
price_csv = open("/media/newhd/Raspberry_Pi/SenseHatProjects/Bitcoin_Price_Ticker/bitcoin_price.csv", "r")
lastrow = None
for lastrow in csv.reader(price_csv): pass

#Displaying price in Green, Red or White based on fluctuation in price, running on simulator Pi-Sense-Hat Simulator
sense = SenseHat()
if(float(lastrow[1])>bitcoin_price):
    sense.show_message(str(bitcoin_price), text_colour=[0, 255, 0])
elif((float(lastrow[1])<bitcoin_price)):
    sense.show_message(str(bitcoin_price), text_colour=[255, 0, 0])
else:
    sense.show_message(str(bitcoin_price), text_colour=[255, 255, 255])
price_csv.close()

#Writing new price to csv file
price_csv = open("/media/newhd/Raspberry_Pi/SenseHatProjects/Bitcoin_Price_Ticker/bitcoin_price.csv", "a")
event_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
row = "\n"+str(event_time)+","+str(bitcoin_price)
price_csv.write(row)
price_csv.close()

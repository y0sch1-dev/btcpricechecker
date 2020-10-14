import requests
import json
import time

lastPrice = 0
def BtcPrice():
    print(newPrice,"euro")
while True:
    url = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=BTCEUR')
    data = url.json()
    newPrice = float(data['price'])
    if (newPrice != lastPrice):
        lastPrice = newPrice
        BtcPrice()
    time.sleep(15)

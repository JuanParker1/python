import keyboard

from binance.client import Client
#from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

#Declaracion api_key y api_secret_key       Se recogen desde gestion de apis en mi cuenta binance

kapi=''
sapi=''

client=Client(kapi,sapi)
shib_balance=client.get_asset_balance(asset='SHIB')

print(str(shib_balance))



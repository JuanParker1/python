import keyboard

from binance.client import Client
#from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

#Declaracion api_key y api_secret_key       Se recogen desde gestion de apis en mi cuenta binance

kapi='i1C8P7g2qiGDpibFT8cE2YZGwC2lCgzyb6O3Gc7K3ojFIN58QJz3jU9ohHRmW0JU'
sapi='r9XDXllkOwEf2t9PY25ootO7Ph5KC3lvSXnQxeMJmJnB0n1C90FhLVlPfAgFvERF'

client=Client(kapi,sapi)
shib_balance=client.get_asset_balance(asset='SHIB')

print(str(shib_balance))




import requests
from time import sleep
def Endpoint():

    while true:


        return

try:
    r = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/today')

    print (r)
    sleep(15)



except TimeoutException:
    print ('Przekroczono czas polaczenia')








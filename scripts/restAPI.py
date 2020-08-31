import requests


parameters = {'key1':'value1', 'key2':'value2'}

r = requests.get('https://fabrykatestow.pl', params=parameters)
print(r.url)

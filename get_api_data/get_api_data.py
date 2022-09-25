import requests
from pprint import pprint

base_url = 'https://back-coworking.herokuapp.com'
query = '/coworking/623e33a6de3234fd99f632e4'

get_data = requests.get(base_url + query).json()
pprint(get_data)
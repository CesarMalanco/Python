# Author: reDragonCoder

import requests
import pandas as pd
from bs4 import BeautifulSoup

# Making a GET request
def getdata(url):
    r=requests.get(url)
    return r.text

# API key
api='YOUR API KEY'

# Number & country code
number='9852638787'
country='IN'

# Get data function
htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup=BeautifulSoup(htmldata, 'html.parser')
print(soup)
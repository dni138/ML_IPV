import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests

url = 'https://apkpure.com/girlfriend-tracker-by-number/com.androidaplicativos.girlfriendtrackerpro'
response = requests.get(url)

soup = BS(response.text)

print(soup.title)



#<meta name="keywords" content="Girlfriend Tracker, Girlfriend Tracker for android, Girlfriend Tracker android download, Girlfriend Tracker apk, Girlfriend Tracker android apk, Girlfriend Tracker download">

keywords = soup.find_all('meta')
keywords2 = soup.find("meta",  property="keywords")
#keywords = soup.find("meta",  name="keywords")
#print(type(keywords[0]))
print(keywords[0])
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests

url = 'https://apkpure.com/girlfriend-tracker-by-number/com.androidaplicativos.girlfriendtrackerpro'
response = requests.get(url)

soup = BS(response.text)

print(soup.title)


#<div class="content" itemprop="description">Girfriend...
#<meta name="keywords" content="Girlfriend Tracker, Girlfriend Tracker for android, Girlfriend Tracker android download, Girlfriend Tracker apk, Girlfriend Tracker android apk, Girlfriend Tracker download">

all_meta= soup.find_all('meta')
keywords = soup.findAll(attrs={"name":"keywords"}) 
description = soup.findAll(attrs={"name":"description"})
og_image = soup.findAll(attrs={"property":"og:image"})
#internal_description = soup.findAll(attrs={"itemprop"="description"})
print(keywords)
print(description)
print(og_image)
#print(internal_description)
print(soup.prettify())

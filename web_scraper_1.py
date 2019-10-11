import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests

url = 'https://apkpure.com/girlfriend-tracker-by-number/com.androidaplicativos.girlfriendtrackerpro'
response = requests.get(url)

soup = BS(response.text, "lxml")

#all_meta= soup.find_all('meta')
title = soup.title
titleText = title.get_text()
keywords = soup.find(attrs={"name":"keywords"}) 
description = soup.find(attrs={"name":"description"})
description_body = soup.find("div", itemprop="description")
og_image = soup.find(attrs={"property":"og:image"})

print(titleText)
print(keywords)
print(description)
print(description_body)
print(og_image)

#print(soup.prettify())
#print(soup.body)

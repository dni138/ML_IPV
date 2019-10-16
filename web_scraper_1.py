import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests
import urllib.request

# List with google queries I want to make
desired_google_queries = ['com.facebook.phone']

for query in desired_google_queries:
    # Constracting http query
    url = 'https://apkpure.com/search?q=' + query
    # For avoid 403-error using User-Agent
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    response = urllib.request.urlopen( req )
    html = response.read()
    print(html)
    # Parsing response
    soup = BS(html, 'html.parser')
    # Extracting number of results
    resultStats = soup.find(id="resultStats").string
    print(resultStats)

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

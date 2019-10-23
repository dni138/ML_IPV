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
    # Parsing response
    print(html)
    soup = BS(html, 'html.parser')
    # Extracting number of results
    title = soup.title
    titleText = title.get_text()
    keywords = soup.find(attrs={"name":"keywords"}) 
    description = soup.find(attrs={"name":"description"})
    description_body = soup.find("div", itemprop="description")
    og_image = soup.find(attrs={"property":"og:image"})
    search_res = soup.find('div', id = 'search-res').find_all('a', href=True)

    for href in search_res:
        print(href['href'])
    print(titleText)
    #print(keywords)
    print(description)
    print(description_body)
    print(og_image)
    #print(search_res)

#getting screenshots
screenshots = []
for link in soup.findAll('a', {'class': 'mpopup'}):
    try:
       screenshots.append(link['href'])
    except KeyError:
        pass
print(screenshots)

# Important comment: alt text is usually app Title + screenshot number. Give no additional info, so not included.
# Same with Icon title and alt text

# ------------------ OCR
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#getting text from image
def ocr_core(filename):
  
    text = pytesseract.image_to_string(Image.open(filename))
    return text

text_from_screenshots = ocr_core("screenhot_girlfriend.jpg")
print(ocr_core(text_from_screenshots))

#tesseract /Users/paulabarmaimon/Desktop/IPV/ML_IPV/screenhot_girlfriend.jpg out
#im = Image.open("screenhot_girlfriend.jpg")
#im.show()
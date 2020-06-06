import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests
import urllib.request
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def parse_html_request(desired_queries, url):
    '''
    A fucntion that returns a list of html parsed BeautifulSoup objects.

    Input: Desired list of queries (queries are strings represnting appids), suffix url

    Output: List of soup objects from the desired queries
    '''
    soup = []
    for query in desired_queries:
        # Constracting http query
        total_url = url + query
        # For avoid 403-error using User-Agent
        req = urllib.request.Request(total_url, headers={'User-Agent' : "Magic Browser"})
        response = urllib.request.urlopen( req )
        html = response.read()
        # Parsing response
        soup.append(BS(html, 'html.parser'))

    return soup

def grab_info(soup_objects, appids):
    '''
    Grab and format specific pieces of data from soup objects into json lines

    Important comment: alt text is usually app Title + screenshot number. Give no additional info, so not included.
    Same with Icon title and alt text

    Input: list of soup objects, list of (strings) appids

    Output: JSON lines containing appid, title, keywords, description, description_body, and og_image
    '''
    all_data = []
    for soup_object, appid in zip(soup_objects, appids):
        data = {}
        data['title'] = soup_object.title.get_text()
        data['keywords'] = soup_object.find('meta', attrs={"name":"keywords"}) 
        data['description'] = soup_object.find(attrs={"name":"description"})
        data['description_body'] = soup_object.find("div", itemprop="description")
        data['og_image'] = soup_object.find(attrs={"property":"og:image"})
        screenshots = []
        for link in soup_object.findAll('a', {'class': 'mpopup'}):
            try:
                screenshots.append(link['href'])
            except KeyError:
                pass
        data['screenshots'] = screenshots
        data['appid'] = appid
        all_data.append(data)
    
    return all_data

#getting text from image
def ocr_core(filename):
  
    text = pytesseract.image_to_string(Image.open(filename))
    return text


#Main method
if __name__ == '__main__':
    desired_queries = ['com.facebook.phone'] #'com.androidaplicativos.girlfriendtrackerpro'
    soup_list = parse_html_request(desired_queries, 'https://apkpure.com/search?q=')
    new_queries = []
    for soup_object, appid in zip(soup_list, desired_queries):
        search_res = soup_object.find('div', id = 'search-res').find_all('a', href=True)
        for href in search_res:
            if appid in href['href']:
                new_query = href['href']
                break
        new_queries.append(new_query)

    desired_soup = parse_html_request(new_queries, 'https://apkpure.com')

    data = grab_info(desired_soup, desired_queries)

    print(data[0]['description_body'])            
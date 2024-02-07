import requests
from typing import List
from bs4 import BeautifulSoup as bs


def topic_url_list() -> List[str]:
    '''
    Returns a list of urls to scrape
    '''
    URL = 'https://learn.microsoft.com/en-us/power-bi/guidance/'
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254"}
    
    # List of topics to include
    INCLUDE = {'Power BI guidance', 'Transform and shape data', 'Data modeling', 'DAX', 'Power BI reports'}


    page = requests.get(url=URL, headers=HEADERS)

    soup = bs(page.text, 'lxml')
    links = soup.findAll(class_='has-external-link-indicator')

    links = [URL+a['href'] for a in links if a.parent.parent.parent.h2.text in INCLUDE ]
    
    return links

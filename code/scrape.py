import requests
from typing import List
from functools import reduce
from bs4 import BeautifulSoup as bs

class DocScrapper:
    def __init__(self) -> None:
        self.URL = 'https://learn.microsoft.com/en-us/power-bi/guidance/'
        self.HEADERS = {"User-Agent": "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254"}
        self.INCLUDE = {'Power BI guidance', 'Transform and shape data', 'Data modeling', 'DAX', 'Power BI reports'}


    def topic_url_list(self) -> List[str]:
        '''
        Returns a list of urls to scrape
        '''
        # Extracting urls to crawl
        links = [ a['href'] for a in bs(requests.get(url=self.URL, headers=self.HEADERS).text, 'lxml').findAll(class_='has-external-link-indicator') if a.parent.parent.parent.h2.text in self.INCLUDE ]

        return links


    def url_to_doc(self, url: str) -> None:
        # TODO: convert html to markdown
        page = reduce(lambda x,y: x+y, map(lambda x: str(x), filter(lambda x: x.name!='div' and x.name!='h2' and x.name!='h3', bs(requests.get(self.URL+url, headers=self.HEADERS).text, 'lxml').find('div', class_='content').contents)))

        return page
    
    def gen_doc(self):
        # TODO: generate documentation topic_url_list+url_to_doc
        pass


print(DocScrapper().url_to_doc('report-page-tooltips'))
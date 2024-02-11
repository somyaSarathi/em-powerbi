from functools import reduce
from typing import List

import requests
from bs4 import BeautifulSoup as bs
from markdownify import markdownify as md

class DocScrapper:
    def __init__(self) -> None:
        self.URL = 'https://learn.microsoft.com/en-us/power-bi/guidance/'
        self.HEADERS = {"User-Agent": "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254"}

        # List of documentations to scrape
        self.DESIRED_TOPICS = {'Power BI guidance', 'Transform and shape data', 'Data modeling', 'DAX', 'Power BI reports'}

        self.session = requests.Session()


    def topic_url_list(self) -> List[str]:
        '''
        Returns a list of urls to scrape
        '''
        response = self.session.get(url=self.URL, headers=self.HEADERS)
        response.raise_for_status()

        # Extract page content
        page_content = response.text
        
        # Extract all URLs present in the page
        urls = bs(page_content, 'lxml').select('a.has-external-link-indicator')

        # Filtering desired urls
        filtered_urls = [ url['href'] for url in urls if url.parent.parent.parent.h2.text in self.DESIRED_TOPICS ]

        return filtered_urls
    

    def url_to_doc(self, url: str) -> None:
        '''
        Scrapes the provided webpage into a markdown file
        '''
        # Requesting page content 
        # - Customised for each URLs
        if url.startswith('/en-us/'):
            response = self.session.get('https://learn.microsoft.com'+url, headers=self.HEADERS)
        elif url.startswith('..'):
            url = url[3:]
            response = self.session.get(url='https://learn.microsoft.com/en-us/power-bi/'+url, headers=self.HEADERS)
        else:
            response = self.session.get(url=self.URL+url, headers=self.HEADERS)
        response.raise_for_status()

        # Extracting desired session
        soup = bs(response.text, 'lxml')
        content_div = soup.find('div', class_='content')

        # Removing unwanted chunks
        content_div.find('div').decompose()
        content_div.find('div').decompose()
        content_div.find('nav').decompose()

        # Document content 
        article = ''
        for tag in content_div:
            if tag == '\n' or tag.name == 'img':
                continue
            elif tag.name == 'h2' or tag.name == 'h3':
                if tag.text == 'Related content':
                    break
                tag = '---'
            article += str(tag) + '\n'
        
        # Creating documents
        with open(f'./doc/{url.split("/")[-1]}.md', 'w', encoding='utf-8') as doc:
                doc.write(md(article))

    
    def generate_docs(self) -> None:
        '''
        Scrapes links and creates documents
        '''
        urls = self.topic_url_list()

        for url in urls:
            self.url_to_doc(url)

        return
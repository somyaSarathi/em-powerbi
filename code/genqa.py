from typing import List

import json

import os
from dotenv import load_dotenv

from datetime import datetime

import google.generativeai as genai


class GenerateQuestions:
    def __init__(self) -> None:
        # Configure API
        load_dotenv()
        genai.configure(api_key=os.environ['GENAI_API_KEY'])

        # Set up model
        self.model = genai.GenerativeModel('gemini-pro')

        # Prompt tempalate
        with open('./data/prompt.txt', 'r') as prompt:
            self.prompt = prompt.read()
        
        # Documentation links for the model to refer.
        self.urls = [
            'https://learn.microsoft.com/en-us/power-bi/guidance/power-query-folding',
            'https://learn.microsoft.com/en-us/power-bi/guidance/power-query-background-refresh',
            'https://learn.microsoft.com/en-us/power-bi/guidance/power-query-referenced-queries',
            'https://learn.microsoft.com/en-us/power-bi/transform-model/dataflows/dataflows-introduction-self-service',
            'https://learn.microsoft.com/en-us/power-bi/guidance/star-schema',
            'https://learn.microsoft.com/en-us/power-bi/guidance/import-modeling-data-reduction',
            'https://learn.microsoft.com/en-us/power-bi/guidance/relationships-one-to-one',
            'https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many',
            'https://learn.microsoft.com/en-us/power-bi/guidance/relationships-bidirectional-filtering',
            'https://learn.microsoft.com/en-us/power-bi/guidance/relationships-troubleshoot',
            'https://learn.microsoft.com/en-us/power-bi/guidance/relationships-active-inactive',
            'https://learn.microsoft.com/en-us/power-bi/guidance/directquery-model-guidance',
            'https://learn.microsoft.com/en-us/power-bi/guidance/composite-model-guidance',
            'https://learn.microsoft.com/en-us/power-bi/guidance/report-separate-from-model',
            'https://learn.microsoft.com/en-us/power-bi/guidance/report-page-tooltips',
            'https://learn.microsoft.com/en-us/power-bi/guidance/report-drillthrough',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-error-functions',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-avoid-converting-blank',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-avoid-avoid-filter-as-filter-argument',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-column-measure-references',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-divide-function-operator',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-countrows',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-selectedvalue',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-variables',
            'https://learn.microsoft.com/en-us/dax/best-practices/dax-avoid-avoid-filter-as-filter-argument'
        ]

        return
    
    def response(self, urls: str) -> str:
        return self.model.generate_content(
            self.prompt%urls,
            generation_config=genai.types.GenerationConfig(
                temperature=1,
                top_p=0.7,
                max_output_tokens=2000
            )
        ).text[8:-3]

    def generateJson(self, urls: List[str] = None) -> None:
        '''
        Generates and formats the question into JSON
        - Creates only 50 questions.
        '''
        # Check argument type
        if urls is None:
            urls = self.urls
        
        if not(isinstance(urls, List)):
            raise ValueError(f'expected a List of urls("https://...") instead recieved {type(urls)}')
        
        if not urls:
            raise ValueError(f'expectd a List of urls("https://...") instead recieved an EMPTY List')
        
        if not(all(isinstance(url, str) for url in urls)):
            raise ValueError(f'expected a List of urls("https://...")')
        
        if not(any(url.startswith('https://') for url in urls)):
            raise ValueError(f'expected a List of urls("https://...") instead recieved a string')
        

        # List of json
        questions: List[str] = []

        for i in range(4, 26, 5):
            prompt_urls = ''
            for j in range(i-5, i+1):
                prompt_urls += '    - ' + urls[j] + '\n'
            questions += json.loads( self.response(prompt_urls) )['questions']
        
        
        questions = {
            'date': int(datetime.now().strftime('%Y%m%d')),
            'questions': questions
        }
        with open('./data/questions.json', 'w') as f:
            json.dump(questions, f, indent=4)
    

if __name__ == '__main__':
    GenerateQuestions().generateJson()
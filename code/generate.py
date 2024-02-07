import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API
genai.configure(api_key=os.environ['GENAI_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

# Prompt
prompt = '''
Generate 10 MCQ related to Power BI based on following instructions.

Instructions:
1. All questions must be based on relevant sources.
2. The questions must be senario based, hence avoid direct questions.
3. Do not repeat repeat or generate similar questions.
4. The questions must be based on:
    - Query Folding,
    - Power Query,
    - Power BI Optimization,
    - dataflows best practice,
    - star schema,
    - data reduction techniques, 
    - Power BI data modeling and 
    - DAX.
5. generate 5 easy questions, 3 medium questions and 2 hard questions out of 10.
6. hard questions must be multi-choice and medium questions must be senario based.
7. Format the response in JSON as shown bellow.

Output:
```json
{
    "qustions": [
        {
            "question": "question statement",
            "A": "option A",
            "B": "option B",
            "C": "option C",
            "D": "option D",
            "correct": ["A"],
            "difficulty": "easy"
        },
        {
            "question": "question statement",
            "A": "option A",
            "B": "option B",
            "C": "option C",
            "D": "option D",
            "correct": ["A", "B"],
            "difficulty": "hard"
        }
    ]
}
```
'''

# Generating response
response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(
        temperature=0.2,
        top_p=0.7,
        max_output_tokens=1020
    )
)

with open('questions.json','w') as f:
    f.write(response.text[8:-3])
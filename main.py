
import re
import os 
import time
import sys
import openai

from dotenv import load_dotenv 
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


def get_gpt_response(prompt):
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=[{"role": "user", "content": prompt}])
    response = chat_completion.choices[0].message.content

    return response 


question = "Which of these is youngest animal?"

curation1 = "A cat is here"
curation2 = "A chick is here"
curation3 = "A dinosaur is here" 

prompt_with_curation = f"""
{question}
(1) {curation1}
(2) {curation2}
(3) {curation3}
What is the answer? Please respond with a single number.  
"""


response = get_gpt_response(prompt_with_curation)
print("agent's response") 
print(response)
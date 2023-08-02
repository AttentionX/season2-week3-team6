
import re
import os 
import time
import sys
import openai

from dotenv import load_dotenv 
load_dotenv()

from img2text import Image2Text

openai.api_key = os.environ['OPENAI_API_KEY']

def get_gpt_response(prompt):
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=[{"role": "user", "content": prompt}])
    response = chat_completion.choices[0].message.content

    return response 


question = "Which of these is the youngest animal?"
curation_prompt = "Please describe this picture to me."

img2text = Image2Text()
curation1 = img2text.blip2(imgUrl="assets/cat.jpg", prompt=curation_prompt)
curation2 = "A chick is here"
curation3 = "A dinosaur is here" 

prompt_with_curation = f"""
{question}
(1) {curation1}
(2) {curation2}
(3) {curation3}
What is the answer? Please respond with a single number.  
"""

print("final prompt")
print(prompt_with_curation)

response = get_gpt_response(prompt_with_curation)
print("agent's response") 
print(response)
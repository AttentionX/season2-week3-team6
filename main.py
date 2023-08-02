
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


question = "Which of these is not edible?"
 
curation_prompt = "Please describe this picture to me."
img2text = Image2Text()
curation1 = img2text.blip2(imgUrl="assets/Q3/answer1.png", prompt=curation_prompt)
curation2 = img2text.blip2(imgUrl="assets/Q3/answer2.JPG", prompt=curation_prompt)
curation3 = img2text.blip2(imgUrl="assets/Q3/answer3.jpg", prompt=curation_prompt)

prompt_with_curation = f"""
    Choose the most appropriate choice as the correct answer to the question from among the three choices.
    There are three different choices and one question. Your answer should be the number of the most appropriate choice.
    Let's think step by step. First, you should read the question. Second, you should read the choices. Then, you should make a score how appropriate each choice is as the answer to the question. Finally, you should choose the most appropriate choice as the answer to the question.
    Although you think none of the choices are appropriate or you are unsure about the answer, you should still choose the most appropriate choice as the answer to the question.
   
    Here are some examples of a question, choices and answer:
   
    <Example1>
    Question: Which of these is not an animal?
    choice 1: The rice is on the spoon.
    choice 2: There is a deer which has two horns.
    choice 3: The bird is standing on the branch.
    Answer : 1
   
    <Example2>
    Question: Which of the characters is not using a computer?
    choice 1: The cat on the chair is using a computer with a mouse.
    choice 2: The man is chatting with his friends on the computer.
    choice 3: The cute bee is flying around the flowers.
    Answer : 3
   
    <Example3>
    Question : Which of these is not edible?
    choice 1: The baked chicken is on the plate.
    choice 2: The glasses are on the newspapers on the table.
    choice 3: The red strawberries are on the plate.
    Answer : 2
   
    <Example4>
    Question : Which of the following is not a painting?
    choice 1: The real camera photo of two puppies on the top of the mountain.
    choice 2: The oil painting of a horse's head.
    choice 3: The artwork depicting World War II.
    Answer : 1
   
    <Example5>
    Question : Which of the images does not include letters?"
    choice 1: Yes
    choice 2: No
    choice 3: Yes
    Answer : 2
   
    <Example6>
   
    Here is a question and choices for you to answer:
    Question : {question}
    choice 1: {curation1}
    choice 2: {curation2}
    choice 3: {curation3}
    Answer :
    """ 

print("final prompt")
print(prompt_with_curation)

response = get_gpt_response(prompt_with_curation)
print("agent's response") 
print(response)
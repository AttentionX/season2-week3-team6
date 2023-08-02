import os
from dotenv import load_dotenv
import requests
import replicate

load_dotenv()

# Replicate set
replicate_api_key = os.getenv('REPLICATE_API_KEY')
r = replicate.Client(api_token=replicate_api_key)

class Image2Text:
    def blip2(self, imgUrl, prompt=None, isWeb=None):
        if(prompt):
            if(isWeb):
                output = r.run(
                    "andreasjansson/blip-2:4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608",
                    input={"image": imgUrl, "question" : prompt}
                )
                return output
            else:
                output = r.run(
                    "andreasjansson/blip-2:4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608",
                    input={"image": open(imgUrl, "rb"), "question" : prompt}
                )
                return output
        else:
            if(isWeb):
                output = r.run(
                    "andreasjansson/blip-2:4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608",
                    input={"image": imgUrl}
                )
                return output
            else:
                output = r.run(
                    "andreasjansson/blip-2:4b32258c42e9efd4288bb9910bc532a69727f9acd26aa08e175713a0a857a608",
                    input={"image": open(imgUrl, "rb")}
                )
                return output
    
    

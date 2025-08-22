from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI()
response = client.models.list()
model_list = [model.id for model in response.data]
for item in model_list:
    print(item)
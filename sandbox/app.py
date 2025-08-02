from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "Write a 3 sentence bed time horror story about AI."
        }
    ]
)

print(completion.choices[0].message.content)
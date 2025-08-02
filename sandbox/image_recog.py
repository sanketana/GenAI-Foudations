from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "user", "content": "What do you see in the attached image?"},
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png"
                }
            ]
        }
    ]
)

print(response.output_text)
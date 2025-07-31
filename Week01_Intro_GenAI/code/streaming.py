from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Tell me brief history of modern Generative AI in 100 words",
        },
    ],
    stream=True,
)

print("Streaming response:")
for chunk in stream:
    if chunk.choices[0].delta.content is not None:  # Only prints if there's actual content (some chunks are just metadata)
        print(chunk.choices[0].delta.content, end="", flush=True)  # end="": Prevents automatic line breaks, flush=True: Forces immediate output (makes streaming visible)
print()  # Add a newline at the end
from openai import OpenAI
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv()

# Initialize the client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Function to encode image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Vision API example
# Note: You'll need to provide an actual image path
image_path = "path/to/your/image.jpg"  # Replace with actual image path

try:
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encode_image(image_path)}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300,
    )
    
    print(response.choices[0].message.content)
    
except FileNotFoundError:
    print("Please provide a valid image path in the image_path variable")
except Exception as e:
    print(f"Error: {e}") 
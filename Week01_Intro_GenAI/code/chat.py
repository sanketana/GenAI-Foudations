#!/usr/bin/env python3
"""
Minimalistic OpenAI Chat Program
Simple command-line chat using OpenAI's latest SDK.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("🤖 OpenAI Chat (type 'quit' to exit)")
print("-" * 30)

while True:
    # Get user input
    user_input = input("\nYou: ").strip()
    
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    if not user_input:
        continue
    
    # Add user message to history
    messages.append({"role": "user", "content": user_input})
    
    # Get AI response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500
    )
    
    ai_response = response.choices[0].message.content
    print(f"AI: {ai_response}")
    
    # Add AI response to history
    messages.append({"role": "assistant", "content": ai_response}) 
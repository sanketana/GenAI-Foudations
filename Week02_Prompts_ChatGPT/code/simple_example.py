"""
Simple System Prompts Example
Week 02: Prompts and ChatGPT

A basic demonstration of system prompts with OpenAI API.
"""

import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI()

def chat_with_system_prompt(system_prompt, user_message):
    """Simple function to chat with a system prompt"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Example 1: Basic helpful assistant (generic)
basic_prompt = "You are a helpful assistant."

# Example 2: Specific expert assistant
expert_prompt = """
You are a senior software engineer with 10+ years of experience in Python and web development.
You specialize in helping developers write clean, efficient, and maintainable code.
Always provide practical examples and explain your reasoning.
"""

# Example 3: Educational assistant with boundaries
educational_prompt = """
You are a programming tutor for beginners. Your role is to explain programming concepts in simple terms.

Your teaching style:
- Use analogies and real-world examples
- Break down complex concepts into simple steps
- Be patient and encouraging
- Avoid jargon unless necessary

Important: You can explain programming concepts but cannot write complete applications or solve homework problems.
"""

# Test the different prompts
if __name__ == "__main__":
    print("🚀 Simple System Prompts Example")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        exit(1)
    
    # Test question
    question = "What is a function in programming?"
    
    print(f"\n❓ Question: {question}")
    print("\n" + "="*50)
    
    # Test with basic prompt
    print("\n🤖 Basic Assistant Response:")
    print("-" * 30)
    response = chat_with_system_prompt(basic_prompt, question)
    print(response)
    
    # Test with expert prompt
    print("\n👨‍💻 Expert Engineer Response:")
    print("-" * 30)
    response = chat_with_system_prompt(expert_prompt, question)
    print(response)
    
    # Test with educational prompt
    print("\n📚 Programming Tutor Response:")
    print("-" * 30)
    response = chat_with_system_prompt(educational_prompt, question)
    print(response)
    
    print("\n✅ Notice how each system prompt changes the AI's response style and focus!") 
    
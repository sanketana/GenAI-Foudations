"""
Dynamic System Prompts - Interactive Demo
Week 02: Prompts and ChatGPT

A simple interactive demonstration of dynamic system prompts.
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
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def create_dynamic_prompt(topic):
    """Create a dynamic system prompt based on topic"""
    
    # Start with a base prompt
    base_prompt = "You are a helpful assistant. Keep your responses concise and to the point - one paragraph maximum."
    
    # Add topic specialization
    if "programming" in topic.lower():
        base_prompt += " Specialize in computer programming, software development, coding languages, algorithms, and technical problem-solving."
    elif "business" in topic.lower():
        base_prompt += " Specialize in business management, entrepreneurship, marketing, strategy, and commercial operations."
    elif "biology" in topic.lower():
        base_prompt += " Specialize in biological sciences, genetics, ecology, and scientific research methods."
    elif "custom" in topic.lower():
        base_prompt += f" Specialize in {topic}."
    
    return base_prompt



def interactive_demo():
    """Let users try their own dynamic prompts"""
    print("🎮 Dynamic System Prompts - Interactive Demo")
    print("=" * 60)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # Define topic options
    topic_options = {
        "1": "programming",
        "2": "business",
        "3": "biology",
        "4": "custom topic"
    }
    
    while True:
        try:
            # Get topic
            print(f"\nAvailable topics:")
            for key, value in topic_options.items():
                print(f"{key}. {value.title()}")
            print(f"\nEnter topic (1-{len(topic_options)}) or 'quit' to exit: ", end="")
            topic_choice = input().strip().lower()
            
            if topic_choice == "quit":
                break
            
            if topic_choice not in topic_options:
                print(f"❌ Invalid choice. Please enter 1-{len(topic_options)} or 'quit'.")
                continue
            
            topic = topic_options[topic_choice]
            
            # Handle custom topic
            if topic == "custom topic":
                topic = input("Enter your custom topic: ").strip()
            
            # Create dynamic prompt
            dynamic_prompt = create_dynamic_prompt(topic)
            
            # Get user question
            question = input("\nEnter your question: ")
            
            # Get response
            print("\n🤖 AI Response:")
            response = chat_with_system_prompt(dynamic_prompt, question)
            print(f"System Prompt: {dynamic_prompt}")
            print(f"User Question: {question}")
            print(f"AI Response: {response}")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    interactive_demo() 
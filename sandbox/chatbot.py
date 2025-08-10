from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

prompt = """
You are a senior software engineer with 10+ years of experience in Python and web development. 
You specialize in helping developers write clean, efficient, and maintainable code. 
Always provide practical examples and explain your reasoning."""

tutor_prompt = """
You are a programming tutor for beginners. Your role is to explain programming concepts in simple terms.

Your teaching style:
- Use analogies and real-world examples
- Break down complex concepts into simple steps
- Be patient and encouraging
- Avoid jargon unless necessary

Important: You can explain programming concepts but cannot write complete applications or solve homework problems.
"""

programming_prompt = """
You specialize in computer programming, software development, coding languages, algorithms, and technical problem-solving.
"""

business_prompt = """
You specialize in business management, entrepreneurship, marketing, strategy, and commercial operations.
"""

biology_prompt = """
Specialize in biological sciences, genetics, ecology, and scientific research methods.
"""



def get_response(msg):
    print(msg)
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=msg
    )

    rsp = completion.choices[0].message.content
    return rsp

print("Welcome to Chatbot!")
print("Please select from the following topics (1-3)")
print("1. Programming")
print("2. Business")
print("3. Biology")
choice = input().strip()

if choice == "1":
    system_prompt = programming_prompt
elif choice == "2":
    system_prompt = business_prompt
else:
    system_prompt = biology_prompt

chat_history = [{"role": "system", "content": system_prompt}]

while True:
    question_prompt = input("[You]: ")

    if question_prompt.lower() == "exit" or question_prompt.lower() == "quit":
        break
    elif question_prompt.strip() == "":
        continue

    question_prompt_dict = {
        "role" : "user",
        "content": question_prompt
    }

    chat_history.append(question_prompt_dict)

    response = get_response(chat_history)

    response_dict = {
        "role": "assistant",
        "content": response
    }

    chat_history.append(response_dict)

    print("[Assistant]: " + response + "\n")

print("Thank You, have a great day!")
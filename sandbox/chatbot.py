from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

chat_history = []

print("Welcome to Chatbot, How may I help you today")

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


    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=chat_history
    )

    response = completion.choices[0].message.content

    response_dict = {
        "role": "assistant",
        "content": response
    }

    chat_history.append(response_dict)

    print("[Assistant]: " + response + "\n")

print("Thank You, have a great day!")
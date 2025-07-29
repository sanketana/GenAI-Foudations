from openai import OpenAI
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Initialize the client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Create an assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    model="gpt-4-1106-preview",
    tools=[{"type": "code_interpreter"}]
)

# Create a thread
thread = client.beta.threads.create()

# Add a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# Run the assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Wait for the run to complete
while True:
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    
    if run_status.status == 'completed':
        break
    elif run_status.status == 'failed':
        print("Run failed")
        break
    
    time.sleep(1)

# Retrieve messages
messages = client.beta.threads.messages.list(thread_id=thread.id)

# Print the assistant's response
for message in messages.data:
    if message.role == "assistant":
        print("Assistant:", message.content[0].text.value)
        break 
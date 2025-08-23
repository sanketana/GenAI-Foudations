# S178 Batch Weekly Log

---

## Week 1 - Intro to GenAI (19-July)

### Topics Covered
- OpenAI Playground setup
- Prompt Parameters
- Temperature, Top-P, Top-K etc
- Roles of AI users
- Git / Github Overview

### Homework
- Experiment playing around with Prompt Parameters like Temperature, Max Token, Top-P, Top-K with OpenAI Playground
- You can make use of examples provided in the classwork notes here: [Understanding LLM Parameters](https://github.com/sanketana/GenAI-Foudations/blob/main/Week01_Intro_GenAI/notes.md#understanding-llm-parameters)

---

## Week 2 - Simple OpenAI Chatbot (26-July)

### Topics Covered
- venv (Virtual Environment)
- OpenAI SDK
- Environment variables for storing API keys
- load_dotenv

### Homework
- Debug and test the code developed in the class
- Try other API available on the getting started page
- This includes Vision API code and tool calling code
- You can make use of examples provided in the OpenAI documentation here: [OpenAI Quickstart Guide](https://platform.openai.com/docs/quickstart?api-mode=responses)

---

## Week 3 - OpenAI Chatbot (with history) (2-August)

### Topics Covered
- Configuring Environment variables
- Using Load Dot Env
- Passing Messages List in API call
- Maintaining Conversation history / Context

### Homework
- Extend the Chatbot exercise to add following features:
  - User Preferences: Allow users to set their name and preferred conversation style
  - Temperature Control: Add a setting to control response creativity (0.0 = focused, 1.0 = creative)
  - Response Length: Max Token parameter to control the token length
  - Optional: Learn and Use Tiktokeniser to provide the summary of tokens consumed during the conversation

---

## Week 4 - OpenAI Chatbot (with System Context) (10-August)

### Topics Covered
- Abstraction using Function (def keyword)
- Message Roles: user, assistant, system
- Defining a System prompt
- Creating a Dynamic System Prompt

### Homework
- Modify the chatbot to create 2 responses from different GPT models using the same user prompt and compare the results (e.g., gpt-4 vs gpt-4.1).
- Add an additional question to the user to select an appropriate model for the task at hand, e.g.,
  - "Do you want a faster, cheaper model or a slower, more accurate one?"
  - Based on the choice, route the request to the selected model.
- Let the user enter a custom system prompt before starting the conversation, and see how it changes the chatbot's behavior.

---

## Week 5 - Introduction to Streamlit

### Topics Covered
- Origin of Streamlit
- Need for Streamlit
- Key Design Philosophies
- Developed Simple Chatbot using Streamlit
- Covered Requirements.txt concepts

### Homework
- Try this super short code-along Streamlit tutorial on Youtube
- https://youtu.be/D0D4Pa22iG0?si=WCJT6rNma923gTiE

---

## Week 6 - Streamlit Chatbot (23-August)

### Topics Covered
- Streamlit + OpenAI Integration
- Git and Github Concepts
- Deployment on Streamlit Community Server

### Homework
- Complete the rest of the ChatBot features including Side navbar, Model selector, Temperature Selector, Export and Clear chat
- Link: https://github.com/sanketana/GenAI-Foudations/tree/main/Week03_Streamlit_UI/code

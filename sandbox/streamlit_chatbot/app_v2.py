# ENHANCED VERSION OF app.py - OpenAI Integration with Conversation History
# 
# KEY ENHANCEMENTS FROM app.py:
# 1. Added OpenAI API integration (imports, client setup, environment loading)
# 2. Added system prompt for context
# 3. Implemented real AI responses instead of echo
# 4. Added conversation history management with system message
# 5. Modified message display loop to skip system message
# 6. Updated title and removed unnecessary UI elements

import streamlit as st
# NEW: OpenAI imports for API integration
from openai import OpenAI
from dotenv import load_dotenv

# NEW: Environment setup for API key
load_dotenv()
client = OpenAI()

# NEW: System prompt to define AI assistant behavior
#system_prompt = "You are a helpful assistant"

# NEW: Function to get AI response from OpenAI API
def get_response(msg, model, temperature):
    #print(msg)
    completion = client.chat.completions.create(
        model=model,
        messages=msg,
        temperature=temperature
    )
    rsp = completion.choices[0].message.content
    print(system_prompt)
    return rsp

st.set_page_config(page_title="Chatbot", page_icon="💬")
# ENHANCED: Updated title to be more descriptive

with st.sidebar:
    st.header("AI Settings")
    model = st.selectbox(
        "Choose AI Model:",
        ["gpt-4", "gpt-3.5-turbo", "gpt-4-turbo-preview"],
        help="Different models have different capabilities"
    )

    temperature = st.slider(
        "Temperature: ",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Lower = more factual, Higher = more creative"
    )

    system_prompt = st.text_area(
        "System Prompt: ",
        value="You are a helpful assistant",
        height=100
    )

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.messages = [{"role": "system", "content": system_prompt}]
        st.rerun()

    

st.title("My first Streamlit ChatBot")
# REMOVED: st.write("My first Streamlit window") - unnecessary UI element

# ENHANCED: Creating session state with system message included
if "messages" not in st.session_state:
    # NEW: Initialize with system message for context
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# ENHANCED: Display history - skip system message (index 0) to show only user/assistant messages
for m in st.session_state.messages[1:]:  # CHANGED: [1:] instead of [:] to skip system message
    # display mesages
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

#text = st.text_input("How may I help you?")
prompt = st.chat_input("Type your message....")

if prompt:
    st.session_state.messages.append({"role": "user" , "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # ENHANCED: Get real AI response instead of echo
    # OLD: bot_reply = f"Echo: {prompt}"
    # NEW: Call OpenAI API with full conversation history
    bot_reply = get_response(st.session_state.messages, model, temperature)

    st.session_state.messages.append({"role": "assistant" , "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# REMOVED: Commented out button code that was unused





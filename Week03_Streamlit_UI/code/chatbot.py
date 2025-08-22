# OpenAI Integration with Conversation History

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Environment setup for API key
load_dotenv()
client = OpenAI()

def get_response(msg, model, temperature):
    """Get AI response from OpenAI API"""
    completion = client.chat.completions.create(
        model=model,
        messages=msg,
        temperature=temperature
    )
    rsp = completion.choices[0].message.content
    print(system_prompt)
    return rsp

st.set_page_config(page_title="Chatbot", page_icon="💬")

# Sidebar configuration
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

    # Create chat export text
    chat_text = ""
    if "messages" in st.session_state and len(st.session_state.messages) > 1:
        for msg in st.session_state.messages[1:]:  # Skip system message
            chat_text += f"{msg['role'].title()}: {msg['content']}\n\n"
    
    # Export chat button
    st.download_button(
        label="Export Chat",
        data=chat_text,
        file_name="chat_export.txt",
        mime="text/plain",
        disabled=len(chat_text) == 0
    )

st.title("Streamlit OpenAI ChatBot")

# Initialize session state with system message
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# Display conversation history (skip system message)
for m in st.session_state.messages[1:]:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Chat input
prompt = st.chat_input("Type your message....")

if prompt:
    # Add user message to conversation
    st.session_state.messages.append({"role": "user" , "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    bot_reply = get_response(st.session_state.messages, model, temperature)

    # Add assistant response to conversation
    st.session_state.messages.append({"role": "assistant" , "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)





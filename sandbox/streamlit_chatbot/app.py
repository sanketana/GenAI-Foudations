import streamlit as st

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("My first Streamlit App")
st.write("My first Streamlit window")


# Creating session state with history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Diplaying the history based on the content of messages list
for m in st.session_state.messages:
    # display mesages
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

#text = st.text_input("How may I help you?")
prompt = st.chat_input("Type your message....")

if prompt:
    st.session_state.messages.append({"role": "user" , "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    bot_reply = f"Echo: {prompt}"

    st.session_state.messages.append({"role": "assistant" , "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

#if st.button("Send") and text:
#    st.write("You said", text)
# Simple OpenAI Chat

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [🚀 Setup](#setup)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

Minimalistic command-line chat using OpenAI's latest SDK.

## Setup

1. Install dependencies:
```bash
pip install openai python-dotenv
```

2. Create `.env` file:
```bash
cp env_template.txt .env
# Edit .env and add your OpenAI API key
```

3. Run:
```bash
python chat.py
```

## Usage

- Type your message and press Enter
- Type 'quit' to exit
- Conversation history is maintained automatically

That's it! 🚀 

## 🛠️ Prerequisites

- Python 3.8 or higher
- An OpenAI account and API key ([get yours here](https://platform.openai.com/account/api-keys))
- Internet connection

## 📁 File Structure

- `chat.py` — Main chat application script
- `env_template.txt` — Template for your environment variables file
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project is a minimalistic command-line chat app using OpenAI's latest SDK. Here's how it works:

1. **Environment Setup**: Loads your OpenAI API key from a `.env` file using `python-dotenv`.
2. **OpenAI Client**: Initializes the OpenAI client with your API key.
3. **Conversation Loop**: 
   - Prompts you for input (type your message and press Enter).
   - Maintains a conversation history so the AI remembers the context.
   - Sends your message (and the history) to OpenAI's GPT model (`gpt-3.5-turbo`).
   - Prints the AI's response.
   - Type `quit` to exit the chat.

✨ The code is simple, readable, and easy to extend for your own experiments! Happy chatting! 🤖 

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 💡 **Change the System Prompt:** Edit the `messages` list in `chat.py` to change the assistant's personality or instructions.
- 🤖 **Switch Models:** Try using a different OpenAI model by changing the `model` parameter in the code.
- 📝 **Save Conversation History:** Add functionality to save the chat history to a file.
- 🌐 **Add a GUI:** Build a simple web or desktop interface using frameworks like Streamlit or Tkinter.
- 🔒 **Error Handling:** Improve error messages and handle network/API issues gracefully.

Feel free to experiment and make it your own! 
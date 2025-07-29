# Simple OpenAI Chat

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 Configuring API Keys](#-configuring-api-keys)
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

## 🔑 Configuring API Keys

Your code needs access to your OpenAI API key to work, but we don't want to hardcode it directly in the source code (that would be like leaving your house key under the doormat!). Instead, we use **environment variables** - think of them as secret notes that your computer can read but aren't stored in your code files.

The code expects to find your API key in an environment variable called `OPENAI_API_KEY`. You have two ways to set this up:

1. **Using a `.env` file** (recommended for beginners) - A simple text file that stores your secrets
2. **Setting it manually** in your terminal/command prompt - More advanced but gives you more control

This project uses a `.env` file to securely store your OpenAI API key and any other sensitive configuration values. The `.env` file should be placed in the same directory as your code.

**Example `.env` file:**
```env
OPENAI_API_KEY=your-openai-api-key-here
```

- Never share your `.env` file or commit it to version control (e.g., GitHub).
- Use the provided `env_template.txt` as a starting point.

### Loading Environment Variables in Python

This project uses the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from the `.env` file automatically. In `chat.py`, the following code loads your variables:

```python
from dotenv import load_dotenv
load_dotenv()
```

You can then access your API key (or any other variable) using:

```python
import os
api_key = os.getenv('OPENAI_API_KEY')
```

This approach keeps your secrets out of your code and makes it easy to manage different environments (development, production, etc.).

### Manual Environment Variable Setup (Alternative Method)

If you prefer to set environment variables manually instead of using a `.env` file, here's how to do it:

#### On macOS/Linux:

**Set an environment variable:**
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

**Show a specific environment variable:**
```bash
echo $OPENAI_API_KEY
```

#### On Windows:

**Set an environment variable (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-openai-api-key-here
```

**Set an environment variable (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-openai-api-key-here"
```

**Show a specific environment variable (Command Prompt):**
```cmd
echo %OPENAI_API_KEY%
```

**Show a specific environment variable (PowerShell):**
```powershell
echo $env:OPENAI_API_KEY
```

**Note:** If you set environment variables manually, you can remove the `.env` file and the `load_dotenv()` call from your code, as Python will automatically pick up system environment variables.

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
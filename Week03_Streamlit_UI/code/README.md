# Streamlit OpenAI ChatBot

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 Configuring API Keys](#-configuring-api-keys)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

A modern web-based chatbot built with Streamlit and OpenAI's API, featuring conversation history, customizable AI settings, and chat export functionality.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file:
```bash
cp env_template.txt .env
# Edit .env and add your OpenAI API key
```

3. Run the Streamlit app:
```bash
streamlit run chatbot.py
```

4. Open your browser to the URL shown in the terminal (usually http://localhost:8501)

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

This project uses the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from the `.env` file automatically. In `chatbot.py`, the following code loads your variables:

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

### Main Features:
- **Chat Interface**: Type your messages in the chat input at the bottom
- **Model Selection**: Choose between different OpenAI models (GPT-4, GPT-3.5-turbo, etc.)
- **Temperature Control**: Adjust creativity vs. factualness with the temperature slider
- **System Prompt**: Customize the AI's behavior and personality
- **Clear Chat**: Reset the conversation history
- **Export Chat**: Download your conversation as a text file

### How to Use:
1. Launch the app with `streamlit run chatbot.py`
2. Configure AI settings in the sidebar (optional)
3. Type your message in the chat input
4. Press Enter to send and receive a response
5. Continue the conversation - history is maintained automatically
6. Use "Clear Chat" to start fresh or "Export Chat" to save your conversation

That's it! 🚀 

## 🛠️ Prerequisites

- Python 3.8 or higher
- An OpenAI account and API key ([get yours here](https://platform.openai.com/account/api-keys))
- Internet connection
- Web browser (Chrome, Firefox, Safari, etc.)

## 📁 File Structure

- `chatbot.py` — Main Streamlit application with chat interface
- `requirements.txt` — Python dependencies
- `env_template.txt` — Template for your environment variables file
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project is a web-based chatbot using Streamlit and OpenAI's latest SDK. Here's how it works:

1. **Environment Setup**: Loads your OpenAI API key from a `.env` file using `python-dotenv`.
2. **Streamlit Configuration**: Sets up the web interface with page title and icon.
3. **Sidebar Controls**: 
   - Model selection dropdown (GPT-4, GPT-3.5-turbo, etc.)
   - Temperature slider for controlling response creativity
   - System prompt text area for customizing AI behavior
   - Clear chat and export chat buttons
4. **Session State Management**: Maintains conversation history across page reloads
5. **Chat Interface**: 
   - Displays conversation history with proper chat message styling
   - Handles user input through Streamlit's chat input widget
   - Processes messages through OpenAI API
   - Updates conversation history with responses
6. **OpenAI Integration**: Uses the latest OpenAI SDK with proper error handling

✨ The code demonstrates Streamlit best practices including session state management, sidebar layouts, and interactive widgets! 

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 💡 **Add Message Roles**: Implement different message types (system, user, assistant) with visual indicators
- 🤖 **Model Comparison**: Add a feature to compare responses from different models side-by-side
- 📝 **Save/Load Conversations**: Add functionality to save conversations to files and load them later
- 🎨 **Custom Themes**: Implement dark/light mode toggle and custom CSS styling
- 🔒 **Enhanced Security**: Add user authentication and rate limiting
- 📊 **Usage Analytics**: Track token usage and conversation statistics
- 🌐 **Multi-language Support**: Add language selection and translation features
- 🔄 **Streaming Responses**: Implement real-time streaming of AI responses
- 📱 **Mobile Optimization**: Improve the interface for mobile devices
- 🎯 **Prompt Templates**: Add pre-built prompt templates for different use cases

Feel free to experiment and make it your own! 

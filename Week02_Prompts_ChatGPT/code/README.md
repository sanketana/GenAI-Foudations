# System Prompts Demo

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 Configuring API Keys](#-configuring-api-keys)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

Interactive demonstrations of system prompts with OpenAI's latest SDK.

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

3. Run either demo:
```bash
# Simple comparison demo
python simple_example.py

# Interactive dynamic prompts demo
python dynamic_prompts.py
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

This project uses the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from the `.env` file automatically. In both demo files, the following code loads your variables:

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

### Simple Example Demo (`simple_example.py`)
- Shows how the same question gets different responses with different system prompts
- Demonstrates basic vs. expert vs. educational prompts
- Perfect for understanding the concept quickly

### Dynamic Prompts Demo (`dynamic_prompts.py`)
- Interactive demo where you choose topics and ask questions
- Shows how system prompts adapt to different domains (Programming, Business, Biology)
- Demonstrates the power of dynamic prompt generation

## 🛠️ Prerequisites

- Python 3.8 or higher
- An OpenAI account and API key ([get yours here](https://platform.openai.com/account/api-keys))
- Internet connection

## 📁 File Structure

- `simple_example.py` — Basic system prompt comparison demo
- `dynamic_prompts.py` — Interactive dynamic system prompts demo
- `env_template.txt` — Template for your environment variables file
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project demonstrates the power of system prompts in AI interactions. Here's how it works:

### Simple Example (`simple_example.py`)
1. **Three Different Prompts**: Shows how the same question gets different responses based on the system prompt
   - Basic: Generic helpful assistant
   - Expert: Senior software engineer with specific expertise
   - Educational: Programming tutor with teaching guidelines
2. **Same Question**: All three prompts answer "What is a function in programming?"
3. **Different Responses**: Each prompt produces a different style and focus of response

### Dynamic Prompts (`dynamic_prompts.py`)
1. **Topic Selection**: Choose from Programming, Business, Biology, or Custom topics
2. **Dynamic Generation**: Creates system prompts based on the selected topic
3. **Interactive Testing**: Ask any question and see how the AI responds based on the topic
4. **Cross-Domain Examples**: Perfect for testing words like "pandas" that have different meanings across domains

### Key Concepts Demonstrated
- **System Prompts**: Instructions that define the AI's role and behavior
- **Context Matters**: How the same question gets different responses based on context
- **Dynamic Generation**: Creating prompts programmatically based on user input
- **Cross-Domain Thinking**: How concepts have different meanings in different fields

✨ The code is simple, readable, and perfect for learning about prompt engineering! 

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 💡 **Add More Topics**: Extend the dynamic prompts demo with more domains like medicine, law, or art
- 🤖 **Experiment with Different Models**: Try using different OpenAI models by changing the `model` parameter
- 📝 **Save Conversations**: Add functionality to save the chat history to a file
- 🌐 **Add a GUI**: Build a simple web interface using Streamlit or Flask
- 🔒 **Improve Error Handling**: Add better error messages and handle API rate limits
- 🎯 **Create Custom Prompts**: Add more sophisticated prompt templates for specific use cases
- 📊 **Compare Responses**: Add functionality to compare multiple responses side by side

Feel free to experiment and make it your own! 
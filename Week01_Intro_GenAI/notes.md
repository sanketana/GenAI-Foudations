# Week 01: Introduction to Generative AI - Instructor Notes

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Key Topics to Cover](#key-topics-to-cover)
- [Discussion Points](#discussion-points)
- [Additional Resources](#additional-resources)
- [Understanding LLM Parameters](#understanding-llm-parameters)
  - [Temperature](#temperature)
  - [Top-p (Nucleus Sampling)](#top-p-nucleus-sampling)
  - [Top-k](#top-k)
  - [Presence Penalty](#presence-penalty)
  - [Applying to a Real Question](#applying-to-a-real-question)
  - [Summary Table](#summary-table)
  - [Playground Experiment Suggestion](#playground-experiment-suggestion)
  - [Final Takeaway](#final-takeaway)
- [System Prompt](#system-prompt)
  - [What is a System Prompt?](#what-is-a-system-prompt)
  - [System Prompt Examples](#system-prompt-examples)
  - [System Prompt vs. User Prompt](#system-prompt-vs-user-prompt)
  - [How to Write Effective System Prompts](#how-to-write-effective-system-prompts)
  - [Advanced System Prompt Techniques](#advanced-system-prompt-techniques)
  - [Real-World Applications](#real-world-applications)
- [Understanding Tokenisation](#understanding-tokenisation)
  - [What are Tokens?](#what-are-tokens)
  - [Token Counting Tools](#token-counting-tools)
  - [Practical Tips](#practical-tips)
- [Understanding Context Window](#understanding-context-window)
  - [What is a Context Window?](#what-is-a-context-window)
  - [Managing Context Window](#managing-context-window)
  - [Practical Examples](#practical-examples)

## Learning Objectives
- Dev Environment Setup
- Account Creation
- Setting up API Keys
- Exploring OpenAI Dashboard and Playground
- [System Prompt](#system-prompt)
- [Understanding Prompt Parameters (Temperature, Top-K, Top-P etc.)](#understanding-llm-parameters)
- [Understanding Tokenisation](#understanding-tokenisation)
- [Understanding Context Window](#understanding-context-window)
- Understanding what Generative AI is
- Overview of different types of generative models
- Current applications and use cases
- Ethical considerations

## Key Topics to Cover
1. Definition of Generative AI
2. Types of generative models (GANs, VAEs, Transformers)
3. Real-world applications
4. Limitations and challenges
5. Ethical implications

## Discussion Points
- How is GenAI different from traditional AI?
- What are the potential risks and benefits?
- How can we use GenAI responsibly?

## Additional Resources
- Research papers on generative models
- Case studies of GenAI applications
- Ethical guidelines for AI development 

---

# Understanding LLM Parameters: 
Temperature, Top-p, Top-k, and Presence Penalty

Large Language Models (LLMs) like ChatGPT offer tunable parameters that significantly influence how responses are generated. Understanding these is key to getting the kind of output you want — whether factual, creative, diverse, or safe.

---

## Temperature

**Controls**: Randomness in the model's output  
**Range**: 0 to 2 (commonly 0.2–1.0)

| Low Temperature (0.2) | High Temperature (1.0) |
|----------------------|------------------------|
| Predictable, factual, deterministic | Creative, vivid, and surprising |

### ✨ Example Prompt:
> "Write a birthday message for my 11-year-old niece who loves Harry Potter."

- **Temp 0.2**:  
  "Happy birthday! I hope you have a magical day filled with joy and fun. Best wishes."

- **Temp 1.0**:  
  "Wishing you a spellbinding birthday, young witch! May your cake be as sweet as a Honeydukes treat and your day more magical than a ride on the Hogwarts Express!"

---

## Top-p (Nucleus Sampling)

**Controls**: How much of the probability mass to consider  
**Range**: 0 to 1

Top-p dynamically selects the smallest set of most probable next tokens whose cumulative probability exceeds `p`.

### 🍦 Ice Cream Analogy

Suppose top 5 flavors ranked by popularity:
1. Vanilla (40%)  
2. Chocolate (30%)  
3. Strawberry (15%)  
4. Pistachio (10%)  
5. Mango (5%)

With `top-p = 0.95`, the model will consider only the top 4 (total = 95%) and **exclude** Mango.  
With `top-p = 0.3`, only Vanilla and Chocolate would be considered.

> ✅ **Use top-p for flexible creativity.**

---

## Top-k

**Controls**: The number of top most likely tokens to sample from  
**Range**: 1 to infinity

With `top-k = 3`, the model **only** chooses from the top 3 most probable tokens — regardless of their actual probabilities.

> ✅ **Use top-k for strict control over randomness.**  
In practice, GPT models often favor `top-p` over `top-k`.

---

## Presence Penalty

**Controls**: How much to discourage using words already mentioned  
**Range**: 0 to 2

- **Low**: May repeat the same ideas or phrases  
- **High**: Encourages introduction of new ideas and vocabulary

### 🧪 Example Prompt:
> "List things to do in Paris."

- **Presence Penalty = 0**:  
  "See the Eiffel Tower, Eiffel Tower light show, Eiffel Tower view…"

- **Presence Penalty = 1.2**:  
  "Visit the Eiffel Tower, explore the Louvre, cruise the Seine, eat croissants…"

---

## Applying to a Real Question

### 🎓 Prompt:
> "Explain photosynthesis to a 12-year-old."

#### 🔥 Temperature
- **Low (0.2)**:  
  "Photosynthesis is the process by which green plants make food using sunlight, water, and carbon dioxide."

- **High (0.9)**:  
  "Imagine plants as tiny chefs! They use sunlight, air, and water to whip up sugar — their energy snack!"

#### 🎲 Top-p
- **Low (0.3)**:  
  "Photosynthesis is when plants make food using sunlight."

- **High (0.95)**:  
  "Plants are like solar panels. They grab sunlight, mix it with water and air, and cook up sugar to grow."

#### 🚫 Presence Penalty
Ask ChatGPT the same question again:

- **Low**:  
  "Photosynthesis is when plants use sunlight to make food. Plants use sunlight to convert water and carbon dioxide…"

- **High**:  
  "Photosynthesis is a special process where plants harness solar energy to create fuel. Instead of eating, they build sugar from sunlight."

---

## Summary Table

| Parameter         | Purpose                            | Low Value                        | High Value                            |
|------------------|------------------------------------|----------------------------------|----------------------------------------|
| **Temperature**   | Controls creativity/randomness     | Safe, factual                    | Creative, varied                       |
| **Top-p**         | Controls probability mass threshold| Basic, common phrasing           | Broader vocabulary, surprises          |
| **Top-k**         | Limits selection to top `k` words  | Predictable, narrow choices      | Unpredictable, wider sampling          |
| **Presence Penalty** | Penalizes repeated concepts     | Repetitive responses             | Encourages fresh ideas                 |

---

## Playground Experiment Suggestion

**Prompt**:
> "Generate five unique business ideas for kids aged 10–13 during summer vacation."

Try two versions in [OpenAI Playground](https://platform.openai.com/playground):

1. `temperature = 0.9`, `top_p = 0.3`, `presence_penalty = 0`
2. `temperature = 0.9`, `top_p = 0.95`, `presence_penalty = 1.2`

Compare how creative and diverse the results become.

---

## Final Takeaway

These parameters aren't just for fun — they shape **tone, style, originality, and clarity**. Whether you're coding, writing a poem, teaching a concept, or brainstorming ideas, tuning them (or understanding how they're tuned) gives you more control over what the model generates.

Would you like a template to use these insights while building prompts or a cheatsheet PDF version?

---

# System Prompt

The system prompt is a special instruction given to a language model that defines its role, behavior, and capabilities for the entire conversation. It's like giving the AI a "job description" that shapes how it responds to all your questions.

---

## What is a System Prompt?

**System Prompt** = Instructions that tell the AI who it is and how to behave.

Think of it as the **"personality"** or **"role"** you're assigning to the AI before starting your conversation.

### 🔑 Key Characteristics
- **Set once** at the beginning of a conversation
- **Invisible to users** (not shown in chat)
- **Persistent** throughout the entire session
- **Influences all responses** from the model

---

## System Prompt Examples

### Example 1: Expert Role
```
You are an expert Python programmer with 10 years of experience. 
You write clean, efficient, and well-documented code. 
Always explain your reasoning and suggest best practices.
```

### Example 2: Educational Assistant
```
You are a patient and encouraging coding tutor. 
Break down complex concepts into simple terms.
Use analogies and examples to help students understand.
Never give complete solutions - guide them to discover answers.
```

### Example 3: Creative Writer
```
You are a creative writing assistant who specializes in science fiction.
You have a vivid imagination and love creating unique worlds and characters.
Your writing style is engaging and descriptive.
```

---

## System Prompt vs. User Prompt

### System Prompt (Background Instructions)
```
Role: Expert data scientist
Style: Professional and analytical
Goal: Help with data analysis projects
```

### User Prompt (Specific Question)
```
"Can you help me analyze this dataset of customer purchases?"
```

### Combined Effect
The AI responds as a professional data scientist would to your specific question about customer data analysis.

---

## How to Write Effective System Prompts

### 1. **Define the Role Clearly**
```
❌ Bad: "Be helpful"
✅ Good: "You are a senior software engineer specializing in web development"
```

### 2. **Specify the Style**
```
❌ Bad: "Write well"
✅ Good: "Use clear, concise language. Include code examples when relevant."
```

### 3. **Set Boundaries**
```
❌ Bad: "Answer everything"
✅ Good: "Only provide information you're confident about. If unsure, say so."
```

### 4. **Include Context**
```
❌ Bad: "Help with coding"
✅ Good: "Focus on Python and JavaScript. Assume the user has basic programming knowledge."
```

---

## Advanced System Prompt Techniques

### 1. **Multi-Role System Prompts**
```
You are a coding mentor who can switch between:
- A patient teacher for beginners
- A code reviewer for intermediate developers
- A technical consultant for advanced projects
Adapt your style based on the user's questions.
```

### 2. **Conditional Instructions**
```
If the user asks about code: Provide working examples
If the user asks about concepts: Use analogies and explanations
If the user asks for debugging: Ask for error messages first
```

### 3. **Output Formatting**
```
Always structure your responses with:
1. Brief answer
2. Detailed explanation
3. Code example (if applicable)
4. Additional resources
```

---

## Real-World Applications

### Code Review Assistant
```
You are a senior software engineer conducting code reviews.
Focus on:
- Code quality and best practices
- Security vulnerabilities
- Performance optimizations
- Readability and maintainability
Provide specific, actionable feedback.
```

### Research Assistant
```
You are a research assistant helping with academic papers.
Your tasks include:
- Summarizing research findings
- Identifying key methodologies
- Suggesting related research
- Formatting citations properly
Always cite sources when possible.
```

### Creative Writing Coach
```
You are a creative writing coach who helps authors develop their stories.
Provide feedback on:
- Character development
- Plot structure
- Dialogue quality
- World-building
Be encouraging but honest in your critiques.
```

---

## System Prompt Limitations

### What System Prompts CAN'T Do
- **Override model training** (can't make it forget basic knowledge)
- **Change core capabilities** (can't make it solve unsolvable problems)
- **Guarantee perfect behavior** (models can still make mistakes)
- **Replace user instructions** (still need clear user prompts)

### What System Prompts CAN Do
- **Set the tone** and style of responses
- **Define expertise areas** and focus
- **Establish boundaries** and limitations
- **Create consistent behavior** patterns
- **Improve response quality** and relevance

---

## Hands-On Exercise

### Exercise: Create Your Own System Prompt

**Step 1**: Choose a role (e.g., tutor, consultant, creative assistant)

**Step 2**: Write a system prompt that includes:
- Role definition
- Style guidelines
- Boundaries
- Output format preferences

**Step 3**: Test it with various questions

**Step 4**: Refine based on the responses

### Example Template
```
You are a [ROLE] with expertise in [AREA].
Your communication style is [STYLE].
You focus on [GOALS].
When responding, always [SPECIFIC BEHAVIOR].
Avoid [LIMITATIONS].
```

---

## Key Takeaways

1. **System prompts** define the AI's role and behavior
2. **Be specific** about expertise, style, and boundaries
3. **Test and refine** your system prompts
4. **Combine** with clear user prompts for best results
5. **Understand limitations** - they can't work miracles
6. **Consistency matters** - good system prompts improve all responses

Mastering system prompts is key to getting the most out of your AI interactions!

# Understanding Tokenisation

Tokenisation is the process of breaking down text into smaller units called "tokens" that language models can understand and process. This is a fundamental concept that affects how we interact with LLMs and manage costs.

---

## What are Tokens?

**Tokens** are the basic units of text that language models process. They can be:
- **Words**: "hello" = 1 token
- **Parts of words**: "understanding" = 3 tokens ("under", "stand", "ing")
- **Punctuation**: "." = 1 token
- **Special characters**: "!" = 1 token
- **Numbers**: "123" = 1 token

### 📊 Token Examples

| Text | Tokens | Count |
|------|--------|-------|
| "Hello world!" | ["Hello", " world", "!"] | 3 |
| "I love pizza" | ["I", " love", " pizza"] | 3 |
| "Understanding" | ["Under", "stand", "ing"] | 3 |
| "123-456-7890" | ["123", "-", "456", "-", "7890"] | 5 |

---

## Why Tokens Matter

### Cost Implications
- **OpenAI charges per token** (both input and output)
- **GPT-4**: ~$0.03 per 1K input tokens, ~$0.06 per 1K output tokens
- **GPT-3.5**: ~$0.0015 per 1K input tokens, ~$0.002 per 1K output tokens

### Performance Impact
- **Longer prompts** = more processing time
- **Context window limits** (e.g., GPT-4: 8K-32K tokens)
- **Memory usage** increases with token count

---

## Tokenisation Rules

### English Text
- **Average**: ~4 characters per token
- **Words**: Usually 1-2 tokens each
- **Common words**: Often 1 token ("the", "and", "is")
- **Rare words**: Split into multiple tokens

### Special Cases
- **Code**: More tokens than plain text
- **Numbers**: Usually 1 token per number
- **Emojis**: 1-3 tokens each
- **Non-English**: Often more tokens per character

---

## Token Counting Tools

### OpenAI Tokenizer
```python
import tiktoken

# Initialize tokenizer
encoding = tiktoken.encoding_for_model("gpt-4")

# Count tokens
text = "Hello, how are you today?"
token_count = len(encoding.encode(text))
print(f"Token count: {token_count}")
```

### Online Tools
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [GPT Calculator](https://gptcalculator.com/)

---

## Practical Tips

### Reducing Token Usage
1. **Be concise**: Remove unnecessary words
2. **Use abbreviations**: "e.g." instead of "for example"
3. **Avoid repetition**: Don't repeat the same information
4. **Structure prompts**: Use clear, direct language

### Example Optimization

**Before** (15 tokens):
> "Could you please help me understand how to write a function that calculates the factorial of a number in Python programming language?"

**After** (8 tokens):
> "Write a Python function to calculate factorial"

---

## Tokenisation Experiment

Try this in the OpenAI Playground:

**Prompt**: "Count the tokens in this sentence: 'The quick brown fox jumps over the lazy dog.'"

**Expected**: The model should explain that this sentence has approximately 8-10 tokens, depending on the specific tokenizer used.

---

## Token Limits by Model

| Model | Context Window | Input Cost/1K | Output Cost/1K |
|-------|----------------|---------------|----------------|
| GPT-4 | 8K-32K tokens | ~$0.03 | ~$0.06 |
| GPT-3.5 | 4K-16K tokens | ~$0.0015 | ~$0.002 |
| Claude-3 | 200K tokens | ~$0.015 | ~$0.075 |

---

## Key Takeaways

1. **Tokens ≠ Characters**: 1 word ≠ 1 token
2. **Cost awareness**: Monitor token usage for budget management
3. **Efficiency**: Shorter prompts save money and time
4. **Limits**: Respect context window boundaries
5. **Tools**: Use tokenizers to estimate costs before API calls

Understanding tokenisation helps you write more efficient prompts and manage your API costs effectively!

---

# Understanding Context Window

The context window (also called context length or token limit) is the maximum number of tokens a language model can process in a single conversation. This includes both the input (your prompt) and output (the model's response).

---

## What is a Context Window?

**Context Window** = The total number of tokens the model can "see" and remember in one conversation.

Think of it as the model's **working memory** - like how much information you can hold in your mind at once while having a conversation.

### 📊 Context Window Examples

| Model | Context Window | Approximate Text |
|-------|----------------|------------------|
| GPT-3.5 | 4K tokens | ~3,000 words |
| GPT-4 | 8K tokens | ~6,000 words |
| GPT-4 Turbo | 128K tokens | ~100,000 words |
| Claude-3 | 200K tokens | ~150,000 words |

---

## How Context Window Works

### Input + Output = Total Context
```
Your Prompt (2K tokens) + Model Response (1K tokens) = 3K tokens used
```

### Conversation Flow
1. **You send a message** → Tokens counted
2. **Model responds** → More tokens added
3. **You reply** → Even more tokens
4. **Total must stay under limit**

### ⚠️ When You Hit the Limit
- **Older messages get "forgotten"** (truncated)
- **Model loses context** from the beginning
- **Conversation quality degrades**
- **You may need to start fresh**

---

## Why Context Window Matters

### Real-World Impact
- **Long documents**: Can't process entire books at once
- **Code reviews**: Limited by file size
- **Research papers**: May need to break into sections
- **Conversations**: Memory fades over time

### Cost Implications
- **Larger context** = Higher cost per request
- **More tokens processed** = More expensive
- **Efficiency matters** for budget management

---

## Managing Context Window

### Strategies for Long Content

#### 1. **Chunking** (Breaking into pieces)
```
Original: 50-page document (20K tokens)
Strategy: Break into 5-page chunks (2K tokens each)
Result: Process 10 separate requests
```

#### 2. **Summarization** (Condensing information)
```
Original: Detailed meeting notes (5K tokens)
Strategy: Summarize key points (500 tokens)
Result: Use summary for context, details as needed
```

#### 3. **Hierarchical Processing**
```
Step 1: Summarize entire document
Step 2: Use summary + specific sections
Step 3: Deep dive into important parts
```

---

## Practical Examples

### Example 1: Code Review
**Problem**: Review a 10K-line codebase

**Solution**:
1. **First pass**: Summarize overall architecture
2. **Second pass**: Review specific modules
3. **Third pass**: Focus on critical functions

### Example 2: Research Paper Analysis
**Problem**: Analyze a 50-page research paper

**Solution**:
1. **Abstract + Introduction**: Get overview
2. **Methodology**: Understand approach
3. **Results**: Focus on key findings
4. **Discussion**: Analyze implications

### Example 3: Long Conversation
**Problem**: Chat history is 15K tokens

**Solution**:
1. **Summarize earlier parts** of conversation
2. **Keep recent context** intact
3. **Reference summary** when needed

---

## Context Window vs. Memory

### What Gets "Forgotten"
- **Older messages** (first in, first out)
- **Less relevant information**
- **Redundant content**

### What Stays Important
- **Recent messages** (last in, last out)
- **Key instructions** from user
- **Critical context** for current task

### Memory Management
```
Context Window: 8K tokens
Current Usage: 7.5K tokens
Available: 500 tokens
Strategy: Summarize or remove old content
```

---

## Context Window Experiment

Try this in the OpenAI Playground:

**Step 1**: Start with a simple question
> "What is machine learning?"

**Step 2**: Ask follow-up questions
> "Can you explain that in more detail?"
> "What are the different types?"
> "How does deep learning fit in?"

**Step 3**: Notice how the model maintains context

**Step 4**: Try a very long conversation and observe when context starts to degrade

---

## Context Window Comparison

| Model | Context Window | Best For | Limitations |
|-------|----------------|----------|-------------|
| **GPT-3.5** | 4K tokens | Short conversations, simple tasks | Limited for long documents |
| **GPT-4** | 8K tokens | Medium complexity, detailed analysis | May struggle with very long texts |
| **GPT-4 Turbo** | 128K tokens | Long documents, complex research | Higher cost per request |
| **Claude-3** | 200K tokens | Book-length content, extensive analysis | Most expensive option |

---

## Optimization Tips

### For Short Context Windows (4K-8K)
1. **Be concise** in your prompts
2. **Summarize** long content first
3. **Focus** on specific questions
4. **Use bullet points** instead of paragraphs

### For Long Context Windows (128K+)
1. **Provide full context** when needed
2. **Include relevant documents** in one request
3. **Ask for comprehensive analysis**
4. **Reference specific sections** by page/line

### General Best Practices
- **Monitor token usage** in your requests
- **Plan your conversation** structure
- **Keep important info** in recent messages
- **Use summaries** for long-term context

---

## Key Takeaways

1. **Context window** = model's working memory limit
2. **Input + output** = total token usage
3. **Older content** gets forgotten when limit is reached
4. **Chunking and summarization** help manage long content
5. **Choose model** based on your context needs
6. **Monitor usage** to avoid hitting limits unexpectedly

Understanding context windows helps you design better prompts and manage long conversations effectively!
# Week 02: Prompts and ChatGPT - Instructor Notes

## Step 1: Choosing a Model

When working with AI models, selecting the right model for your specific use case is crucial. Here's a comparison of different model categories:

| Aspect | Reasoning Models | GPT Models | Large Models | Small Models (Mini/Nano) |
|--------|------------------|------------|--------------|--------------------------|
| **Description** | Specialized models designed for complex logical reasoning and problem-solving | General-purpose language models based on transformer architecture | High-parameter models with extensive capabilities | Compact models optimized for speed and efficiency |
| **Examples** | - Claude 3.5 Sonnet<br>- Claude 3.5 Haiku<br>- GPT-4o with reasoning<br>- Gemini 1.5 Pro<br>- o3-mini | - GPT-4.1<br>- GPT-4o<br>- GPT-4o-mini<br>- GPT-3.5 Turbo<br>- Claude 3.5 Sonnet<br>- Gemini 1.5 Flash | - GPT-4.1 (1.7T+ parameters)<br>- Claude 3.5 Opus<br>- Gemini 1.5 Ultra<br>- o3<br>- PaLM 2 | - GPT-4o-mini<br>- Claude 3.5 Haiku<br>- Gemini 1.5 Nano<br>- Llama 3.1 8B<br>- o3-mini |
| **Use Cases** | - Mathematical problem solving<br>- Code debugging<br>- Logical analysis<br>- Multi-step reasoning tasks<br>- Complex analytical workflows | - Text generation<br>- Conversation<br>- Content creation<br>- General Q&A<br>- Creative writing<br>- Real-time chat | - Complex tasks requiring deep understanding<br>- Research and analysis<br>- High-quality content generation<br>- Advanced reasoning<br>- Enterprise applications | - Real-time applications<br>- Cost-sensitive projects<br>- Simple Q&A<br>- Basic text processing<br>- Edge deployment<br>- Mobile applications |
| **Pros** | - Superior reasoning abilities<br>- Better at complex problem decomposition<br>- More reliable for analytical tasks<br>- Enhanced mathematical capabilities | - Versatile and flexible<br>- Good conversational abilities<br>- Extensive training data<br>- Strong language understanding<br>- Real-time processing | - Most capable and accurate<br>- Better context understanding<br>- Superior performance on difficult tasks<br>- Advanced multimodal capabilities | - Fast response times<br>- Lower costs<br>- Efficient resource usage<br>- Suitable for real-time applications<br>- Lower latency |
| **Cons** | - Often slower response times<br>- Higher computational costs<br>- May be overkill for simple tasks<br>- Limited availability | - Can hallucinate<br>- Limited reasoning in complex scenarios<br>- Context window limitations<br>- Variable performance | - High computational cost<br>- Slower response times<br>- Expensive API calls<br>- Resource intensive<br>- Limited availability | - Limited capabilities<br>- Reduced accuracy<br>- Smaller context windows<br>- Less nuanced understanding<br>- Fewer features |

### 📊 Model Comparison Resources

**[OpenAI Model Comparison Table](https://platform.openai.com/docs/models/compare?model=o3)** - Interactive table with detailed specs, pricing, and performance metrics

### Model Selection Guidelines

**Choose Reasoning Models when:**
- Working on complex analytical problems
- Need step-by-step logical reasoning
- Mathematical or scientific computations
- Code debugging and analysis

**Choose GPT Models when:**
- General conversation and chat
- Content creation and writing
- Simple Q&A tasks
- Creative projects

**Choose Large Models when:**
- High accuracy is critical
- Complex, multi-faceted tasks
- Research and analysis work
- Budget allows for higher costs

**Choose Small Models when:**
- Speed is essential
- Cost is a major constraint
- Simple, straightforward tasks
- Real-time applications
- Limited computational resources

## Step 2: Define System Prompt

### What is a System Prompt?

A system prompt is the foundational instruction that defines an AI model's role, behavior, and capabilities before any user interaction begins. It acts as the "personality" and "job description" for the AI, setting the context and boundaries for all subsequent conversations.



### Why System Prompts Are Critical

**1. Behavior Control:** System prompts establish the AI's personality, tone, and response style

**2. Context Setting:** They provide background information and domain expertise

**3. Safety & Ethics:** They define boundaries and prevent harmful or inappropriate responses

**4. Consistency:** They ensure uniform behavior across all user interactions

**5. Specialization:** They transform a general-purpose AI into a domain-specific expert

### Real-World System Prompt Examples

#### ChatGPT.com (General Assistant)
```
You are ChatGPT, an AI assistant created by OpenAI. You are helpful, creative, clever, and very friendly. You can engage in casual conversation, answer questions, help with writing, analysis, coding, and creative projects. You aim to be helpful while being honest about your limitations.
```

#### Cursor IDE (Code Assistant)
```
You are an expert software developer and coding assistant. You help users write, debug, and optimize code across multiple programming languages. You provide clear explanations, suggest best practices, and help with code reviews. You can analyze code, suggest improvements, and help with debugging issues. Always provide working, production-ready code examples.
```


#### Medical Information Assistant
```
You are a medical information assistant. You can provide general health information and explain medical concepts, but you cannot diagnose conditions or provide treatment advice. Always recommend consulting healthcare professionals for medical decisions. You prioritize accuracy and safety in all responses.
```

### Crafting Effective System Prompts

#### Key Components to Include:

1. **Role Definition:** What is the AI's primary function?
2. **Expertise Level:** What knowledge and skills does it have?
3. **Response Style:** How should it communicate (formal, casual, technical)?
4. **Boundaries:** What should it NOT do?
5. **Context:** What background information is relevant?
6. **Safety Guidelines:** How should it handle sensitive topics?

#### Code Examples

See the complete implementation in the `code/` folder:
- **`system_prompts_demo.py`** - Comprehensive demonstration with multiple system prompt types
- **`simple_example.py`** - Basic examples showing the difference between generic and specific prompts
- **`README.md`** - Detailed documentation and usage instructions

### Best Practices for System Prompt Design

#### 1. **Be Specific and Detailed**
❌ **Poor:** "You are a helpful assistant."

✅ **Good:** "You are a senior software engineer with 15 years of experience in Python, JavaScript, and cloud architecture. You specialize in helping developers build scalable web applications and provide code reviews, debugging assistance, and architectural guidance."

#### 2. **Define Clear Boundaries**
❌ **Poor:** "Help with any questions."

✅ **Good:** "You can help with programming questions, code reviews, and technical discussions. You cannot provide medical advice, legal counsel, or financial recommendations. For those topics, recommend consulting appropriate professionals."

#### 3. **Include Response Format Guidelines**
❌ **Poor:** "Answer questions."

✅ **Good:** "Provide responses in the following format:
- Brief overview of the concept
- Step-by-step explanation with examples
- Common pitfalls to avoid
- Additional resources for learning"

#### 4. **Consider Safety and Ethics**
❌ **Poor:** "Answer anything the user asks."

✅ **Good:** "You are designed to be helpful while maintaining ethical boundaries. You will not assist with harmful activities, provide personal information about individuals, or generate content that could cause harm."

#### 5. **Test and Iterate**
- Start with a basic system prompt
- Test with various user inputs
- Refine based on actual responses
- Consider edge cases and potential misuse

### Common Pitfalls to Avoid

1. **Overly Vague Instructions:** "Be helpful" doesn't provide enough guidance
2. **Conflicting Instructions:** Don't ask for both brevity and comprehensive detail
3. **Missing Boundaries:** Always define what the AI should NOT do
4. **Ignoring Context:** Consider the specific use case and audience
5. **Static Prompts:** Update system prompts based on user feedback and performance

### Advanced Techniques

For advanced system prompt techniques including dynamic prompts and multi-role assistants, see the complete implementation in `code/system_prompts_demo.py`.

---
## Learning Objectives
- Understanding prompt engineering fundamentals
- Mastering effective prompting techniques
- Exploring ChatGPT capabilities and limitations
- Best practices for AI interaction

## Key Topics to Cover
1. What is prompt engineering?
2. Types of prompts (zero-shot, few-shot, chain-of-thought)
3. ChatGPT architecture overview
4. Practical prompting strategies
5. Common pitfalls and how to avoid them

## Hands-on Activities
- Live demonstration of prompt optimization
- Student practice sessions with ChatGPT
- Comparing different prompting approaches
- Troubleshooting common issues

## Discussion Points
- When does prompt engineering work well vs. poorly?
- How to evaluate prompt effectiveness?
- Role of context and specificity in prompts

## Demo Scripts
- Basic prompt examples
- Progressive prompt refinement
- Role-playing prompts
- Technical documentation generation

## Assessment Checkpoints
- Students should demonstrate improved prompt quality
- Understanding of different prompt types
- Ability to critique and improve prompts 


- Choosing a model
  Model types
    - Reasoning models
    - GPT models
    - Large and Small (mini, nano)
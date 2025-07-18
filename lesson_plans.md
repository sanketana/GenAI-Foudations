# 🧭 Phase 1 Curriculum (12-Week Lesson Plan)

**Goal:** Build a working GenAI application using LLM APIs + RAG by Week 12.  

---

## 🔹 Week 1: Introduction to GenAI & Use Cases

**Goal:** Understand the landscape of Generative AI and what’s possible in enterprise/infra settings.  
**Topics:**  
- Generative AI overview  
- LLMs: GPT-4, Claude, Gemini  
- Use cases: Infra, support bots, document summarization  
- Difference between predictive vs generative ML  

**📚 Pre-read:**  
- What is Generative AI? (DeepLearning.AI)  
- OpenAI blog on GPT models  

**💻 In-class hands-on:**  
- Setup: Python / Node.js environment + API keys  
- Call OpenAI API (basic prompt → response)  

**🏠 Homework:**  
- Write 3 prompts that answer a user query. Try tweaking temperature, max_tokens.  

**📌 Weekly milestone:**  
- You’ve made your first GPT-powered text generation app via API!

---

## 🔹 Week 2: Prompt Engineering Basics

**Goal:** Learn to craft and refine prompts with control.  
**Topics:**  
- Prompt structure: system, user, assistant  
- Zero-shot, few-shot, role prompting  
- Parameters: temperature, max tokens, stop  

**📚 Pre-read:**  
- Prompt Engineering Guide (section 1–2)  

**💻 In-class hands-on:**  
- Try zero-shot vs few-shot prompting  
- Summarization, question answering examples  

**🏠 Homework:**  
- Create a prompt template for summarizing any email or blog article.  

**📌 Weekly milestone:**  
- You now understand how prompting affects model behavior.

---

## 🔹 Week 3: Streamlit UI for LLM Apps

**Goal:** Build a basic front-end for your LLM app.  
**Topics:**  
- Intro to Streamlit  
- Building UI: text input, button, output display  
- Integrating OpenAI API with Streamlit  

**📚 Pre-read:**  
- Streamlit official tutorial: https://docs.streamlit.io  

**💻 In-class hands-on:**  
- Build: User inputs question → LLM responds on screen  

**🏠 Homework:**  
- Add a new prompt type: “Rewrite as a professional email”  

**📌 Weekly milestone:**  
- First working LLM app with a UI!

---

## 🔹 Week 4: Embeddings & Semantic Search

**Goal:** Learn how text is embedded into vector space and searched semantically.  
**Topics:**  
- What are embeddings?  
- Use cases: similarity, clustering, search  
- OpenAI Embeddings API  

**📚 Pre-read:**  
- OpenAI Embedding docs  

**💻 In-class hands-on:**  
- Get embeddings of a few text blocks and compute cosine similarity  

**🏠 Homework:**  
- Try semantic similarity on 5 user input phrases and your own data (e.g., FAQ text)  

**📌 Weekly milestone:**  
- You’ve generated embeddings and done similarity search!

---

## 🔹 Week 5: Intro to Vector Databases (ChromaDB)

**Goal:** Store & retrieve text chunks using embeddings.  
**Topics:**  
- What is a vector DB?  
- FAISS vs Pinecone vs ChromaDB  
- CRUD operations in ChromaDB  

**📚 Pre-read:**  
- ChromaDB tutorial on GitHub  

**💻 In-class hands-on:**  
- Build vector DB → add 5 docs → search with a query  

**🏠 Homework:**  
- Load 3 personal or professional PDFs and index them.  

**📌 Weekly milestone:**  
- You’ve built a working vector DB with search!

---

## 🔹 Week 6: Retrieval Augmented Generation (RAG) – Part 1

**Goal:** Combine LLM + vector DB for smarter QA.  
**Topics:**  
- What is RAG and why it matters  
- Simple RAG pipeline (manual)  

**📚 Pre-read:**  
- DeepLearning.AI short course: “RAG with LLMs”  

**💻 In-class hands-on:**  
- Build: query → retrieve from ChromaDB → insert into LLM prompt  

**🏠 Homework:**  
- Add 5 enterprise FAQs and build a RAG app to answer them  

**📌 Weekly milestone:**  
- You’ve built a primitive RAG system!

---

## 🔹 Week 7: RAG – Part 2 + Chunking Documents

**Goal:** Improve document chunking and retrieval quality.  
**Topics:**  
- Chunking strategies: by paragraph, token count  
- Chunk overlap  
- Improving search quality  

**📚 Pre-read:**  
- Read on chunking techniques from LlamaIndex blog  

**💻 In-class hands-on:**  
- Compare performance of small vs large chunking in RAG app  

**🏠 Homework:**  
- Test your chunking approach on a long PDF  

**📌 Weekly milestone:**  
- You’ve improved your RAG app’s accuracy!

---

## 🔹 Week 8: Prompt Templates + OpenAI Functions

**Goal:** Create structured prompts and start tool-calling.  
**Topics:**  
- Prompt templating for context reuse  
- OpenAI function calling (structured outputs)  

**📚 Pre-read:**  
- OpenAI Function Calling docs  

**💻 In-class hands-on:**  
- Build: Ask a question → model returns structured JSON  

**🏠 Homework:**  
- Create 3 functions for summarization, classification, and rephrasing  

**📌 Weekly milestone:**  
- You now have structured responses + tool hooks!

---

## 🔹 Week 9: Integrate External Tools & APIs

**Goal:** Connect your LLM app with real-world data.  
**Topics:**  
- Call weather, finance, or ticket APIs  
- Inject results into prompt  

**📚 Pre-read:**  
- Python Requests + any open API doc  

**💻 In-class hands-on:**  
- Build: “Ask the weather” bot → fetches real-time data + explains it  

**🏠 Homework:**  
- Connect to an API that could be useful in your domain  

**📌 Weekly milestone:**  
- Your LLM app talks to the real world!

---

## 🔹 Week 10: Streamlit App Polish + Layout

**Goal:** Improve app UI/UX for final presentation.  
**Topics:**  
- Streamlit forms, tabs, layout, styling  
- Upload file feature  
- Session states  

**📚 Pre-read:**  
- Streamlit advanced docs (forms, layout)  

**💻 In-class hands-on:**  
- Enhance your RAG UI with sections, upload capability  

**🏠 Homework:**  
- Polish your app UI and flow  

**📌 Weekly milestone:**  
- Your app is ready for a live demo!

---

## 🔹 Week 11: Deployment & Sharing

**Goal:** Put your GenAI app online.  
**Topics:**  
- Deploy to HuggingFace Spaces / Vercel  
- Share with others  

**📚 Pre-read:**  
- HuggingFace Spaces / Vercel deployment guides  

**💻 In-class hands-on:**  
- Deploy your working RAG app live  

**🏠 Homework:**  
- Share your deployed app with a friend or colleague  

**📌 Weekly milestone:**  
- You now have a live GenAI app deployed!

---

## 🔹 Week 12: Final Demo & Wrap-up

**Goal:** Share your work, reflect, and plan next steps.  
**Topics:**  
- Showcase day: each person demos their app  
- Feedback & ideas  
- Intro to what Phase 2 could offer  

**📚 Pre-read:**  
- None (use this week for wrap-up)  

**💻 In-class hands-on:**  
- Demo & feedback session  

**🏠 Homework:**  
- Share a write-up of your app (what it does, why it’s useful)  

**📌 Weekly milestone:**  
- You’ve built and deployed your first GenAI project!
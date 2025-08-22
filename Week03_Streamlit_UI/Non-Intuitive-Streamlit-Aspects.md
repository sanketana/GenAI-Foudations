# Streamlit Concepts for Python Developers

This is where many Python devs feel "huh?" when moving into Streamlit apps. Let's take it in layers.

---

## 1. Concept of `if` in Python (normal)

You already know:

```python
if condition:
    # only run this block if condition is True
```

In Streamlit:
- It's the same — but because Streamlit reruns the whole script top-to-bottom on every user interaction, the `if` blocks get evaluated fresh each time.
- So `if` doesn't just guard code at runtime; it determines what will appear in the UI on that run.

---

## 2. Concept of `with`

In Python, `with` is a context manager. Example:

```python
with open("file.txt") as f:
    data = f.read()
```

- It temporarily enters a context, does the indented code, then exits cleanly (closing the file, releasing resources, etc.).

In Streamlit:

```python
with st.chat_message("user"):
    st.markdown("Hello")
```

- Here, `st.chat_message("user")` creates a chat bubble UI block.
- Everything inside the `with` goes into that bubble.
- When the block ends, Streamlit knows to "close" that bubble.

Think of it like saying:
➡️ "Hey Streamlit, start drawing a bubble… okay now I'm done filling it."

---

## 3. General flow of a Streamlit app

This is the most non-obvious thing for regular Python devs.

👉 **Streamlit scripts rerun from top to bottom every time something changes.**

That means:
- Every button click, text input, slider move, etc. triggers a full rerun of your script.
- The output UI is rebuilt fresh each time.
- Your code is not sitting there "waiting" like in Flask/Django or a chatbot loop.

So how does it remember things like conversation history?
➡️ With `st.session_state`, a special dictionary that persists across reruns.

---

## 4. Non-obvious / non-intuitive things for Python devs

### 🔁 1. The rerun model
- In a normal Python script, code runs once and stops.
- In Streamlit, every interaction reruns the whole file.
- So you don't put `while True:` loops — you trust reruns to handle "interaction".

### 📦 2. `st.session_state` is your memory
- Without it, variables reset every rerun.
- With it, you can persist values like messages, counters, login flags, etc.
- Treat it like a per-user global dictionary.

### 📋 3. Widgets are "declarations" not "procedures"

When you write:

```python
name = st.text_input("Enter your name")
```

- It looks like a function call that returns a value.
- But really, it's declaring a widget in the UI.
- On each rerun:
  - If the user typed something, `name` is that value.
  - If not, it's the default/empty.

So you don't "ask" the widget; you "declare" it, and Streamlit fills in the state.

### 🎨 4. `with` blocks = UI containers
```python
with st.container(): ...
with st.chat_message("assistant"): ...
```
- They're just "draw this stuff inside this UI block".
- Not resources or files, but visual grouping.

### ⏳ 5. Sequential but declarative feel
- The script still runs top-to-bottom sequentially.
- But since the whole script reruns often, your "mental model" shifts:
- Instead of "flow control", you think "what should the UI look like this time?"

### 🔀 6. Conditionals shape UI

For example:

```python
if st.checkbox("Show details"):
    st.write("Here are more details")
```

- Each rerun, the `if` decides whether to render that block.
- The UI can change dynamically like a webpage, but code-wise it's just conditionals.

---

## 5. Putting it together (flow of a chatbot example)

Here's what happens when you type into a chatbot:

1. **App runs from top**: builds the title, renders old messages, shows input box.
2. **You type something + hit enter**.
3. **Streamlit triggers a full rerun**.
4. **On rerun**:
   - It rebuilds old messages (`for m in session_state.messages`).
   - Sees `prompt = st.chat_input(...)` and gets your typed text.
   - Runs the `if prompt:` block → saves message, calls OpenAI, renders reply.
   - Adds reply to `session_state`.
5. **UI is redrawn with new bubbles**.

---

## ✅ Key Takeaway

**The golden rule is**: don't think of Streamlit as a long-running loop. Think of it as redrawing the app from scratch each time, with `session_state` carrying the memory across runs.


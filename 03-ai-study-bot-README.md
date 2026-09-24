# 🎓 AI Study Bot

An interactive LLM-powered study assistant built with Python, the OpenAI
API, and Streamlit.

## ✨ What It Does

Choose a learning level, enter a question, and the Study Bot generates:

-   an explanation adapted to the selected level
-   a simple example
-   a short quiz or practice question

## 🧠 Architecture

``` text
Streamlit UI
    ↓
Python variables
    ↓
OpenAI SDK
    ↓
API
    ↓
LLM
    ↓
Generated response
    ↓
Streamlit UI
```

## ▶️ Run

From the repository root:

``` bash
pip install -r requirements.txt
streamlit run 03-ai-study-bot/study_bot_app.py
```

Make sure `OPENAI_API_KEY` is available in your environment before
running the app.

## 📚 Concepts Practised

-   LLM APIs
-   SDK vs API vs model
-   dynamic prompting
-   environment variables
-   API responses
-   Streamlit widgets
-   connecting a UI to AI application logic

## 🔜 Next Improvements

-   input validation
-   exception handling
-   loading state
-   structured LLM responses
-   conversation history
-   tool calling
-   RAG

# 🎓 AI Study Bot

An interactive LLM-powered study assistant built with **Python, the
OpenAI API, and Streamlit**.

This is the **third project in my AI Engineering Learning Journey** and
my first application that connects a user interface to a hosted large
language model.

------------------------------------------------------------------------

## 🎯 Project Goal

The goal of this project was not simply to call an LLM.

I wanted to understand the complete application flow:

**User → UI → Python → SDK → API → LLM → Response → UI**

I first built the Study Bot as a terminal application and then converted
it into an interactive Streamlit application.

------------------------------------------------------------------------

## ✨ Features

-   🎚️ Select a learning level:
    -   Beginner
    -   Intermediate
    -   Advanced
-   💬 Enter any study question
-   🧠 Generate an explanation adapted to the selected level
-   💡 Generate a simple example
-   📝 Generate a practice question or short quiz
-   🖥️ Display the response through a Streamlit interface
-   🔐 Use an API key supplied through the local environment

------------------------------------------------------------------------

## 🏗️ Architecture

``` text
              USER
                │
                ▼
        ┌──────────────┐
        │  Streamlit   │
        │      UI      │
        └──────┬───────┘
               │
       level + question
               │
               ▼
        ┌──────────────┐
        │    Python    │
        │ application  │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ OpenAI SDK   │
        └──────┬───────┘
               │
               ▼
             API
               │
               ▼
             LLM
               │
               ▼
        Generated answer
               │
               ▼
        ┌──────────────┐
        │  Streamlit   │
        │    output    │
        └──────────────┘
```

------------------------------------------------------------------------

## 🧠 What I Learned

### SDK vs API vs LLM

A major learning outcome was understanding that these are different
components.

``` text
OpenAI Python SDK
       ↓
helps Python communicate with
       ↓
API
       ↓
sends the request to
       ↓
LLM
       ↓
generates the response
```

### Dynamic Prompting

The selected study level becomes part of the instructions sent to the
model.

This allows the same application to adapt its explanation based on user
input.

### Streamlit

The original terminal interaction:

``` text
input() → Python → LLM → print()
```

became:

``` text
Streamlit widgets → Python → LLM → Streamlit output
```

The underlying Python/LLM logic remained similar while the user
interface changed.

------------------------------------------------------------------------

## 🛠️ Technologies

-   Python
-   OpenAI Python SDK
-   OpenAI API
-   Streamlit

------------------------------------------------------------------------

## ▶️ Run Locally

### 1. Install dependencies

From the repository root:

``` bash
pip install -r requirements.txt
```

### 2. Configure your API key

The application expects an `OPENAI_API_KEY` environment variable.

Never place a real API key directly in the source code or commit it to
GitHub.

The repository includes `.env.example` only as a safe configuration
template.

### 3. Start the application

``` bash
streamlit run 03-ai-study-bot/study_bot_app.py
```

Streamlit will start a local web application, normally accessible
through the local address shown in the terminal.

------------------------------------------------------------------------

## 🔐 Security

Never commit:

-   API keys
-   `.env`
-   Streamlit secrets
-   credentials

The root `.gitignore` is configured to exclude local secret files.

------------------------------------------------------------------------

## 🗺️ Current Application Flow

``` text
Select study level
        ↓
Enter question
        ↓
Click "Ask AI"
        ↓
Create dynamic instructions
        ↓
Send API request
        ↓
LLM generates response
        ↓
Extract output text
        ↓
Display in Streamlit
```

------------------------------------------------------------------------

## 🚧 Current Limitations

This is intentionally an early version of the application.

It does not yet include:

-   conversation memory
-   structured model responses
-   external tools
-   document retrieval
-   embeddings/vector search
-   RAG
-   agent orchestration

Those capabilities will be added progressively as I learn each concept.

------------------------------------------------------------------------

## 🛣️ Next Steps

-   [ ] Stronger input validation
-   [ ] API exception handling
-   [ ] Loading/error states
-   [ ] Structured LLM outputs
-   [ ] Conversation history
-   [ ] Tool/function calling
-   [ ] Embeddings and vector search
-   [ ] Document ingestion
-   [ ] Retrieval-Augmented Generation (RAG)
-   [ ] Citations
-   [ ] Agent workflows

------------------------------------------------------------------------

## 🎯 Long-Term Direction

This Study Bot is an early building block toward a larger **AI Research
& Study Agent**.

Rather than replacing this application with a completely different
project, I plan to progressively add the engineering concepts I learn
and document why each component is needed.

# 🤖 AI Engineering Learning Journey

> A hands-on journey from Python APIs and structured data to LLM
> applications, RAG, tool calling, and AI agents.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![OpenAI
API](https://img.shields.io/badge/OpenAI-API-black)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

## 👋 About This Repository

This repository documents my practical AI engineering learning journey.

Rather than jumping directly into high-level AI frameworks, I am
building each component step by step so I understand **what the code is
doing, why it works, and how the different parts of an AI application
connect together**.

My learning approach is:

**Learn → Practise → Build → Debug → Improve → Repeat**

The long-term goal is to evolve these foundations into a complete **AI
Research & Study Agent**.

------------------------------------------------------------------------

## 🗺️ Journey So Far

  ------------------------------------------------------------------------
  Stage             Project           Main Concepts      Status
  ----------------- ----------------- ------------------ -----------------
  01                GitHub Profile    REST APIs, GET,    ✅ Completed
                    Finder            JSON, status       
                                      codes, error       
                                      handling           

  02                Structured Quiz   Dictionaries,      ✅ Completed
                    Board             lists, loops,      
                                      structured data    

  03                AI Study Bot      LLM API,           ✅ Working
                                      prompting, SDK,    
                                      Streamlit          

  04                Reliability       Validation,        🔜 Next
                                      exceptions, API    
                                      errors             

  05                Structured LLM    Machine-readable   🔜 Planned
                    Outputs           AI responses       

  06                Tool Calling      Giving the AI      🔜 Planned
                                      controlled tools   

  07                Embeddings &      Semantic retrieval 🔜 Planned
                    Vector Search                        

  08                RAG               Grounding answers  🔜 Planned
                                      in documents       

  09                Agent Workflows   State, tools,      🔜 Planned
                                      orchestration      

  10                Production        FastAPI, testing,  🔜 Planned
                    Engineering       security,          
                                      streaming          
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 📁 Repository Structure

``` text
ai-engineering-learning-journey/
│
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
│
├── 01-github-profile-finder/
│   ├── github_profile_finder.py
│   └── README.md
│
├── 02-structured-quiz/
│   ├── quiz_board.py
│   └── README.md
│
└── 03-ai-study-bot/
    ├── study_bot_app.py
    └── README.md
```

------------------------------------------------------------------------

## 🔎 Project 01 --- GitHub Profile Finder

My first project focused on communicating with an external API using
Python.

### What it does

The program accepts a GitHub username, sends a GET request to the GitHub
API, parses the JSON response, and displays selected public profile
information.

### What I learned

-   API endpoints
-   HTTP GET requests
-   HTTP status codes
-   `requests`
-   JSON responses
-   Python dictionaries
-   Functions and return values
-   `try/except`
-   Network errors and timeouts

### Mental model

``` text
Username
   ↓
Python
   ↓
HTTP GET request
   ↓
GitHub API
   ↓
JSON response
   ↓
Python dictionary
   ↓
Profile information
```

------------------------------------------------------------------------

## 🧩 Project 02 --- Structured Quiz Board

The second project focused on structured Python data.

### What it does

The application stores questions and answers in nested data structures,
asks the user each question, checks their answer, and calculates a final
score.

### What I learned

-   Dictionaries
-   Lists
-   Nested data
-   Loops
-   Conditionals
-   User input
-   String comparison
-   Score tracking

This project also helped prepare me for **structured AI outputs**, where
an application needs predictable fields rather than an uncontrolled
block of text.

------------------------------------------------------------------------

## 🎓 Project 03 --- AI Study Bot

My first LLM-powered application.

The Study Bot allows a learner to choose a study level and ask a
question. The LLM then adapts the explanation to the selected level and
provides an example plus a practice question.

### Features

-   🎚️ Beginner, Intermediate, and Advanced learning levels
-   💬 User-defined study questions
-   🧠 LLM-generated explanations
-   💡 Simple examples
-   📝 Practice questions / quizzes
-   🖥️ Interactive Streamlit interface
-   🔐 API key loaded from an environment variable

### Application Flow

``` text
User
  ↓
Streamlit UI
  ↓
Python application
  ↓
OpenAI Python SDK
  ↓
OpenAI API
  ↓
LLM
  ↓
Generated response
  ↓
Streamlit UI
```

One of the most important lessons from this stage was understanding that
the **SDK, API, LLM, and UI are different parts of the application**.

------------------------------------------------------------------------

## 🚀 Run the AI Study Bot Locally

### 1. Clone the repository

``` bash
git clone YOUR_REPOSITORY_URL
cd ai-engineering-learning-journey
```

### 2. Create a virtual environment

Windows:

``` powershell
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure the API key

Copy `.env.example` to `.env` and place your own API key in `.env`.

> ⚠️ Never commit `.env` or your real API key to GitHub.

If your current application reads `OPENAI_API_KEY` directly from your
operating-system environment, you can continue using that approach
instead of loading `.env`.

### 5. Run Streamlit

``` bash
streamlit run 03-ai-study-bot/study_bot_app.py
```

Streamlit will provide a local address, normally
`http://localhost:8501`.

------------------------------------------------------------------------

## 🔐 Security

Secrets should never be committed to source control.

This repository:

-   ignores `.env`
-   ignores common secret-key file patterns
-   provides `.env.example` only as a safe template
-   expects `OPENAI_API_KEY` to be supplied locally

**The `.env.example` file contains a placeholder only --- never replace
it with a real key before committing.**

------------------------------------------------------------------------

## 🧠 Key Concepts Learned

``` text
Python dictionary
      ↓
JSON
      ↓
HTTP/API
      ↓
SDK
      ↓
LLM
      ↓
Response
      ↓
Application UI
```

I am deliberately learning these layers before relying heavily on agent
frameworks.

------------------------------------------------------------------------

## 🎯 Roadmap

-   [x] Python API requests
-   [x] JSON parsing
-   [x] HTTP status codes
-   [x] Basic exception handling
-   [x] Structured Python data
-   [x] First LLM API call
-   [x] Dynamic prompting
-   [x] Streamlit interface
-   [ ] Input validation and robust API error handling
-   [ ] Structured LLM outputs
-   [ ] Conversation state
-   [ ] Tool/function calling
-   [ ] Embeddings
-   [ ] Vector search
-   [ ] Retrieval-Augmented Generation (RAG)
-   [ ] Document ingestion and citations
-   [ ] Agent workflows
-   [ ] FastAPI backend
-   [ ] Testing
-   [ ] Security and reliability
-   [ ] Streaming / WebSockets

------------------------------------------------------------------------

## 🏁 Long-Term Goal

The final goal is to build a portfolio-ready **AI Research & Study
Agent** that can work with documents, retrieve relevant information,
produce grounded answers with citations, use tools, maintain workflow
state, and expose its capabilities through a production-style
application.

------------------------------------------------------------------------

## 📌 Project Status

**Actively learning and building.**

This repository will continue to evolve as each new AI engineering
concept is learned, tested, and integrated into the larger project.

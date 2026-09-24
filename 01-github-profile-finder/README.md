# 🔎 GitHub Profile Finder

A beginner-friendly Python project that retrieves and displays public
GitHub profile information using the GitHub REST API.

This was the **first project in my AI Engineering Learning Journey** and
helped me understand how Python applications communicate with external
APIs.

------------------------------------------------------------------------

## 🎯 Project Goal

Before working with LLM APIs, I wanted to understand the fundamentals of
API communication:

**Python → HTTP Request → API → JSON Response → Python**

The application asks for a GitHub username, sends a GET request to the
GitHub API, processes the response, and displays useful profile
information.

------------------------------------------------------------------------

## ✨ Features

-   Search for a public GitHub user by username
-   Retrieve profile information using an API
-   Display:
    -   Name
    -   Username
    -   Bio
    -   Location
    -   Public repositories
    -   Followers
    -   Following
    -   Profile URL
-   Handle profiles that do not exist
-   Handle network/request errors
-   Use a request timeout to avoid waiting indefinitely

------------------------------------------------------------------------

## 🧠 How It Works

``` text
User enters GitHub username
            ↓
      Python program
            ↓
     HTTP GET request
            ↓
       GitHub API
            ↓
      JSON response
            ↓
 response.json()
            ↓
   Python dictionary
            ↓
  Profile information
```

------------------------------------------------------------------------

## 🛠️ Concepts Practised

-   Python functions
-   Function parameters and return values
-   REST APIs
-   API endpoints
-   HTTP GET requests
-   HTTP status codes
-   JSON
-   Python dictionaries
-   `requests`
-   `try/except`
-   Timeouts
-   Basic error handling

------------------------------------------------------------------------

## ▶️ Run Locally

From the main repository directory, install the dependencies:

``` bash
pip install -r requirements.txt
```

Then run:

``` bash
python 01-github-profile-finder/github_profile_finder.py
```

Enter a public GitHub username when prompted.

------------------------------------------------------------------------

## 💡 Key Learning

One of the most important things I learned from this project was that
creating a URL does **not** call an API.

The API request actually happens when Python executes the request:

``` text
requests.get(...)
```

I also learned the difference between the complete HTTP response and the
JSON body contained inside that response.

``` text
HTTP response
    ↓
response.json()
    ↓
Python dictionary
```

------------------------------------------------------------------------

## 🚀 Why This Project Matters

This project created the foundation for the later stages of my AI
engineering journey.

An LLM application also communicates with an external service through an
API, so understanding ordinary API requests first made it easier to
understand LLM APIs later.

------------------------------------------------------------------------

## ➡️ Next Project

**02 --- Structured Quiz Board**

The next project focuses on nested Python data structures, loops,
conditionals, and structured information.

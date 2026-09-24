# 🧩 Structured Quiz Board

An interactive Python quiz application built to practise working with
structured data.

This is the **second project in my AI Engineering Learning Journey**,
following the GitHub Profile Finder.

------------------------------------------------------------------------

## 🎯 Project Goal

The goal was to become comfortable working with structured Python data
before moving into structured LLM responses.

The project stores multiple questions and answers inside nested Python
data structures and processes them using loops and conditionals.

------------------------------------------------------------------------

## ✨ Features

-   Store multiple quiz questions
-   Display questions one at a time
-   Accept user answers
-   Compare answers without case sensitivity
-   Tell the user whether an answer is correct
-   Display the correct answer when needed
-   Track the score
-   Display the final result

------------------------------------------------------------------------

## 🧠 Data Structure

The project uses a structure similar to:

``` text
Quiz dictionary
      ↓
"questions"
      ↓
List
      ↓
Question dictionary
      ├── Question
      └── Answer
```

The application then loops through each dictionary in the list.

------------------------------------------------------------------------

## 🔄 Application Flow

``` text
Quiz data
    ↓
for loop
    ↓
Display question
    ↓
User input
    ↓
Compare answers
   ↙     ↘
Correct  Incorrect
   ↓        ↓
+1 score  Show answer
     \      /
      ↓    ↓
    Next question
         ↓
    Final score
```

------------------------------------------------------------------------

## 🛠️ Concepts Practised

-   Python dictionaries
-   Lists
-   Nested data structures
-   `for` loops
-   Conditionals
-   User input
-   String methods
-   Score tracking
-   Accessing dictionary values
-   Iterating over structured information

------------------------------------------------------------------------

## ▶️ Run Locally

From the repository root:

``` bash
python 02-structured-quiz/quiz_board.py
```

No API key is required for this project.

------------------------------------------------------------------------

## 💡 Key Learning

This project helped me understand that structured information is easier
for software to process than an uncontrolled block of text.

For example:

``` text
Question
Answer
Difficulty
Topic
```

can each be stored as separate fields.

That idea becomes important later when working with **structured LLM
outputs**, where an AI application may need to extract specific fields
from a model response rather than simply display generated text.

------------------------------------------------------------------------

## 🔗 Connection to AI Engineering

``` text
Python structured data
        ↓
Nested dictionaries/lists
        ↓
Predictable fields
        ↓
Structured LLM outputs
        ↓
AI application logic
```

This project therefore acts as a bridge between Python fundamentals and
AI application development.

------------------------------------------------------------------------

## ➡️ Next Project

**03 --- AI Study Bot**

The next stage connects Python to an actual LLM API and then places a
Streamlit interface in front of the application.

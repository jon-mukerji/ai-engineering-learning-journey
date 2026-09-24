from openai import OpenAI
import streamlit as st


client = OpenAI()


st.title("🎓 AI Study Bot")

st.write(
    "Ask a question and I'll explain it according to your study level."
)


level = st.selectbox(
    "Select your study level:",
    ["Beginner", "Intermediate", "Advanced"]
)


question = st.text_area(
    "What would you like to learn?"
)


if st.button("Ask AI"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        ai_answer = client.responses.create(
            model="gpt-5.6-luna",

            instructions=f"""
            You are an AI study assistant.
            The student is at {level} level.
            Explain the concept at an appropriate level.
            Give one simple example.
            Finish with a short practice question or quiz.
            """,

            input=question
        )

        st.write(ai_answer.output_text)
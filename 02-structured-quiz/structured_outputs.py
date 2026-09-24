''' 
ai_response = {
    "topic": "Python Loops",
    "difficulty": "beginner",
    "definition": "A loop allows Python to repeat instructions.",
    "example": "for number in range(5): print(number)",
    "practice_question": "Write a loop that prints numbers from 1 to 10."
}

print(ai_response["topic"])
print(f"Topic: {ai_response['topic']}")
'''

quiz = {

     "topic" : "What is python?",
     "Definition": "Pythin is a programming language",
     "questions": [
     
         {"Question": "What keyword defines a function in Python?",
          "Answer": "def"},

        {"Question": "What keyword sends a value back from a function?",
         "Answer" : "return"},

        {"Question": "Which data type stores key-value pairs?",
        "Answer": "dictionary"}
     ]

}

score = 0

print("=============================")
print("Quiz board")
print("=============================")

for item in quiz["questions"]:

    print(f"\nQuestions : {item["Question"]}")

    user_answer = input("Your answer")
    if user_answer.lower() == item["Answer"].lower():
        print("Correct")

        score = score + 1

    else:
        print("Incorrect")
        print(f"Correct Answer: {item["Answer"]}")

print("==============================")
print(f"Your score = {score}/{len(quiz["questions"])} ")
print("================================")
#Quiz app 


# List of questions and answers
questions = [
    {
        "question": "What is the output of 2 + 3 * 2?",
        "options": {"a": "10", "b": "8", "c": "7", "d": "12"},
        "answer": "c"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": {"a": "list", "b": "dict", "c": "set", "d": "tuple"},
        "answer": "d"
    },
    {
        "question": "What keyword is used to define a function?",
        "options": {"a": "define", "b": "func", "c": "def", "d": "function"},
        "answer": "c"
    }
]

score = 0

print("🎓 Welcome to the Python Quiz!")
print("Type a, b, c, or d for your answer.\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['question']}")
    for key, value in q["options"].items():
        print(f"   {key}) {value}")
    
    user_answer = input("Your answer: ").lower()
    
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was: {q['answer']}\n")

print(f"📝 Quiz complete! Your score: {score}/{len(questions)}")

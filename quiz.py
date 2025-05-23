def quiz_game():
    score = 0

    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Mumbai", "B) Delhi", "C) Chennai", "D) Kolkata"],
            "answer": "B"
        },
        {
            "question": "Who is the father of the computer?",
            "options": ["A) Charles Babbage", "B) Alan Turing", "C) Tim Berners-Lee", "D) Bill Gates"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
            "answer": "C"
        }
    ]

    print("🧠 Welcome to the Quiz Game!\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}\n")

    print(f"🎉 Quiz Over! Your final score is {score}/{len(questions)}")

quiz_game()

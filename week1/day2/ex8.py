def star_wars_quiz():
    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"}
    ]

    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for item in data:
        user_answer = input(item["question"] + " ").strip()
        if user_answer.lower() == item["answer"].lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({"question": item["question"], "your_answer": user_answer, "correct_answer": item["answer"]})

    print(f"\nYou got {correct_answers} correct answers and {incorrect_answers} incorrect answers.")

    if wrong_answers:
        print("\nHere are the questions you got wrong:")
        for wrong in wrong_answers:
            print(f"Question: {wrong['question']}")
            print(f"Your answer: {wrong['your_answer']}")
            print(f"Correct answer: {wrong['correct_answer']}\n")

    if incorrect_answers > 3:
        retry = input("You got more than 3 wrong answers. Do you want to play again? (yes/no) ").strip().lower()
        if retry == "yes":
            star_wars_quiz()

star_wars_quiz()

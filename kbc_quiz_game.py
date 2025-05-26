# KBC Game

def kbc_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
            "answer": "1"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
            "answer": "2"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["1. Charles Dickens", "2. William Shakespeare", "3. J.K.Rowling", "4. Mark Twain"],
            "answer": "2"
        },
        {
            "question": "What is 5 + 3?",
            "options": ["1. 6", "2. 7", "3. 8", "4. 9"],
            "answer": "3"
        }
    ]

    prize_money = [1000, 2000, 5000, 10000]
    total_prize = 0

    print("Welcome to KBC".center(50))
    print("Let's Play".center(50))

    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]['question']}")
        for option in questions[i]["options"]:
            print(option)
        user_input = input("Enter your answer (1/2/3/4): ")

        if user_input == questions[i]["answer"]:
            total_prize += prize_money[i]
            print(f"Congratulations! You won Rs.{prize_money[i]}.")
        else:
            print(f"Wrong answer! The correct answer was option {questions[i]['answer']}.")
            print(f"You are taking home Rs.{total_prize}.")
            break
    else:
        print(f"Congratulations! You have won the full prize of Rs.{total_prize}.")

kbc_game()

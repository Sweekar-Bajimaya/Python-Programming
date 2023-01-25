class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

def run_quiz():
    quiz_question = "What is the capital of France?"
    quiz_options = ["Paris", "London", "Rome", "Madrid"]
    quiz_answer = "Paris"

    quiz = Quiz(quiz_question, quiz_options, quiz_answer)

    print(quiz.question)
    for i, option in enumerate(quiz.options):
        print(f"{i+1}. {option}")

    user_answer = input("Enter the number of the correct option: ")
    if quiz.options[int(user_answer)-1] == quiz.answer:
        print("Correct!")
    else:
        print("Incorrect.")

run_quiz()

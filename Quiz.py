class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question.prompt)
        for idx, choice in enumerate(question.choices, 1):
            print(f"{idx}. {choice}")

    def take(self):
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Enter the number of your answer: ")
            if question.check_answer(question.choices[int(user_answer) - 1]):
                self.score += 1
                print("Correct!")
            else:
                print("Wrong!")
        if self.score != 15: print(f"Your final score is: {self.score}/{len(self.questions)}")
        else: print(f"You have the maximum number of points! You're the best!")

class User:
    def __init__(self):
        self.scores = []
    
    def take_quiz(self, quiz):
        name = input("Enter Your Name: ")
        print(f"Welcome to the School Quiz, {name}!")
        quiz.take()
        self.scores.append(quiz.score)

class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer
    
    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()

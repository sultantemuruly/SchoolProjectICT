from Question import Question
from Quiz import Quiz
from User import User

questions = [
    Question("What is the capital of Great Britain?", ["London", "Paris", "Berlin", "Madrid"], "London"),
    Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"),
    Question("What color is a banana?", ["Red", "Green", "Blue", "Yellow"], "Yellow"),
    
    Question("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter"),
    Question("Who wrote the play \"Romeo and Juliet\"?", ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"], "William Shakespeare"),
    Question("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], "H2O"),
    
    Question("What gas do plants absorb from the atmosphere for photosynthesis?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "Carbon Dioxide"),
    Question("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Silicon"], "Diamond"),
    Question("What part of the plant conducts photosynthesis?", ["Root", "Stem", "Leaf", "Flower"], "Leaf"),
    
    Question("What is the value of Pi, to two decimal places?", ["3.14", "2.18", "4.13", "3.5"], "3.14"),
    Question("If a triangle has angles of 45° and 45°, what is the measure of the third angle?", ["45°", "90°", "100°", "180°"], "90°"),
    Question("Solve for x: 2x + 3 = 7", ["1", "2", "3", "4"], "2"),
    
    Question("Which river is known as the longest river in the world?", ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "Nile River"),
    Question("What country has the most natural lakes?", ["United States", "Canada", "Russia", "China"], "Canada"),
    Question("Who was the first President of the United States?", ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "George Washington"),
]

quiz = Quiz(questions)

user = User()
user.take_quiz(quiz)

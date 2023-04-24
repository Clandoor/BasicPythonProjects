"""

"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []

for data in question_data:
    questionObject = Question(data['question'], data['correct_answer'])
    questionBank.append(questionObject)

#questionBank is a list of objects

"""
Another Approach:
for i in range(len(question_data)):
    questionObject = Question(question_data[i]['text'], question_data[i]['answer'])
    questionBank.append(questionObject)

print(questionBank)
"""

quiz = QuizBrain(questionBank)
while quiz.stillHasQuestion():
    quiz.nextQuestion()

print("Congratulations! You have completed the Quiz!")
print(f"Your final score is: {quiz.userScore} / {quiz.questionNumber}")

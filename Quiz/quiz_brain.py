"""
Manages the tasks of:
1. Asking the user questions
2. Checking whether answer was correct or not.
3. Checking whether the quiz has ended or not
"""

class QuizBrain:
    def __init__(self, questionList):
        self.questionList = questionList
        self.questionNumber = 0
        self.userScore = 0

    def stillHasQuestion(self):
        totalQuestions = len(self.questionList)
        return self.questionNumber < totalQuestions

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        usersAnswer = input(f"Q.{(self.questionNumber + 1)}: {currentQuestion.questionText} (True / False): ")
        self.questionNumber += 1
        self.checkAnswer(usersAnswer, currentQuestion.answer)

    def checkAnswer(self, usersAnswer, correctAnswer):
        self.totalScore = 0
        self.totalScore += 1
        if usersAnswer.lower() == correctAnswer.lower():
            self.userScore += 1
            print("You got it!")

        else:
            print("That's wrong :/")

        print(f"Your current score: {self.userScore} / {self.questionNumber}")
        print(f"The correct answer is {correctAnswer}.")
        print()
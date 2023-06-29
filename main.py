from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for counter in range(0, len(question_data)):
    text = (question_data[counter]['question'])
    answer = (question_data[counter]['correct_answer'])
    question = Question(text, answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the course")
print(f"Your over-all score is {quiz_brain.score}/{quiz_brain.question_number}")








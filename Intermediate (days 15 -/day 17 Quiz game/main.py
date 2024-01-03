from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_objects = []
for question in question_data:
    question_objects.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_objects)

while quiz.has_questions():
    quiz.next_question()

print("Thats it your done")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")
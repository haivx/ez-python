from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for record in question_data:
    question_bank.append(Question(record["text"], record["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("\n")
print(f"You're completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
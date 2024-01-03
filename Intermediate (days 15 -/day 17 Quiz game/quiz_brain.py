class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ") 

        self.check_answer(player_answer, current_question.answer)

    def has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, player_answer, game_answer):
        if player_answer.lower() == game_answer.lower():
            print("You are correct")
            self.score += 1
        else:
            print("You are wrong")
        print(F"The correct answer was: {game_answer}")
        print(f"Your current score is {self.score} / {self.question_number}")
        print("\n")
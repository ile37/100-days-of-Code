import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
screen.setup(width=750, height=500)

turtle.shape("blank_states_img.gif")

states_data = pd.read_csv("50_states.csv")
list_of_states = states_data["state"].to_list()
correct_guesses = 0
while True:
    
    answer_state = screen.textinput(title=f"{correct_guesses} / 50 States correct", prompt="What's another state's name?").title()

    if answer_state in list_of_states:
        correct_guesses += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        answer_state_row = states_data[states_data.state == answer_state]
        t.goto(int(answer_state_row.x), int(answer_state_row.y))  
        t.write(answer_state)
        list_of_states.remove(answer_state)
    else:
        continue


    if correct_guesses == 50:
        break




turtle.mainloop()
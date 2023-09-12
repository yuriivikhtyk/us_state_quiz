import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state_data = pd.read_csv('50_states.csv')
state_normal = state_data.state.to_list()
game_is_on = True
guessed_states_count = 0
w_t = turtle.Turtle()
w_t.hideturtle()
w_t.penup()
w_t.color("black")
guessed_states = []
not_guessed_states = []

def write_state(state):
    tmp_state = state_data[state_data.state == state]
    x_cor = tmp_state.x.to_list()
    y_cor = tmp_state.y.to_list()
    coordinates = (x_cor[0], y_cor[0])
    w_t.goto(coordinates)
    tmp_text = state_data[state_data.state == state]
    text = tmp_text.state.to_list()
    w_t.write(arg=f"{text[0]}", move=False, align="center", font=("Arial", 7, "normal"))


while game_is_on:
    answer_state = screen.textinput(title=f"{guessed_states_count}/50 Guess the State", prompt="What is another state`s name?").title()
    if answer_state == "Exit":
        game_is_on = False
        for state in state_normal:
            if state not in guessed_states:
                w_t.color("red")
                write_state(state=state)
    if answer_state in state_normal and answer_state not in guessed_states:
        guessed_states_count += 1
        write_state(answer_state)
        guessed_states.append(answer_state)



screen.exitonclick()


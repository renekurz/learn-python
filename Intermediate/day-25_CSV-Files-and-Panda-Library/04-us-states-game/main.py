import turtle
import pandas

FONT = ("Courier", 6, "normal")
ALIGN = "center"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states = pandas.read_csv("50_states.csv")
states_list = states["state"].to_list()
guessed_states = []

print_states = turtle.Turtle()
print_states.penup()
print_states.hideturtle()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another states name?").title()

    if answer_state == "Exit":
        break
    elif answer_state in states_list:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state = states[states["state"] == answer_state]

            state_name = state.state.iloc[0]
            state_x = state.x.iloc[0]
            state_y = state.y.iloc[0]

            print_states.goto(state_x, state_y)
            print_states.write(state_name, align=ALIGN, font=FONT)

not_guessed_states = states_list

for state in guessed_states:
    if state in not_guessed_states:
        not_guessed_states.remove(state)

states_dict = {
    "state": not_guessed_states
}

not_guessed_states_data = pandas.DataFrame(states_dict)
not_guessed_states_data.to_csv("states_to_learn.csv")
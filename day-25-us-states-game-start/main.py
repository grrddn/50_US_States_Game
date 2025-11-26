import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("day-25-us-states-game-start/50_states.csv")
states = data.state.to_list()
guessed_states = []

score = 0
running = True
while running:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        running = False
    if answer_state in states:
        score += 1
        guessed_states.append(answer_state)
        circle = turtle.Turtle()
        circle.hideturtle()
        circle.penup()
        circle.goto(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        circle.write(answer_state)

missing_states = []
for state in states:
    if state not in guessed_states:
        missing_states.append(state)

new_data = pd.DataFrame(missing_states)
new_data.to_csv("day-25-us-states-game-start/missing_states.csv")


circle = turtle.Turtle()
circle.hideturtle()
circle.penup()
circle.goto(0, 0)
circle.write(f"Your score is: {score}", align="center", font=("Arial", 16, "normal"))



# screen.exitonclick()
screen.mainloop()

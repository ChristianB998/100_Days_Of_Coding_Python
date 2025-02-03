import turtle
import pandas

# Cordinates are not correct in this format

screen = turtle.Screen()
screen.title("U.S. States Games")
screen.setup(width=800, height=600)

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")

# turtle.penup()
#
#
# game_is_on = True
# counter = 0

# while game_is_on:
#     if counter != 50:
#         answer_state = screen.textinput(title=f"{counter}/50 States Correct", prompt= "What's another state's name?")
#         answer_state = answer_state.lower()
#         if answer_state in data['state'].str.lower().values:
#             state_data = data[data.state.str.lower() == answer_state]
#             original_state = data[data.state.str.lower() == answer_state]['state'].values[0] # should be in lower case write in original
#             x_cor = state_data.x.values[0]
#             y_cor = state_data.y.values[0]
#             turtle.goto(x_cor, y_cor)
#             turtle.write(original_state)
#             counter += 1
#
# turtle.mainloop()

game_is_on = True
all_states = data.state.to_list()
guessed_states = []
states_to_learn = []

while len(guessed_states) != len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # # Create a DataFrame of states to learn
        # states_to_learn = data[~data['state'].isin(guessed_states)]
        #
        # # Save the DataFrame to a CSV file
        # states_to_learn.to_csv('states_to_learn.csv', index=False)
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item()) # .item() we get the wholeframe without it which gives errors
        t.write(state_data.state.item())
        guessed_states.append(answer_state)


turtle.mainloop()



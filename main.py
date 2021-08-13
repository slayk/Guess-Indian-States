import turtle
import pandas

answer_state_list = []
state_data = pandas.read_csv('28_states.csv')
state_data.reset_index(drop=True, inplace=True)
state_list = state_data["state"].tolist()

total_number_of_states = len(state_list)

screen = turtle.Screen()
screen.title("Indian States Game")

screen.addshape("india-states.gif")
turtle.shape("india-states.gif")

count = 1
while count <= total_number_of_states:
    answer_state = screen.textinput(title=f"Guessed States: {count-1}/{total_number_of_states}", prompt=f"What's {count} state's name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in state_list:
            if state not in answer_state_list:
                missing_state.append(state)
        data = pandas.DataFrame(missing_state)
        data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        answer_state_list.append(answer_state)
        create_new = turtle.Turtle()
        create_new.hideturtle()
        create_new.penup()
        answer_state_data = state_data[state_data["state"]==answer_state]
        create_new.goto(int(answer_state_data["x"]), int(answer_state_data["y"]))
        create_new.write(answer_state)
    count +=1

turtle.mainloop()

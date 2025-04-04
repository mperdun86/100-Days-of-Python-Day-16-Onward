import turtle as t
import pandas

IMAGE = "blank_states_img.gif"
STATE_INFO = "50_states.csv"
FONT = ('Consolas', 10, 'normal')

screen = t.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
t.shape(IMAGE)

df = pandas.read_csv(STATE_INFO)
state_names = df.state.tolist()
print(state_names)
writer = t.Turtle()
writer.hideturtle()
writer.penup()
writer.color('black')

guessed_states = []
game_active = True
while game_active:
    user_guess = screen.textinput(title=f'{len(guessed_states)}/50 States guessed', prompt="Type the name of a U.S. State!\n You may also type 'exit'").title()
    if user_guess == 'Exit':
        missed_states = [state for state in state_names if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('states_missed.csv')
        ### IS THIS MORE CONCISE OR LESS READABLE? ###
        #pandas.DataFrame(missed_states).to_csv('states_missed.csv')
        break

    if user_guess in state_names and user_guess not in guessed_states:
        state_data = df[df.state == user_guess]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(user_guess, align='center', font=FONT)

        guessed_states.append(user_guess)
    else:
        print("this text is a placeholder for later")

    # if len(guessed_states) == 50:
    #     writer.goto(0,0)
    #     writer.color('red')
    #     writer.write('YOU GUESSED THEM ALL!', align='center', font=FONT)
    #     game_active = False
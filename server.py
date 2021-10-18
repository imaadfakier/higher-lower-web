import flask
import random

# target_number = random.randint(1, 10)
target_number = 0

app = flask.Flask(__name__)


# def make_bold(func):
#     def wrapper():
#         return '<b>' + func() + '</b>'
#     return wrapper


def generate_random_number():
    global target_number
    target_number = random.randint(0, 9)


@app.route('/')
# @make_bold
def index():
    generate_random_number()
    return '<h1>Guess a number between 0 and 9!</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def check_guess(guess):
    if guess > target_number:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if guess < target_number:
        return '<h1 style="color: orange">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    return '<h1 style="color: green">You found me!</h1>' \
           '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)

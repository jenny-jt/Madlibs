"""A madlib game that compliments its users."""

import random

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

PERSON_global = "person"
@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    person = request.args.get("person")
    PERSON_global = person
    compliment = random.sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=person,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """see if person wants to play madlibs"""

    play_game = request.args.get("play")
   
    person = request.args.get("person")
    print(person)

    if play_game == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html", person=PERSON_global)

# @app.route('/game')
# def display():
#     return render_template("game.html")
          
@app.route('/madlib')
def show_madlib():
    """show madlib"""

    name = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    return render_template("madlib.html", 
                            person=name,
                            color=color,
                            noun=noun,
                            adjective=adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")

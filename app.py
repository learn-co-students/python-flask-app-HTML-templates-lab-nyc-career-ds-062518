# import flask and render_template here
from flask import Flask, request, render_template
import pdb


# create new Flask App here
app = Flask(__name__)


# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1><p>be careful, it\'s still under construction...</p>"

@app.route('/profile/<name>')
def profile(name):
    return "<h1>Welcome to " + name.title() + "'s profile</h1>"


@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def profile_name(name, age, favorite_hobby, hometown):
    formatted_name = name.title()
    city = hometown.split(',')[0]
    state = hometown.split(',')[1]
    state = state.upper()
    city = city.replace("_", " ").title()
    formatted_hometown = city + ", " + state
    formatted_hobby = favorite_hobby.title()
    return render_template("profile.html", profile_name = formatted_name, person_age = age, person_hobby = formatted_hobby, person_hometown = formatted_hometown)




# tell your flask app to run with debug mode on
if __name__ == '__main__':
    app.run(debug = True)

# import flask and render_template here
from flask import Flask, render_template
import re

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1> <p>be careful, it's still under construction...</p>"

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', person_name = name.title())

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def about(name, age, favorite_hobby, hometown):
    hometown_formatted = hometown.split(',')
    city = re.sub('[_]', ' ', hometown_formatted[0]).title()
    # city = hometown_formatted[0].strip('_')
    state = hometown_formatted[1].upper()
    hometown_final = city + ', ' + state
    return render_template('about.html', name=name.title(), age=age, favorite_hobby=favorite_hobby.title(), hometown=hometown_final)

    # city = re.sub('[^a-zA-Z0-9\n\.]', ' ', hometown_formatted[0])
# tell your flask app to run with debug mode on
if __name__ == '__main__':
    app.run(debug=True)

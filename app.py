# import flask and render_template here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1> <p>be careful, it's still under construction...</p>"
#
# @app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
# def profile(name,age,favorite_hobby, hometown):
#     return "<h1>Welcome to {0}'s profile</h1> <h3>Abount {0}: </h3> <ul><b>Age:</b> <li>{1}</li> <br> <b>Favorite Hobby:</b><li>{2}</li> <br> <b>Hometown:</b> <li>{3}</li></ul>".format(name, age, favorite_hobby, hometown)
@app.route('/profile/<name>')
def user_profile(name):
    return "<h1>Welcome to {}'s profile</h1>".format(name.capitalize())

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def show_profile(name, age, favorite_hobby, hometown):
    name = name.capitalize()
    age = age
    favorite_hobby = favorite_hobby.title()
    hometown_list= hometown.title().replace("_", " ").split(",")
    hometown = hometown_list[0] + ", " + hometown_list[1].upper()
    return render_template('profile.html', name=name, age=age, favorite_hobby=favorite_hobby, hometown=hometown)

# tell your flask app to run with debug mode on
if __name__ == '__main__':
    app.run(debug=True)

# import flask and render_template here
from flask import Flask, render_template
import pdb

# create new Flask App here
app=Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1> <p>be careful, it's still under construction...</p>"

#
# @app.route("/profile/mary")
# def profile():
#     return "<h1>Welcome to Mary's profile</h1>"

@app.route("/profile/<name>")
def name (name):
    return "<h1>Welcome to %s's profile</h1>" %name.capitalize()

@app.route("/profile/<name>/<age>/<favorite_hobby>/<hometown>")
def bio (name, age, favorite_hobby, hometown):
    welcome="<h1>Welcome to %s's profile!</h1>" %name.capitalize()
    about="<h3>About %s:</h3>"%name.capitalize()
    age='<ul><strong>Age:</strong><li>%s</li></ul>'%age
    favorite_hobby='<ul><strong>Favorite Hobby:</strong><li>%s</li></ul>' %favorite_hobby.title()
    town=hometown.split(',')[0].title()
    state=hometown.split(',')[1].upper()
    hometown='<ul><strong>Hometown:</strong><li>%s</li></ul>'%(town.split('_')[0] + ' ' + town.split('_')[1]+ ', ' + state)
    return welcome + about + age + favorite_hobby + hometown

@app.route("/hello-world-template")
def hello_world_template():
    return render_template('hello_world.html')

@app.route("/profile")
def show_profile(name, age, favorite_hobby, hometown):
    return render_template('profile.html', name=name, age=age, favorite_hobby=favorite_hobby, hometown=hometown)


# tell your flask app to run with debug mode on
if __name__ == '__main__':
    app.run(debug=True)

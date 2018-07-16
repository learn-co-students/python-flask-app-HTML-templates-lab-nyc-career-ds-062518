from flask import Flask, render_template
import re

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1> <p>be careful, it's still under construction...</p>"

@app.route('/profile/<name>')
def profile_name(name):
    return render_template('profile.html', person_name = name.title())

@app.route("/profile/<name>/<age>/<favorite_hobby>/<hometown>")
def show_profile(name, age, favorite_hobby, hometown):
    hometown_formatted = str(hometown).split(',')
    city = re.sub('[_]', ' ', hometown_formatted[0]).title()
    state = hometown_formatted[1].upper()
    hometown_final = city + ', ' + state
    return render_template('about.html', name = str(name).title(), age = age, favorite_hobby = str(favorite_hobby).title(), hometown = hometown_final)

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

#
# def show_profile(name, age, favorite_hobby, hometown):
#     return render_template('profile.html', name=name, age=age, favorite_hobby=favorite_hobby, hometown=hometown)

# hometown_formatted[0].split('_')
# ('\W+?', ' ', hometown_formatted[0])
# '[^a-zA-Z0-9\n.]', ' ', hometown_formatted[0])



if __name__ == '__main__':
    app.run(debug=True)

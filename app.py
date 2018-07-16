from flask import Flask, render_template
# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1> <p>be careful, it's still under construction...</p>"

@app.route('/login')
def login():
    return "SOME HTML"

@app.route('/profile/<name>')
def profile(name):
    return"<h1> Welcome to {}'s profile </h1>".format(name)

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def show_profile(name, age, favorite_hobby, hometown):
    favorite_hobby_2 = [word.capitalize() for word in favorite_hobby.split('_')]
    favorite_hobby_3 = favorite_hobby_2[0] + '_' + favorite_hobby_2[1]
    hometown_1 = [word.capitalize() for word in hometown.split('_')]
    hometown_2 = hometown_1[1].split(',')
    home_town_final = hometown_1[0] + ' ' + hometown_2[0] + ', ' + hometown_2[1].upper()
    return render_template('profile.html', name=name.capitalize(), age=age, favorite_hobby=favorite_hobby_3, hometown=home_town_final)

# tell your flask app to run with debug mode on

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')


if __name__ == '__main__':
    app.run(debug=True)

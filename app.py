# import flask and render_template here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)


# define routes for your new flask app
@app.route('/')
def index():
    return '<h1>Welcome to my flask app</h1>' "<p>be careful, it's still under construction...</p>"

@app.route('/profile/<name>')
def profile(name):
    proper_name = name.title()
    return "<h1>Welcome to {}'s profile</h1>".format(proper_name)

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def about_me(name,age, favorite_hobby, hometown):
    proper_name = name.title()
    name_output = "<h1>Welcome to {}'s profile!</h1>".format(proper_name)
    about_john = "<h3>About {}:</h3>".format(proper_name)
    age = "<ul> <strong>Age:</strong> <li>{}</li> </ul>".format(age)
    proper_hobby = favorite_hobby.title()
    hobby = "<ul> <strong>Favorite Hobby:</strong> <li>{}</li> </ul>".format(proper_hobby)
    city = str(hometown.split(",")[0])
    city_space = city.replace("_"," ").title()
    state = str(hometown.split(",")[1]).upper()
    city_state = city_space + ", " + state
    home = "<ul> <strong>Hometown:</strong> <li>{}</li> </ul>".format(city_state)
    return name_output + about_john + age + hobby + home

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')
@app.route('/profile')
def show_profile(name, age, favorite_hobby, hometown):
    return render_template('profile.html', name=name, age=age, favorite_hobby=favorite_hobby, hometown=hometown)




# tell your flask app to run with debug mode on
if __name__ == '__main__':
    app.run(debug = True)

# import flask and render_template here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)

# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1> <p>be careful, it's still under construction...</p>"


@app.route('/profile/<name>')
def guest(name):
    return "<h1>Welcome to {}'s profile</h1>".format(name.title())

@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def about_me(name, age, favorite_hobby, hometown):
    if "_" in hometown:
        home = hometown.replace("_", " ").split(",")
        hometown = home[0].title() + ", " + home[1].upper()
    return render_template('profile.html', name=name.title(), age=age, favorite_hobby=favorite_hobby.title(), hometown=hometown)
    # return "<h1>Welcome to {0}'s profile</h1> \
    # <h3>About {0}</h3> \
    # <ul> <b>Age</b> <li>{1} </li><br>\
    #  <b>Favorite Hobby</b> <li>{2}</li> <br>\
    # <b>Hometown</b> <li>{3}</li></ul>".format(name, age, favorite_hobby, hometown)

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

# tell your flask app to run with debug mode on
#only run app if we are in the main file where it is created
#and then can work on files that import it without running th eapp
if __name__ == '__main__':
    app.run(debug=True)

# import flask and render_template here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)


# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1> <p>be careful, it's still under construction...</p>"
@app.route('/profile/<name>')
def user_profile(name):
    return "<h1>Welcome to {}'s profile</h1>".format(name.capitalize())
# @app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
# def user_profile_complete(name, age, favorite_hobby, hometown):
#     return """<h1>Welcome to {0}'s profile!</h1>
#     <h3>About {0}:</h3>
#     <ul>
#         <strong>Age:</strong><li>{1}</li>
#         <strong>Favorite Hobby:</strong><li>{2}</li>
#         <strong>Hometown:</strong><li>{3}</li>
#     </ul>""".format(name,age,favorite_hobby,hometown)
@app.route('/login')
def login():
    return "<h6>SOME HTML</h6>"
@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')
@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def show_profile(name, age, favorite_hobby, hometown):
    favorite_hobby_2 = [word.capitalize() for word in favorite_hobby.split('_')]
    favorite_hobby_3 = favorite_hobby_2[0] + '_' + favorite_hobby_2[1]
    hometown_1 = [word.capitalize() for word in hometown.split('_')]
    hometown_2 = hometown_1[1].split(',')
    home_town_final = hometown_1[0] + ' ' + hometown_2[0] + ', ' + hometown_2[1].upper()
    return render_template('profile.html', name=name.capitalize(), age=age, favorite_hobby=favorite_hobby_3, hometown=home_town_final)
# tell your flask app to run with debug mode on
if __name__ == '__main__':
    app.run(debug=True)

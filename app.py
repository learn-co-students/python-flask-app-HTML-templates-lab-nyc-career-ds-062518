# import flask and render_template here
from flask import Flask, render_template

# create new Flask App here
app = Flask(__name__)




# define routes for your new flask app
@app.route('/')
def index():
    return "<h1>Welcome to my flask app</h1>" "<p>be careful, it's still under construction...</p>"


@app.route('/profile/<name>')
def profile(name):
    name_cap = name.title()
    return "<h1>Welcome to {}'s profile</h1>".format(name_cap)

# @app.route('/profile/jennifer')
# def profile():
#     return "<h1>Welcome to Jennifer's profile</h1>"
# tell your flask app to run with debug mode on

#/profile/<name>/<age>/<favorite_hobby>/<hometown>"
@app.route('/profile/<name>/<age>/<favorite_hobby>/<hometown>')
def about_me(name,age,favorite_hobby,hometown):
     name_cap = name.title()
     cap_h=favorite_hobby.title()
     city = str(hometown.split(",")[0])
     city_space = city.replace("_", " ").title()
     state= str(hometown.split(",")[1]).upper()
     city_state = city_space +", " + state


     name_output ="<h1>Welcome to {}'s profile!</h1>".format(name_cap)
     about_name ="<h3>About {}:</h3>".format(name_cap)
     age="<ul><strong>Age:</strong><li>{}</li>".format(age)
     hobby="<strong>Favorite Hobby:</strong><li>{}</li>".format(cap_h)
     town="<strong>Hometown:</strong><li>{}</li><ul>".format(city_state)
     return name_output + about_name + age + hobby+ town

@app.route('/hello-world-template')
def hello_world_template():
    return render_template('hello_world.html')

@app.route("/profile")
def show_profile(name, age, favorite_hobby, hometown):
    return render_template('profile.html', name=name, age=age, favorite_hobby=favorite_hobby, hometown=hometown)

if __name__ == '__main__':
    app.run(debug=True)


        #"<li> Favorite Hobby {}</li>.format(favorite_hobby)

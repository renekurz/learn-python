from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

# <name> will be the variable for your greet function
@app.route("/users/<name>")
def greet(name):
    return f"Hello {name}!"

# localhost:5000/path/users/1 -> your_path: users/1
# localhost:5000/path/users   -> your_path: users
@app.route("/path/<path:your_path>")
def tell_path(your_path):
    return f"Your path is: {your_path}"

# Dynamic route with two parameters:
# <name> is passed automatically as a string
# <int:age> ensures only numbers are allowed and converts it to an int
# Flask also validates type:
# /users/Alex/abc -> will NOT work (age must be an integer)
@app.route("/users/<name>/<int:age>")
def tell_name_age(name, age):
    return f"Hello {name}! You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True) # With debug=True you don't have to restart the server when changing something in your code
                        # When you save your file, it will automatically rerun the server
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Flask allows HTML in the return
    # You can type enter in a string, so it's easier to read
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragraph</p>' \
            '<img src="https://d2zp5xs5cp8zlg.cloudfront.net/image-61785-800.jpg">' \
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnR0b2Y4ODE5cjV3MHc1MXZ4aWFhNXl5c2o4dnd6N2ZmOTc4c3RwOSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oriO0OEd9QIDdllqo/giphy.gif">' 

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/users/<name>")
def greet(name):
    return f"Hello {name}!"

@app.route("/path/<path:your_path>")
def tell_path(your_path):
    return f"Your path is: {your_path}"

@app.route("/users/<name>/<int:age>")
def tell_name_age(name, age):
    return f"Hello {name}! You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True)
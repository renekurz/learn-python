from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

# with this code, you can start your flask app with "python3 02-special-attributes-built-into-python.py"
if __name__ == "__main__":
    app.run()
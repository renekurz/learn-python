from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Terminal:
# export FLASK_APP=01-first-web-server-with-flask.py
# flask run
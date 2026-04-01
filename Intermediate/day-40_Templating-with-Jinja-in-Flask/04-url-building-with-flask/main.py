from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", random_number=random_number, current_year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blogs")
@app.route("/blogs/<name>")
def get_blogs(name=None):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    
    return render_template("blog.html", posts=all_posts, name=name)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)

@app.route('/guess/<name_to_find>')
def guess(name_to_find):
    parameters = {'name': name_to_find}

    age_response = requests.get("https://api.agify.io", params=parameters)
    age_response.raise_for_status()
    age_data = age_response.json()
    guessed_age = str(age_data["age"])

    gender_response = requests.get("https://api.genderize.io", params=parameters)
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    guessed_gender = gender_data["gender"]

    capitalized_name =  name_to_find.capitalize()

    return render_template('guess.html', age=guessed_age, gender=guessed_gender, name=capitalized_name)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)



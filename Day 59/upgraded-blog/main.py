from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/b887c75c5685975eb953").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    target_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            target_post = blog_post
    return render_template("post.html", post=target_post)


if __name__ == "__main__":
    app.run(debug=True)

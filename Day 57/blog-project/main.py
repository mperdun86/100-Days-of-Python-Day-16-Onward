from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
all_posts_json = response.json()
all_posts = []
for post in all_posts_json:
    new_post = Post(
        post_id=post["id"],
        title=post["title"],
        subtitle=post["subtitle"],
        body=post["body"]
        )
    all_posts.append(new_post)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    selected_post = None
    for current_post in all_posts:
        if current_post.id == post_id:
            selected_post = current_post
            return render_template("post.html", target_post=selected_post)
    return "<h1>404: Page Not Found!</h1>", 404


if __name__ == "__main__":
    app.run(debug=True)

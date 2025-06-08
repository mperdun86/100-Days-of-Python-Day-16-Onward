from flask import Flask
import random

random_number = random.randint(1, 10)
print(random_number)

app = Flask(__name__)

@app.route("/")
def home():
    return ('<h1 style="text-align:center">Guess the Number, 1-10!</h1>'
            '<h2 style="text-align:center">use this endpoint to guess: /guess/(1-10) </h1>'
            '<center><img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWVuZ3B2d2ZqdmZlMnI0eTF6ZHNwenVodGU4dDNlcW9jbGplODdhdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0XtbC8EniiuwAEOQn/giphy.gif"></center>')

@app.route("/guess/<int:number>")
def higher_or_lower(number):
    if number > random_number:
        return ('<h1 style="text-align:center">Too High!</h1>'
                '<center><img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ29weDRpejQxMDVycHoyNjZ4amNicXRicGJ0cDRnZXViNzdsdW1qayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/55vgJ0atxFpks/giphy.gif"></center>')
    elif number < random_number:
        return ('<h1 style="text-align:center">Too Low!</h1>'
                '<center><img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHozdno4cWpscmI5ZW9qY25oenZmdzkzd2xqeDVzam4yNHVudW83ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l3V0uUMTgbrSLoIj6/giphy.gif"></center>')
    else:
        return ('<h1 style="text-align:center">Perfect!</h1>'
                '<center><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjZ6d25ycjhtejlhZTh1c21maG9sYzRsMWFkZmxwZDZxaDFhaHMzOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Od0QRnzwRBYmDU3eEO/giphy.gif"></center>')

if __name__ == "__main__":
    app.run(debug=True)
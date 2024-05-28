# web app file

# from wordle import Wordle
from flask import Flask, render_template, request, redirect, url_for


# app instance
app = Flask(__name__)


# app routes
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


# running web app
if __name__ == "__main__":
    app.run(debug=True)
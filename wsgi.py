from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    render_template('home.html')


if __name__ == "__main__":
    application.run()

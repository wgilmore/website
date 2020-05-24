from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template('index.html')

@application.route("/generic")
def generic():
    return render_template('generic.html')

@application.route("/elements")
def elements():
    return render_template('elements.html')

@application.route("/homepage")
def homepage():
    return render_template('homepage.html')

if __name__ == "__main__":
    application.run()

from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template('index.html')

@application.route("/categories")
def categories():
    return render_template('categories.html')

@application.route("/blog")
def blog():
    return render_template('blog-single.html')

@application.route("/about")
def about():
    return render_template('about.html')

@application.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    application.run()


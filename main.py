import flask
from flask import Flask

app =Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to my website"
@app.route("/contact")
def Contact_Page():
    return "Contact Page"

@app.route("/home")
def HomePage():
    return "Home Page"

@app.route("/gallery")
def Gallery():
    return "Upload photos here"

if __name__ == "__main__":
    app.run()

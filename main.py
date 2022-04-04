import flask
from flask import Flask, render_template

app =Flask(__name__)

@app.route("/")
def Welcome():
    # return "Welcome to my website"
    return "<h1>Welcome</h1>"


@app.route("/contact")
def Contact_Page():
    # return "Contact Page"
    return render_template("contact.html")

@app.route("/home")
def HomePage():
    return "Home Page"

@app.route("/gallery")
def Gallery():
    return "Upload photos here"

if __name__ == "__main__":
    app.run()

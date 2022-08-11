from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world, and all who inhabit it!</p>"

@app.route("/<name>")
def hello_name(name):
    return "<p>Hello, " + name + "!</p>"

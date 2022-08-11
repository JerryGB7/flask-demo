from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world, and all who inhabit it! Look who figured out how to make a jenkins pipeline with docker containers.</p>"

@app.route("/<name>")
def hello_name(name):
    return "<p>Hello, " + name + "!</p>"

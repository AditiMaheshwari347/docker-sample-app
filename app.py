from flask import Flask

app = Flask(__name__)
color = "Blue"
@app.route("/")
def index():
    return "Hello World!" +  color
from flask import Flask, render_template
from jinja2 import Template
from card import card
 
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', location="Index")

@app.route("/test")
def test():
    return card("Jason", "Test Post", "This is a test post using react styled components in jinja2")

app.run()
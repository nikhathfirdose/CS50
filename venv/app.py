from flask import Flask, render_template  # to display html file

app = Flask(__name__)


@app.route("/")
def inde():
    return "Hi from server"


@app.route("/Nikki")
def secondIndex():
    return "Hello from Nikkitashaa"


# generalizede route
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}</h1>"  # can use tags


# can use an entire html page as well
@app.route("/html")
def index():
    return render_template("index.html")


# dynamic rendering of html
@app.route("/html2")
def intro():
    h = "HI from dynamic html"
    return render_template("index.html", line=h, multiple="nextline")
# we can use the same variable and give it another definition in Another route and that will work just fine
# ginger 2 alongside flask allows us to give conditionals inside html
# {% if true %}<h1> Yes</h1>
# {%else%} <h1> No</h1>
# {%endif%}
# checking git work

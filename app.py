import datetime
from flask import Flask, render_template  # to display html file

app = Flask(__name__)


# @app.route("/")
# def inde():
#     return "Hi from server"


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
@app.route("/hi")
def intro():
    h = "HI from dynamic html"
    return render_template("index.html", line=h, multiple="nextline")
# we can use the same variable and give it another definition in Another route and that will work just fine
# ginger 2 alongside flask allows us to give conditionals inside html
# {% if true %}<h1> Yes</h1>
# {%else%} <h1> No</h1>
# {%endif%}


@app.route("/bye")
def goodBye():
    h = "Lets say Bye"
    return render_template("index.html", line=h)


@app.route("/")
def year():
    now = datetime.datetime.now()
    new_year = now.month == 6 and now.day == 14
    return render_template("index.html", new_year=new_year, line="lets check")

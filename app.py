import os
import cs50

import urllib.parse

from urllib.parse import unquote
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

# Configure application
app = Flask(__name__)
app.jinja_env.filters['urlencode'] = urllib.parse.quote

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///projects.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")

@app.route("/portfolio")
def portfolio():
    # Get the 'project' query parameter from the URL
    project_num = request.args.get("project")

    if project_num:
        # Query for a specific project
        project = db.execute("SELECT * FROM projects")
        return render_template("project.html", project=project, id=int(project_num))
    else:
        # Query for all projects
        portfolio = db.execute("SELECT * FROM projects ORDER BY Priority")
        return render_template("portfolio.html", portfolio=portfolio)

#@app.route("/portfolio", methods=["GET", "POST"])
#def portfolio():
#    if request.method == "GET":
#        portfolio = db.execute("SELECT * FROM projects")
#        return render_template("portfolio.html", portfolio=portfolio)
#    else:
#        projectName = request.form.get("project")
#        project = db.execute("SELECT * FROM projects WHERE title = ?", projectName)
#        return render_template("portfolio.html", project=project)


@app.route("/project", methods=["GET", "POST"])
def project():
    if request.method == "GET":
        return redirect("/portfolio")
    else:
        projectName = request.form.get("project")
        project = db.execute("SELECT * FROM projects WHERE title = ?", projectName)
        return render_template("portfolio.html", project=project)

import urllib.parse

from cs50 import SQL
from flask import Flask, redirect, render_template, request

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

@app.route("/project", methods=["GET", "POST"])
def project():
    if request.method == "GET":
        return redirect("/portfolio")
    else:
        projectName = request.form.get("project")
        project = db.execute("SELECT * FROM projects WHERE title = ?", projectName)
        return render_template("portfolio.html", project=project)

@app.after_request
def set_security_headers(response):
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = (
        "default-src 'none'; "
        "script-src 'self' https://cdn.jsdelivr.net; "
        "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
        "img-src 'self' data: https://cdn.jsdelivr.net; "
        "font-src 'self' https://cdn.jsdelivr.net; "
        "connect-src 'self' https://formspree.io; "
        "frame-ancestors 'none'; "
        "base-uri 'self'; "
        "form-action 'self' https://formspree.io; "
        "object-src 'none';"  # Critical: Blocks Flash/PDF plugins that can be attack vectors
    )
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "no-referrer-when-downgrade"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=()"
    return response
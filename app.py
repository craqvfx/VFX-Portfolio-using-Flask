import urllib.parse

from github_request import get_github_repos
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

@app.route("/vfx_portfolio")
def vfx_portfolio():
    # Get the 'project' query parameter from the URL
    project_num = request.args.get("project")

    if project_num:
        # Query for a specific project
        project = db.execute("SELECT * FROM projects")
        return render_template("project.html", project=project, id=int(project_num))
    else:
        # Query for all projects
        portfolio = db.execute("SELECT * FROM projects ORDER BY Priority")
        return render_template("vfx_portfolio.html", portfolio=portfolio)

@app.route("/project", methods=["GET", "POST"])
def project():
    if request.method == "GET":
        return redirect("/vfx_portfolio")
    else:
        projectName = request.form.get("project")
        project = db.execute("SELECT * FROM projects WHERE title = ?", projectName)
        return render_template("vfx_portfolio.html", project=project)

@app.route("/coding_portfolio")
def coding_portfolio():
    username = "craqvfx"
    repos = get_github_repos(username)
    language_colors = {
        'Python': '#3572A5',
        'JavaScript': '#f1e05a',
        'HTML': '#e34c26',
        'CSS': '#563d7c',
        'Java': '#b07219',
        'C++': '#f34b7d',
        'C': '#555555',
    }

    if repos is None:
        return render_template("coding_portfolio.html", repos= None, username=username, language_colors=language_colors)

    # Process repo data for template
    repo_data = []
    if repos:
        for repo in repos:
            print(f"Adding {repo['name']} to list")
            repo_data.append({
            'name': repo['name'],
            'description': repo['description'] or 'No description available',
            'url': repo['html_url'],
            'updated_at': repo['updated_at'][:10],
            'language': repo['language'],
        })



    print("Final data being sent to template:", repo_data)  # Debug line
    return render_template("coding_portfolio.html", repos=repo_data, username=username, language_colors=language_colors)

# For google site ownership verification
@app.route('/google829e6f2aa0273ad6.html')
def google_verification():
    return app.send_static_file('google829e6f2aa0273ad6.html')

@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml')

@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')
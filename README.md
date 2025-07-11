# VFX Portfolio using Flask
## Video Demo:  https://youtu.be/1TyJGXoerXU
## Description:
Web app for my VFX portfolio, made using flask.<br>
Bootstrap was used for basic CSS styling and as a template, using the [Product Template](https://getbootstrap.com/docs/4.0/examples/product/).

## Feature ideas:
- github integration - dynamically render projects with api calls?<br>
- coding portfolio section<br>
- refactor About Me section with education, linkedin?, cv, work history etc.

## Directory:<br>

[Pages:](#pages)
- [Standard sections](#standard-sections)
- [Home](#home)
- [Portfolio](#portfolio)
- [Contact](#contact)
- [About Me](#about-me)

[UX](#ux)<br>
[File organisation](#file-organisation)<br>
[Python Anywhere hosting](#pythonanywhere-hosting)<br>

##

### Pages
There are 4 main pages, each of which have some standard sections, each explained hereafter:

#### Standard sections:
`layout.html`
Header -
- Name (non-linked), Home, Portfolio, Contact, About Me
Footer -
- Copyright text, Sitemap, Socials, Contact

`minimalist_layout.html`
Header -
- Name (non-linked), Home, Portfolio, Contact, About Me
Footer -
- Copyright text

#### Home:
Splash screen with fullscreen showreel playing as background. Centered section has name, brief description and link to portfolio. Uses `index.html`.<br>
This is the only page that uses `minimalist_layout.html` as the flask template instead of the standard `layout.html`.

#### Portfolio:
This is a gallery of all my projects, rendered by getting all projects from my database `projects.db` and their corresponding images. Uses `portfolio.html`.<br>
When `View Project` is clicked for any individual project, it leads you to `/portfolio?project={project_num}`. This is a page dynamically rendered from the database, in which the corresponding images, title and description are displayed using `project.html`.

#### Contact:
Contact form made using Formspree for a mailmerge. Uses `contact.html`.

#### About Me:
Simple About Me page rendered using `about_me.hmtl`.

### UX:
The General system flow is as follows:
```
Splash screen -> Portfolio -> Individual project -> Contact Me
```
On each page there is an appropriately placed button leading the user to the next page.<br>
It is not expected that the user must visit the `About Me` page, that is a voluntary extra.

### File organisation:
`/` contains `app.py`, `README.md` etc.<br>
`/templates` contains relevant .html files.<br>
`/JS` contains .js files. Currently only one: `form-validations.js` to validate the contact form.<br>
`/static/media/{project_num}` stores media (still frames and videos) for the corresponding project, where `{project_num}` represents the `id` attribute in `projects.db`.


### PythonAnywhere Hosting
1. Create venv e.g. `mkvirtualenv myvirtualenv --python=/usr/bin/python3.13`
2. git clone using PAT (private access token) as password
> [!TIP]
> If new PAT needed, go to github settings and generate a temporary classic PAT
3. cd into project directory using `cd craqvfx` or relevant project name.
4. Install dependencies using `pip install -r requirements.txt`
5. change WSGI configuration file to
```
import sys
path = '/home/craqvfx/craqvfx'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```
7. update source code directory, venv directory, etc. in pythonanywhere web section
6. It may be necessary to use absolute file path if an error is recieved that states projects.db does not exist:
db = SQL("sqlite:////home/craqvfx/craqvfx/projects.db")
7. reload app
> [!TIP]
> Troubleshoot using server log or access log

##

I hope you like my project and have enjoyed reading the `README.md`! If you have any questions, or wish to contact me, I am available via `cbolandross@gmail.com`, `craqvfx@gmail.com`, or `+44 7857 423006`.<br>
Alternatively, you can use the [website described in this project](https://craqvfx.pythonanywhere.com/).
> [!NOTE]
> If a web page cannot be found at that URL, it may be because I purchased a unique URL. Contact me using the aforementioned details if any issues arise.

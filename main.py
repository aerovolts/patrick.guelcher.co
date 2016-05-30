from flask import Flask, render_template

app = Flask(__name__)

author = 'Patrick Guelcher'
year = '2016'
credits = 'Template from Google Material Design; Modified by Myself.'

@app.route('/')
def home():
    title = 'Patrick Guelcher'
    description = 'The home of Patrick Guelcher on the internet.'
    return render_template('pages/index.html', author=author, year=year, credits=credits, title=title, description=description)

@app.route('/about')
def about():
    title = 'Patrick Guelcher'
    description = 'About the author of this portfolio website Patrick Guelcher.'
    return render_template('pages/about.html', author=author, year=year, credits=credits, title=title, description=description)

@app.route('/contact')
def contact():
    title = 'Contact Me | Patrick Guelcher'
    description = 'A listing of methods for contacting the website author Patrick Guelcher.'
    return render_template('pages/contact.html', author=author, year=year, credits=credits, title=title, description=description)

@app.route('/portfolio')
def portfolio():
    title = 'Portfolio | Patrick Guelcher'
    description = 'A portfolio of cartographic products produced by Patrick Guelcher in various software packages.'
    return render_template('pages/portfolio.html', author=author, year=year, credits=credits, title=title, description=description)

def main():
    app.run()

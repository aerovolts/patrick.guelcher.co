from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    description = 'The home of Patrick Guelcher on the internet. This personal website contains a blog and portfolio.'
    return render_template('pages/index.html', description=description)

@app.route('/about')
def about():
    description = 'About the author of this website and portfolio Patrick Guelcher.'
    return render_template('pages/about.html', description=description)

@app.route('/contact')
def contact():
    description = 'A listing of methods for contacting the website author Patrick Guelcher.'
    return render_template('pages/contact.html', description=description)

@app.route('/portfolio')
def portfolio():
    description = 'A portfolio of cartographic products produced by Patrick Guelcher in various software packages.'
    return render_template('pages/portfolio.html', description=description)

def main():
    app.run()

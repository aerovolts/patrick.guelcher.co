from flask import Flask, render_template

app = Flask(__name__)

author = 'Patrick Guelcher'
year = '2016'

@app.route('/')
def home():
    title = 'Home | Patrick Guelcher'
    description = 'The home of Patrick Guelcher on the internet.'
    return render_template('pages/index.html', author=author, year=year, title=title, description=description)

@app.route('/resume')
def about():
    title = 'Resume | Patrick Guelcher'
    description = 'A short background and list of skills about Patrick Guelcher.'
    return render_template('pages/resume.html', author=author, year=year, title=title, description=description)

@app.route('/portfolio')
def portfolio():
    title = 'Portfolio | Patrick Guelcher'
    description = 'A portfolio of cartographic products produced by Patrick Guelcher in various software packages.'
    return render_template('pages/portfolio.html', author=author, year=year, title=title, description=description)

if __name__ == '__main__':
    app.run()

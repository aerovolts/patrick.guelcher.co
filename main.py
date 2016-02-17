from flask import Flask, render_template

app = Flask(__name__)

author = 'Patrick Guelcher'
year = '2016'

@app.route('/')
def home():
    title = 'Home | Patrick Guelcher'
    description = 'Patrick Guelcher\'s home on the internet.'
    return render_template('pages/index.html', author=author, year=year, title=title, description=description)

@app.route('/about')
def about():
    title = 'About Me | Patrick Guelcher'
    description = 'About Patrick Guelcher.'
    return render_template('pages/about.html', author=author, year=year, title=title, description=description)

if __name__ == '__main__':
    app.run()

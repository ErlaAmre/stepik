from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tours')
def tour():
    return render_template('tour.html')

@app.route('/departure')
def departure():
    return render_template('departure.html')

app.run()

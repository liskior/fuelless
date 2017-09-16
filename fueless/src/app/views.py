import plotter
from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
@app.route('/map')
def ind():
    return "Map"

@app.route('/grafik')
def grafik():
     plotter.Plotter.draw()
@app.route('/')

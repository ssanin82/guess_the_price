from flask import Flask, render_template, request
from bokeh.embed import components
from numpy import cos, linspace
from bokeh.plotting import figure

app = Flask(__name__)


@app.route('/')
def index():
    x = linspace(-6, 6, 100)
    y = cos(x)
    p = figure(width=500, height=500)
    p.circle(x, y, size=7, color="firebrick", alpha=0.5)

    script, div = components(p)
    print(div)
    return render_template("index.html", script=script, div=div)


# With debug=True, Flask server will auto-reload
# when there are code changes
if __name__ == '__main__':
    app.run(port=5000, debug=True)

from flask import Flask, render_template
import pandas as pd
from datetime import datetime

from bokeh.embed import server_document
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.server.server import Server
from bokeh.themes import Theme

app = Flask(__name__)


def modify_doc(doc):
    """
    df = pd.read_csv('data/tsla.csv')[['Date', 'Adj Close']]
    df.set_index('Date', inplace=True)
    # source = ColumnDataSource(data=df)
    plot = figure(x_axis_type='datetime', y_range=(15, 300), y_axis_label='Adj Close',
                  title="Adjusted Close Price")
    plot.line([datetime.strptime(d, '%Y-%m-%d') for d in df.index], list(df['Adj Close']))
    """

    from bokeh.sampledata.stocks import AAPL
    df = pd.DataFrame(AAPL)
    df['date'] = pd.to_datetime(df['date'])

    # create a new plot with a datetime axis type
    p = figure(plot_width=800, plot_height=250, x_axis_type="datetime")
    p.line(df['date'], df['close'], color='navy', alpha=0.5)

    doc.add_root(p)
    doc.theme = Theme(filename="theme.yaml")


@app.route('/', methods=['GET'])
def bkapp_page():
    script = server_document('http://localhost:5006/bkapp')
    return render_template("embed.html", script=script, template="Flask")


def bk_worker():
    # Can't pass num_procs > 1 in this configuration. If you need to run multiple
    # processes, see e.g. flask_gunicorn_embed.py
    server = Server({'/bkapp': modify_doc}, allow_websocket_origin=["localhost:8000"])
    server.start()
    server.io_loop.start()


from threading import Thread
Thread(target=bk_worker).start()

if __name__ == '__main__':
    print('Opening single process Flask app with embedded Bokeh application on http://localhost:8000/')
app.run(port=8000, debug=True)
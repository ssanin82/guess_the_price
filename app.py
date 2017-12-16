import os
import dash
import flask
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt


STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = dash.Dash()


@app.server.route('/static/<resource>')
def serve_static(resource):
    return flask.send_from_directory(STATIC_PATH, resource)


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.css.append_css({
    "external_url": "static/some.css"
})

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=
[
    html.H1(children='Interactive Stock Predictor', style={'textAlign': 'center', 'color': colors['text']}),
    html.Div(children='Dash: A web application framework for Python.',
             style={'textAlign': 'center', 'color': colors['text']}),
    dcc.Graph(id='example-graph-2', figure=
    {
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
        ],
        'layout': {
            'plot_bgcolor': colors['background'],
            'paper_bgcolor': colors['background'],
            'font': {'color': colors['text']}
        }
    }),
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=dt(1997, 5, 3),
        end_date_placeholder_text='Select a date!'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt


class MyDash(dash.Dash):
    def index(self, *args, **kwargs):
        scripts = self._generate_scripts_html()
        css = self._generate_css_dist_html()
        config = self._generate_config_html()
        title = getattr(self, 'title', 'Dash')
        return ('''
        <!DOCTYPE html>
        <html style="background-color: black;">
            <head>
                <meta charset="UTF-8"/>
                <title>{}</title>
                {}
            </head>
            <body>
                <div id="react-entry-point">
                    <div class="_dash-loading">
                        Loading...
                    </div>
                </div>
            </body>

            <footer>
                {}
                {}
            </footer>
        </html>
        '''.format(title, css, config, scripts))


app = MyDash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.css.append_css({"external_url": './some.css'})
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

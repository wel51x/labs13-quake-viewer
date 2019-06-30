# dash app
# appropriated from https://www.datacamp.com/community/tutorials/learn-build-dash-python
# requires:
#   pip install dash==0.21.1
#   pip install dash-renderer==0.13.0
#   pip install dash-html-components==0.11.0
#   pip install dash-core-components==0.23.0
#   pip install plotly --upgrade

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
colors =\
    {
    'background': '#111111',
    'text': '#7FDBFF'
    }

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1
        (
        children='Quakespect - Analysis of Impact of Earthquakes on Financial Markets',
        style=
            {
            'textAlign': 'center',
            'color': colors['text']
            }
        ),
    html.Div(children='Dash app comparing performance of Gold and S&P 500 30 days after earhtquake event.', style=
        {
        'textAlign': 'center',
        'color': colors['text']
        }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {
                    'x': [6.7, 6.8, 6.9, 7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8, 8.1, 8.2, 8.3, 8.4, 8.6],
                    'y': [0.787557, 0.854592, 0.288289, 0.892119, 0.818553, 0.124668, 0.465835, 0.024738,
                          0.362847, 0.761823, -0.130923, 0.96838, 0.419737, 1.187691, 1.23051, 1.39488,
                          0.495057, 1.934919, 0.861004],
                    'type': 'bar', 'name': u'S&P 500'},
                {
                    'x':    [6.7, 6.8, 6.9, 7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8, 8.1, 8.2, 8.3, 8.4, 8.6],
                    'y':    [0.524222, 0.085566, 0.231729, -0.271789, 0.107205, 1.7547, 0.670126, 1.329997,
                             1.443031, 1.02111, 2.947221, 0.425903, 0.897363, 1.658656, 2.909621, -1.489643,
                             -0.097974, 2.311224, -1.255772],
                    'type': 'bar', 'name': 'Gold'
                },
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)  # debug=True ==>> no need to re-load after changing source

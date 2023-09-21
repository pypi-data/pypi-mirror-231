import pollination_dash_viewer
from dash import Dash, html, Input, State, Output, callback, dcc, ctx
import dash_daq as daq
from pathlib import Path
import dash_renderjson

app = Dash(__name__)

# From bytes to Base64
content = Path('./examples/factory.vtkjs').read_bytes()

app.layout = html.Div([
    # toolbar controller
    pollination_dash_viewer.VTKDashViewer(
        id='po-dash-viewer',
        content = content,
        subscribe=False,
        screenShotName='my-dash-screenshot',
        style={
            'height' : '500px',
            'border' : '2px solid #2ea8e0',
            'border-radius': '5px',
        }
    ),
    # extenal controllers
    html.Div([
    daq.ToggleSwitch(
        className='add-space',
        label='Enable Toolbar',
        id='daq-toggle-toolbar',
        value=True),
    daq.ToggleSwitch(
        className='add-space',
        label='Enable Sidebar',
        id='daq-toggle-sider',
        value=True),
    daq.ToggleSwitch(
        className='add-space',
        label='Enable Clear',
        id='daq-toggle-clear',
        value=True),
    daq.ToggleSwitch(
        className='add-space',
        label='Isolate Data',
        id='daq-isolate-data',
        value=False),
    daq.ToggleSwitch(
        className='add-space',
        label='Toogle Ortho',
        id='daq-toggle-ortho',
        value=False),
    daq.ColorPicker(
        id='color-picker',
        label='Background Color',
        size=256,
        labelPosition='bottom',
        value=dict(rgb=dict(r=255, g=255, b=255, a=1))
    ),
    html.Div([
        html.Button('Screenshot', id='btn-screenshot', n_clicks=0, className='add-space'),
        html.Button('Top View', id='btn-view', n_clicks=0, className='add-space'),
        html.Button('Change Legend Label', id='btn-legend', n_clicks=0, className='add-space'),
        html.Button('Reset Camera', id='btn-camera', n_clicks=0, className='add-space'),
    ], style={  
        'display': 'flex',
        'flex-direction': 'column',
    }),
    html.Div(id='output'),
    ], style={  
        'display': 'flex',
        'flex-direction': 'row',
    }),
])

def get_rbga(value):
    values = list(value.get('rgb').values())
    alpha = values[-1]
    values = [v / 255 for v in values[:-1]]
    values.append(alpha)
    return values

@callback(
    Output('po-dash-viewer', 'toolbar'),
    Input('daq-toggle-toolbar', 'value')
)
def update_toolbar_value(input_value):
    return input_value

@callback(
    Output('po-dash-viewer', 'sider'),
    Input('daq-toggle-sider', 'value')
)
def update_sider_value(input_value):
    return input_value

@callback(
    Output('po-dash-viewer', 'clear'),
    Input('daq-toggle-clear', 'value')
)
def update_clear_value(input_value):
    return input_value

@callback(
    Output('po-dash-viewer', 'actionStack'),
    [
        Input('daq-isolate-data', 'value'),
        Input('daq-toggle-ortho', 'value'),
        Input('color-picker', 'value'),
        Input('btn-screenshot', 'n_clicks'),
        Input('btn-view', 'n_clicks'),
        Input('btn-legend', 'n_clicks'),
        Input('btn-camera', 'n_clicks'),
    ]
     
)
def do_action_stack(isolate, ortho, color, *btn):
    if 'btn-screenshot' == ctx.triggered_id:
        return [{ 'type': 'dash-screenshot' }]
    elif 'btn-view' == ctx.triggered_id:
        return [{ 'type': 'select-view', 'value': 'top' }]
    elif 'btn-legend' == ctx.triggered_id:
        return [{ 'type': 'legend-label', 'value': 'My Data' }]
    elif 'btn-camera' == ctx.triggered_id:
        return [{ 'type': 'reset-camera' }]
    else:
        return [
            { 'type': 'isolate-data', 'value': not isolate },
            { 'type': 'toggle-ortho', 'value': ortho },
            { 'type': 'background-1', 'value': get_rbga(color) },
        ]

@app.callback(
    Output(component_id='output',
      component_property='children'),
    Input(component_id='po-dash-viewer',
      component_property='scene')
)
def set_children(scene):
    return dash_renderjson.DashRenderjson(id='json-out',
                                          data={ 'scene': scene })

if __name__ == '__main__':
    app.run_server(debug=True)

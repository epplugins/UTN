#
# License
#

import numpy as np
import plotly.graph_objects as go

def op_plot_03(y1, z=np.linspace(-2, 5, 500), N=500, Lmax=3.5, dL=0.01):
    fig = go.Figure()
    fig.update_layout(showlegend=False, width=850, height=450)
    fig.update_yaxes(automargin=False)
    fig.update_xaxes(title_text='z', titlefont=dict(size=18))
    fig.update_yaxes(title_text='E', titlefont=dict(size=18), title_standoff = 0)
    fig.update_yaxes(showticklabels=False)

    # Add traces
    # fig.add_trace(go.Scatter(x=z, y=yb, mode='lines'))

    # Add traces, one for each slider step
    for step in np.arange(0, Lmax, dL):
        fig.add_trace(
            go.Scatter(
                visible=False,
                mode='lines',
                name="haz",
                x=z,
                y=[y1(zi, step) for zi in z]))


    fig.add_shape(type="rect",
        xref="x", yref="y",
        x0=0, y0=-0.6,
        x1=2, y1=0.6,
        line_width=0,
        fillcolor="PaleTurquoise",
        opacity=0.4,
        # visible=False,
    )

    fig.add_shape(type="rect",
        xref="x", yref="y",
        x0=0, y0=-0.6,
        x1=2, y1=0.6,
        line=dict(
            color="LightSeaGreen",
            width=2,
        ),
        # visible=False,
    )


    # Make L=2 trace visible
    fig.data[int(2/dL)].visible = True
    # fig.layout['shapes'][int(2/dL*2)].visible = True
    # fig.layout['shapes'][int(2/dL*2+1)].visible = True

    # Create and add slider
    steps = []
    shapes = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            label=np.round(i*dL,2),
            args=[{"visible": [False] * len(fig.data)},
                {"shapes" : [
                    {
                    'fillcolor': 'PaleTurquoise',
                    'line': {'width': 0},
                    'opacity': 0.4,
                    'type': 'rect',
                    'visible': True,
                    'x0': 0,
                    'x1': np.round(i*dL,2),
                    'xref': 'x',
                    'y0': -0.6,
                    'y1': 0.6,
                    'yref': 'y'
                    },
                    {
                    'line': {'color': 'LightSeaGreen', 'width': 2},
                    'type': 'rect',
                    'visible': True,
                    'x0': 0,
                    'x1': np.round(i*dL,2),
                    'xref': 'x',
                    'y0': -0.6,
                    'y1': 0.6,
                    'yref': 'y'
                    }
                ] }],  # layout attribute
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=int(2/dL),
        len=0.5,
        x=2/7,
        currentvalue={"prefix": "Largo: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
        # shapes=shapes
    )

    fig.show(renderer='notebook')

    return fig

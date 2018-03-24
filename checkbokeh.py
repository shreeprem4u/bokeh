''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure

from bokeh.io import output_file, show


# Set up data	746430.47884,210409.99524	787730.20360,221660.00331
#N = 200
x = 750000.25688
y = 220000.25684
#x = np.linspace(0, 4*np.pi, N)
#y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
plot = figure(plot_height=400, plot_width=400, title="Staff Room",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[746430.47884, 787730.20360], y_range=[210409.99524, 221660.00331])

#plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
#plot.circle('x', 'y', source=source, size=5, color="red", alpha=0.5)
plot.circle('x', 'y', source=source, size=5, color="red", alpha=0.5)


# Set up widgets
text = TextInput(title="title", value='Select')
'''
offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0, step=0.1)
phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)
'''

# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)
'''
def update_data(attrname, old, new):

    # Get the current slider values
    a = amplitude.value
    b = offset.value
    w = phase.value
    k = freq.value

    # Generate the new curve
    x = x+1000+a+b+w+k
    y = y+1000+a+b+w+k

    source.data = dict(x=x, y=y)

for w in [offset, amplitude, phase, freq]:
    w.on_change('value', update_data)

'''
# Set up layouts and add to document
inputs = widgetbox(text, offset, amplitude, phase, freq)


curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Check"


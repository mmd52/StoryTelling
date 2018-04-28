import numpy as np
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure
from bokeh.charts import Area, show, output_file,Line

df=pd.read_csv("FB.csv")
#### We need only date , close and volume
df=df[['Date','Close','Volume']]
df=df[df['Date']>'2017-01-01']
df['Date']=pd.to_datetime(df['Date'])

source = ColumnDataSource(df)


# Set up plot
plot = figure(x_axis_type="datetime", x_axis_label='Date' , y_axis_label='Stock price ($)' ,plot_width=800, plot_height=350)
plot.line('Date', 'Close', source=source)


# Set up widgets
text = TextInput(title="title", value='my sine wave')
date1 = Slider(title="Start Month", value=1, start=1, end=17, step=1)
date2 = Slider(title="End Month", value=17, start=17, end=1, step=-1)


# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    a = date1.value
    b = date2.value
    
    print("Entered here")
    

for w in [date1, date2]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = widgetbox(text, date1,date2)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "FB"
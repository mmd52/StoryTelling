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

text = TextInput(title="Title 1", value='Facebook Graph')

def update_title(attrname, old, new):
    p.title.text = text.value

text.on_change('value', update_title)

source = ColumnDataSource(df)

p = figure(x_axis_type="datetime", x_axis_label='Date' , y_axis_label='Stock price ($)' ,plot_width=800, plot_height=350)
p.line('Date', 'Close', source=source)

inputs = widgetbox(text)
curdoc().add_root(row(inputs, p, width=800))

#output_file("ts.html")
#show(p)

curdoc().title = "Sliders"
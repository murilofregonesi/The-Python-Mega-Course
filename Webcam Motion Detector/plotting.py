from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool
import pandas
from datetime import datetime

df = pandas.read_csv('status.csv')

left = [datetime.strptime(point, '%Y-%m-%d %H:%M:%S.%f') for point in df["start"]]
right = [datetime.strptime(point, '%Y-%m-%d %H:%M:%S.%f') for point in df["finish"]]

f = figure(x_axis_type='datetime', height=200, width=1000, title="Motion Graph")
f.quad(left=left, right=right, top=1, bottom=0)

hover = HoverTool(tooltips=[
    ("Start", "@left"),
    ("Finish", "@right")
])

f.add_tools(hover)
f.xaxis.axis_label = "Datetime"
f.yaxis.axis_label = "Detection"

output_file('detection_plot.html')
show(f)
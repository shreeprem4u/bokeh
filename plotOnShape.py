import geopandas as gpd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool, LogColorMapper
import geopandas as gpd
import pandas as pd
# Let's first do some coloring magic that converts the color palet into map numbers (it's okey not to understand)
from bokeh.palettes import RdYlBu11 as palette
from bokeh.models import LogColorMapper
#import pysal as ps
import csv

# File path
DF_fp = r"/home/researcher/Documents/NewDemoRFID/staffroom_shape/staffroom.shp"

# Read the data
DF = gpd.read_file(DF_fp)
DF2 = gpd.read_file(DF_fp)

#print(DF.crs)

#print(DF.tail(5))


def getPolyCoords(row, geom, coord_type):
    """Returns the coordinates ('x' or 'y') of edges of a Polygon exterior"""

    # Parse the exterior of the coordinate
    exterior = row[geom].exterior

    if coord_type == 'x':
        # Get the x coordinates of the exterior
        return list( exterior.coords.xy[0] )
 


def getPolyCoords2(row, geom, coord_type):
    """Returns the coordinates ('x' or 'y') of edges of a Polygon exterior"""

    # Parse the exterior of the coordinate
    exterior = row[geom].exterior

    if coord_type == 'y':
        # Get the x coordinates of the exterior
        return list( exterior.coords.xy[1] )
 



# Get the Polygon x and y coordinates
DF['x'] = DF.apply(getPolyCoords, geom='geometry', coord_type='x', axis=1)
#DF2 = DF2.assign(y=DF.apply(getPolyCoords2, geom='geometry', coord_type='y', axis=1))
DF2['y'] = DF2.apply(getPolyCoords2, geom='geometry', coord_type='y', axis=1)


df = pd.concat([DF, DF2['y']], axis=1)
#print(df[['x', 'y']].head(2))


g_df = df.drop('geometry', axis=1).copy()
gsource = ColumnDataSource(g_df)


# Create the color mapper
color_mapper = LogColorMapper(palette=palette)


# Initialize our figure
p = figure(plot_width=1200, plot_height=800,title = "Academic Block 3 :Floor 1 StaffRoom")

# Plot grid	 fill_color = {'field': 'pt_r_tt_ud', 'transform': color_mapper},
p.patches('x', 'y', source = gsource,fill_color = "grey", fill_alpha = 0.7, line_color = "black", line_width = 0.05)


''' TESTING PORTION
file = open("/home/researcher/Documents/staffroom.csv", "r")
#fp = r"/home/researcher/Documents/staffroom.csv"

reader = csv.reader(file, delimiter=',')

# Read the data

data = pd.read_csv(fp, sep=';')
for x,y in data.values():
	x = data.x
	y = data.y
	p.circle(x='x',y='y',size=5, color="red", alpha=0.5)

for row in reader:
	x1 = row[:1]
	y1 = row[:2]
	print(x1)
	print(y1)
	p.circle(x='x1',y='y1',size=5, color="red", alpha=0.5)
'''

p.circle([754864.16427, 761821.38325, 766090.58580, 768620.48361, 774154.63507], [216825.57847, 215086.27372, 216983.69708, 212398.25730, 218881.12044], size=5, color="red", alpha=0.5)
# Save the figure

output_file("staffroom.html")
show(p)



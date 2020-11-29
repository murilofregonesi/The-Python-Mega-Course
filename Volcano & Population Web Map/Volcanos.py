'''
Volcano & Population Web Map

Created on November 2020
@author: Murilo Fregonesi Falleiros
'''

import folium

# Create a Map object
map = folium.Map(location = (39.746485836236104, -101.53238059442184), 
                 tiles = 'Stamen Terrain',
                 zoom_start = 4)

# Import Volcanos position
import pandas
volcanos = pandas.read_csv('Volcanos.txt')

# Create Volcanos markers
markers = folium.FeatureGroup(name='Markers') # Group of markers

def set_color(elevation):
    if elevation < 2000:
        return 'green'
    elif elevation < 3000:
        return 'blue'
    else:
        return 'red'

for name, lat, lon, ele in zip(volcanos.loc[:,'NAME'], 
                               volcanos.loc[:,'LAT'], 
                               volcanos.loc[:,'LON'], 
                               volcanos.loc[:,'ELEV']):
    #folium.Marker(location=(lat, lon), popup=name, icon=folium.Icon(color=set_color(ele))).add_to(markers)
    folium.CircleMarker(location=(lat, lon), radius=4, popup=name, color=set_color(ele)).add_to(markers)

# Areas GEO-JSON
geojson_data = open('world.json','r',encoding='utf-8-sig').read()

geoStyle = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20e6
                      else 'yellow' if x['properties']['POP2005'] < 50e6
                      else 'red'}
folium.GeoJson(data=geojson_data, style_function=geoStyle, name='Population').add_to(map)

map.add_child(markers)
map.add_child(folium.LayerControl())

# On Jupyter Notebook the Map can be visualized only by calling the object
# On IDEs, save it as HTML for visualization
map.save('Volcanos.html')

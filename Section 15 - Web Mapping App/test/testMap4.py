# String manipulation: Adding elevation data

import folium
import pandas

data = pandas.read_csv('Section 15 - Web Mapping App/mapping_data/Volcanoes.csv')

lat = list(data['LAT'])
lon = list(data['LON'])
names = list(data['NAME'])
elevs = list(data['ELEV'])
types = list(data['TYPE'])

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="Volcanoes")

for lt, ln, name, elev, tp in zip(lat, lon, names, elevs, types):
    desc = name + '\n' + str(elev) + 'm\n' + tp
    fg.add_child(folium.Marker(location=[lt, ln], popup=desc, icon=folium.Icon(color='red')))

map.add_child(fg)

map.save('Section 15 - Web Mapping App/test/testMap4.html')
print("Save successful!")
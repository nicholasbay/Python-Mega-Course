# HTML formatting for volcano data

import folium
import pandas

data = pandas.read_csv('Section 15 - Web Mapping App/mapping_data/Volcanoes.csv')

lat = list(data['LAT'])
lon = list(data['LON'])
names = list(data['NAME'])
elevs = list(data['ELEV'])
types = list(data['TYPE'])

map = folium.Map(location=[41.87, -116.12], zoom_start=5)

fg = folium.FeatureGroup(name="Volcanoes")

for lt, ln, name, elev, tp in zip(lat, lon, names, elevs, types):
    html = f"""
    <h4><a href="https://www.google.com/search?q={name}+volcano" target="_blank"> {name}</a> Information</h4>
    Height: {elev}m<br>
    Type: {tp}<br>
    Coordinates: {lt:.2f}&#176N, {ln:.2f}&#176E
    """
    iframe = folium.IFrame(html=html, width=250, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))

map.add_child(fg)

map.save('Section 15 - Web Mapping App/test/testMap5.html')
print("Save successful!")
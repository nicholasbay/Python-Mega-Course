# Adding multiple markers using for-loops

import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6)

# map.add_child(folium.Marker(location=[38.2, -99.1], popup="Marker!", icon=folium.Icon(color="purple")))
fg = folium.FeatureGroup(name='testMap1')

for coordinates in [[38.2, -99.1], [38, -99], [37.8, -98.9]]:
    fg.add_child(folium.Marker(location=coordinates, popup="This is a marker!", icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("Section 15 - Web Mapping App/test/testMap2.html")
print("Save successful!")
# Adding marker to created map

import folium
# Some bug with the 3rd party tiles (map does not show)
# map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles='Stamen Terrain', attr='<a href=https://endless-sky.github.io/>Endless Sky</a>')
map = folium.Map(location=[38.58, -99.09], zoom_start=6)

# map.add_child(folium.Marker(location=[38.2, -99.1], popup="Marker!", icon=folium.Icon(color="purple")))
fg = folium.FeatureGroup(name='testMap1')
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Marker0", icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[38, -99], popup="Marker1", icon=folium.Icon(color="purple")))
map.add_child(fg)

map.save("Section 15 - Web Mapping App/test/testMap1.html")
print("Save successful!")
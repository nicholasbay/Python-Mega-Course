# Adding population JSON data

import folium
import pandas

def main():
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
        fg.add_child(folium.CircleMarker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            tooltip=f'{name}',
            fill_color=color_code(elev),
            color='grey',
            fill_opacity=0.7))
        
    fg.add_child(folium.GeoJson(data=open('Section 15 - Web Mapping App/mapping_data/world.json', 'r', encoding='utf-8-sig').read()))

    map.add_child(fg)

    map.save('Section 15 - Web Mapping App/test/testMap8.html')
    print("Save successful!")


def color_code(elev):
    if elev >= 0 and elev < 1000:
        return 'green'
    elif elev >= 1000 and elev < 2000:
        return 'orange'
    elif elev >= 2000 and elev < 3000:
        return 'pink'
    else:
        return 'darkred'
    

if __name__ == '__main__':
    main()
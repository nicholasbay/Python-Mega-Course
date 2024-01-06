# Layer control

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

    # Volcano layer
    fg_volcanoes = folium.FeatureGroup(name="Volcanoes")
    for lt, ln, name, elev, tp in zip(lat, lon, names, elevs, types):
        html = f"""
            <h4><a href="https://www.google.com/search?q={name}+volcano" target="_blank"> {name}</a> Information</h4>
            Height: {elev}m<br>
            Type: {tp}<br>
            Coordinates: {lt:.2f}&#176N, {ln:.2f}&#176E
            """
        iframe = folium.IFrame(html=html, width=250, height=100)
        fg_volcanoes.add_child(folium.CircleMarker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            tooltip=f'{name}',
            fill_color=elev_color(elev),
            color='grey',
            fill_opacity=0.7))
        
    # Country layer
    fg_countries = folium.FeatureGroup(name="Population")
    fg_countries.add_child(folium.GeoJson(data=open('Section 15 - Web Mapping App/mapping_data/world.json', 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor':pop_color(x['properties']['POP2005']), 'fillOpacity':0.5}))

    map.add_child(fg_countries)
    map.add_child(fg_volcanoes)
    map.add_child(folium.LayerControl())

    map.save('Section 15 - Web Mapping App/test/testMap10.html')
    print("Save successful!")


def elev_color(elev):
    if elev >= 0 and elev < 1000:
        return 'green'
    elif elev >= 1000 and elev < 2000:
        return 'orange'
    elif elev >= 2000 and elev < 3000:
        return 'pink'
    else:
        return 'darkred'
    

def pop_color(pop):
    # Light green
    if pop >= 0 and pop < 1_000_000:
        return '#AED581'
    # Green
    elif pop >= 1_000_000 and pop < 10_000_000:
        return '#1B5E20'
    # Orange
    elif pop >= 10_000_000 and pop < 100_000_000:
        return '#FB8C00'
    # Light red (pink)
    elif pop >= 100_000_000 and pop < 1_000_000_000:
        return '#F48FB1'
    # Red
    elif pop >= 1_000_000_000:
        return '#FF1744'
    

if __name__ == '__main__':
    main()
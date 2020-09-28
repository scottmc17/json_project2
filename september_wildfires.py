## JSON PROJECT 
import json

sept_in_file = open('US_fires_9_1.json', 'r')

sept_out_file = open('bspet_fire_data.json', 'w')

sept_data = json.load(sept_in_file)

json.dump(sept_data, sept_out_file, indent = 4)

blons, blats, bbrightness = [], [], []


for x in sept_data:
    lon = x['longitude']
    lat = x['latitude']
    bright = x['brightness']
    blons.append(lon)
    blats.append(lat)
    if bright > 450:
        bbrightness.append(bright)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [{
    'type' : 'scattergeo',
    'lon' : blons,
    'lat' : blats,
    'marker' : {
        'size' : [.05 * bright for bright in bbrightness],
        'color' : bbrightness,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Brightness'}
    },
}]

my_layout = Layout(title= 'Fires')

fig = {'data' : data, 'layout' : my_layout}

offline.plot(fig, filename = 'beg_sept_fires.html')

#display fig
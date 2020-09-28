import json

in_file = open('eq_data_30_day_m1.json', 'r')

out_file = open('readable_eq_data.json', 'w')

eq_data = json.load(in_file)

json.dump(eq_data, out_file,indent = 4)

list_of_eqs = eq_data['features']

print(type(list_of_eqs))

print(len(list_of_eqs))

mags, lons, lats = [], [], []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)



print("Mags")
print(mags[:10])

print("Lons")
print(lons[:10])

print("Lats")
print(lats[:10])




from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#data = [Scattergeo(lon = lons, lat = lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Magnitude'}

    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='global_earthquakes.html')
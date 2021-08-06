import geocoder
import pprint

#pos = (35.46383,139.513031)
pos = (35.659025,139.745025)
g = geocoder.osm(pos,method='reverse')
pprint.pprint(g.json)


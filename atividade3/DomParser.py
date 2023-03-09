from xml.dom.minidom import parse
import time
ini = time.time()

MapDocument = parse('map.osm')

print("Starting DOM Parser...")
nodes = []
for c in MapDocument.getElementsByTagName("node"):	
	tag = c.getElementsByTagName("tag")
	node = dict()
	for t in tag:
		if t.getAttribute("k") == "name":
			node["name"] = t.getAttribute("v")
		if t.getAttribute("k") == "amenity":
			node["amenity"] = t.getAttribute("v")
	node["lat"] = c.getAttribute("lat")
	node["lon"] = c.getAttribute("lon")
	if node.get("amenity"):
		nodes.append(node)

for node in nodes:
	print("name:", node.get("name"), "amenity:",node.get("amenity"), "lat:", node.get("lat"), "lon", node.get("lon"))
fim = time.time()
print("\nTime =", fim-ini)
		
		

		


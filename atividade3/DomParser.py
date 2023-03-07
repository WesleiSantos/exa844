from xml.dom.minidom import parse
import time
ini = time.time()

MapDocument = parse('map.osm')

print("Starting DOM Parser...")
for c in MapDocument.getElementsByTagName("node"):	
	tag = c.getElementsByTagName("tag")
	amenity = ""
	for t in tag:
		if t.getAttribute("k") == "name" and amenity:
			print("name: ", t.getAttribute("v"))
			print("lat: ", c.getAttribute("lat"))
			print("lon: ", c.getAttribute("lon"))
			print("")
		if t.getAttribute("k") == "amenity":
			amenity = t.getAttribute("v")
			print("amenity: ", amenity)

fim = time.time()
print("\nTime =", fim-ini)
		
		

		


import xml.sax
import time
import json
class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.lat = ""
    self.lon= ""
    self.name = ""
    self.amenity = ""
    self.feature = []

  def startElement(self, tag, attributes):    
    self.currentData = ""
    if tag =="node":  
      self.lon = attributes.get("lon")
      self.lat = attributes.get("lat")
      self.amenity = ""
      self.name = ""
    if tag == "tag":
      self.currentData = attributes.get("k")
      if self.currentData == "name":
        self.name = attributes.get("v")
      if self.currentData == "amenity":
        self.amenity = attributes.get("v")

  def endElement(self, tag):    
    if tag == "node":
      if self.amenity:
        feature = {"type": "Feature", "properties": {"name": self.name, "type": self.amenity}, "geometry": {"type": "Point", "coordinates": [float(self.lon), float(self.lat)]}}
        self.feature.append(feature)

  def characters(self, content):	
    self.currentData += content
  
  def getFeature(self):
    return self.feature

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")

features = Handler.getFeature()
geoJson = {"type": "FeatureCollection", "features": features}

jsonStr = json.dumps(geoJson,  indent=4, ensure_ascii=False)

print(jsonStr)


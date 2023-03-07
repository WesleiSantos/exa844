import xml.sax
import time

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.lat = ""
    self.lon= ""
    self.name = ""
    self.amenity = ""

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
        print("name: ", self.name )
        print("amenity: ", self.amenity)
        print("lat: ", self.lat)
        print("lon: ", self.lon)
        print("")

  def characters(self, content):	
    self.currentData += content

ini = time.time()
parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")


fim = time.time()
print("\nTime =", fim-ini)
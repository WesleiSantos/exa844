import urllib.request
from bs4 import BeautifulSoup
import webbrowser

urls=[]
with open("seeds.txt") as file:
    for line in file:
      urls.append(line)
aux = ''
for url in urls:
  page = urllib.request.urlopen(url)
  html = str(page.read().decode('utf-8'))
  soup = BeautifulSoup(html, 'lxml')
  title = soup.title.string
  print("Título:", soup.title.string)
  img = soup.find_all('img')
  if img:
    src = str(img[0].attrs.get("src"))
    if (src.startswith("https") or src.startswith("http")):
      aux = aux + ("<li><h1>"+title+"</h1><img width='278' height='278' src='"+src+"'></li>")
    else:
      aux = aux + ("<li><h1>"+title+"</h1><img width='278' height='278' src='"+url+src+"'></li>")
    print("img: ", src)

f = open('index.html','w')

message = "<html><head></head><body><ul>"+aux+ "</ul></body></html>"

f.write(message)
f.close()

#Altere o caminho para refletir a localização do ficheiro
filename = 'index.html'
webbrowser.open_new_tab(filename)

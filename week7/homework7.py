import json
import pprint
import xml.etree.ElementTree as ET



# 2. Access the nested key ‘salary’ from the following JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
print(json.loads(sampleJson)["company"]["employee"]["payble"]["salary"])

print("vehicle*****************************************************************")

# 3. Convert the following Vehicle Object into JSON. Is there a better way (format) to save this class? If yes, write a programm to that convertation also.

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
    def __str__(self):

        jdict={}
        self.dict=jdict
        jdict["name"]=self.name
        jdict["engine"] = self.engine
        jdict["price"]=self.price
        return (json.dumps(jdict,indent=4))
    def makedict(self):
            return (json.loads(self.__str__()))

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
print(vehicle)

# 4. Implement the reverse convertion of previous task
print(vehicle.makedict())

# 5. Read 'movies.xml' file with ElementTree parser and print root's and its children's tags and attributes.

tree = ET.parse('movies.xml')
root = tree.getroot()
print(root.tag,root.attrib)
for child in root:
    print(child.tag, child.attrib)

print("*****************************************************************")
# 6. Get a list of all tag names in the data in an order that they appear.

tags=[root.tag]
for i in root:
    tags.append(i.tag)
    for j in i:
        tags.append(j.tag)
        for k in j:
            tags.append(k.tag)
            for n in k:
                tags.append(n.tag)

print([x for i, x in enumerate(tags) if i == tags.index(x)])


print("******************************************************************")

# 7. Get attributes of movies that came out in 1992
for movie in root.iter('movie'):
    if movie.find('year').text=="1992":
        print(movie.attrib, movie.find('year').text)
        
        
# another way

for movie in root.findall("./genre/decade/movie/[year='1992']"):
      print(movie.attrib, movie.find('year').text)

print("*******************************************************************")

# 8. Get attributes of movies that are available in multiple formats


for movie in root.iter('movie'):
    name = movie.attrib
    format = movie.find('format').attrib
    if format == {'multiple': 'Yes'}:
        print(name, format)
      
# another way

for x in root.findall("./genre/decade/movie/format/[@multiple='Yes'].."):
    print(x.attrib)

print("*********************************************************")

# 9. Change movie title from "Back 2 the Future" to "Back to the Future".

for movie in root.iter('movie'):
    if movie.get('title') == "Back 2 the Future":
         movie.set("title", "Back to the Future")

    tree.write('output.xml')
   
   
print("*********************************************************")

# 10. If you look carefully, 'multiple' attribute is written wrongly in some cases. Find a way to fix it.

for format in root.findall("./genre/decade/movie/format"):
    # print(form.attrib, form.text)
    if format.attrib=={'multiple': 'False'}:
        format.set('multiple','No')
tree.write('output.xml')



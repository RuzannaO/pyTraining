import json
import pprint
import xml.etree.ElementTree as ET

1. Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
mydict={1:"A",9:"B",3:{15:"Hello",16:(67,True)}}
print(json.dumps(mydict, sort_keys=True, indent=4))


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

print("*****************************************************************")

# 3. Convert the following Vehicle Object into JSON. Is there a better way (format) to save this class? If yes, write a programm to that convertation also.

def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Vehicle':
           return Vehicle(obj['name'], obj['engine'],obj['price'])
    return obj

class Vehicle(object):
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
        # self. __type__="Vehicle"

    def __str__(self):
        return (json.dumps(self.__dict__))

def back_to_obj(a):
    b = json.loads(a.__str__())
    b["__type__"] = "Vehicle"
    return json.loads(json.dumps(b),object_hook=object_decoder)


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
print(vehicle.__str__())

# 4. Implement the reverse convertion of previous task
# implementation in the above task

b=vehicle.__str__()
new_obj=back_to_obj(b)
print(new_obj.name)

# 5. Read 'movies.xml' file with ElementTree parser and print root's and its children's tags and attributes.

tree = ET.parse('movies.xml')
root = tree.getroot()
print(root.tag,root.attrib)
for child in root:
    print(child.tag, child.attrib)

print("*****************************************************************")
# 6. Get a list of all tag names in the data in an order that they appear.

tags=[root.tag]
for i in root.iter():
    tags.append(i.tag)


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
    if format.attrib=={'multiple': 'False'}:
        format.set('multiple','No')
    if len(format.text.split(","))>1:
        format.set('multiple','Yes')
    else:
        format.set('multiple','No')
for format in root.findall("./genre/decade/movie/format"):
    print(format.attrib,format.text)
tree.write('output.xml')


# 11. Some of the data has been placed in the wrong decade. Find and fix the decade data errors. Save new document with all this changes to a new .xml file.

# define elements that are in wrong decades
dict={'1970s':[1970,1979],'1980s':[1980,1989],'1990s':[1990,1999],'2000s':[2000,2009]}
for  decade in root.iter('decade'):
    name=movie.attrib
    for year in decade.iter("year"):

            if int(year.text)>dict[decade.attrib['years']][1] or int(year.text)<dict[decade.attrib['years']][0]:
                print(decade.attrib, year.text)


#two movies(X-men and Pycho) are in wrong decades.

# create a new decade under genre category ='Action', with attribute 'year='2000s', and append it with "X-men"
new_dec = ET.SubElement(root.find("./genre[@category='Action']"), 'decade')
new_dec.attrib["years"] = '2000s'
# decade2000s=root.find("./genre[@category='Action']/decade[@years='2000s']")

xmen = root.find("./genre/decade/movie[@title='X-Men']")
new_dec.append(xmen)
# decade2000s.append(xmen)

# remove "X-men" from the wrong decade (years='1990s')

root.find("./genre/[@category='Action']/decade[@years='1990s']").remove(xmen)

# create a new decade under genre category ='Thriller', with attribute 'year='2000s', and append it with "Psycho"

new_dec_thr = ET.SubElement(root.find("./genre[@category='Thriller']/"), 'decade')
new_dec_thr.attrib['years']='2000s'
psycho=root.find("./genre/decade/movie[@title='American Psycho']")
new_dec_thr.append(psycho)

# remove "X-men" from the wrong decade (years='1990s')

root.find("./genre[@category='Thriller']/decade[@years='1980s']").remove(psycho)

# print(ET.tostring(root, encoding='utf8').decode('utf8'))

tree.write('output.xml')

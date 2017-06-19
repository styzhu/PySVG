import xml.etree.ElementTree as ET
import os

svg_ns = '{http://www.w3.org/2000/svg}'

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
origin_file = os.path.join(THIS_FOLDER, 'test.svg')
#origin_file = os.path.join(THIS_FOLDER, 'example.xml')
tree = ET.parse(origin_file)
root = tree.getroot()
g = root.find(svg_ns + 'g')

for rect in g.findall(svg_ns+'rect'):
    print rect.attrib


'''
for child in svg:
    print child.tag, child.attrib
'''

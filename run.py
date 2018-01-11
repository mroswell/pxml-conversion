import os, base64
import xml.etree.ElementTree as et

import csv

ns = {'p': 'http://www.palantirtech.com/pg/schema/import/'}
count = 0

def process(filepath):
    ret = []
    ret.append(path)

    tree = et.parse(filepath)
    root = tree.getroot()
    ret.append('' if root.find('.//p:propertyComponent[@type="TITLE"]/p:propertyData', ns) == None else root.find('.//p:propertyComponent[@type="TITLE"]/p:propertyData', ns).text)
    ret.append('' if root.find('.//p:noteData', ns) == None else root.find('.//p:noteData', ns).text)
    ret.append('' if root.find('.//p:propertyData', ns) == None else root.find('.//p:propertyData', ns).text)

    medias = root.findall('.//p:media[@mediaType="Text File"]', ns)
    for media in medias:
        ret.append('' if media.attrib['mediaType'] == None else media.attrib['mediaType'])
        ret.append('' if media.find('./p:mediaTitle', ns) == None else media.find('./p:mediaTitle', ns).text)
        ret.append('' if media.find('./p:mediaData', ns) == None else media.find('./p:mediaData', ns).text)
        dataSourceRecordNode = media.find('.//p:dataSourceRecord', ns)
        if dataSourceRecordNode != None:
            ret.append(et.tostring(dataSourceRecordNode))
        else:
            ret.append('')
    return ret

data = []
    
for root,dirs,files in os.walk('../xml'):
    for file in files:
        path = root + '/' + file
        if path.endswith('.xml'):
            print (path)
            ret = process(path)
            data.append(ret)
            count += 1
            print (ret)

with open('output.csv', 'w', encoding='utf8') as csvfile:
    w = csv.writer(csvfile, delimiter=',', quotechar = '"', quoting=csv.QUOTE_NONNUMERIC )
    headerwriter = csv.DictWriter(open('output.csv','wt'), ['filename', 'title', 'noteData', 'propertyData', 'mediaType', 'mediaTitle', 'mediaData', 'dataSourceRecord'])
    headerwriter.writeheader()

    for line in data:
        w.writerow(line)

print (count)

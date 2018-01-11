#!/usr/bin/env python
#  coding: utf8

import os
import xml.etree.ElementTree as et
import base64
import csv

ns = {'p': 'http://www.palantirtech.com/pg/schema/import/'}
count = 0


def process(filepath):
    tree = et.parse(filepath)
    root = tree.getroot()

    ret = []
    ret.append(filepath)
    ret.append('' if root.find('.//p:propertyComponent[@type="TITLE"]/p:propertyData', ns) is None else root.find(
        './/p:propertyComponent[@type="TITLE"]/p:propertyData', ns).text)
    ret.append('' if root.find('.//p:noteData', ns) is None else root.find('.//p:noteData', ns).text)
    ret.append('' if root.find('.//p:propertyData', ns) is None else root.find('.//p:propertyData', ns).text)

    medias = root.findall('.//p:media[@mediaType="Text File"]', ns)
    for media in medias:
        ret.append('' if media.attrib['mediaType'] is None else media.attrib['mediaType'])
        ret.append('' if media.find('./p:mediaTitle', ns) is None else media.find('./p:mediaTitle', ns).text)

        orig_text = '' if media.find('./p:mediaData', ns) is None else media.find('./p:mediaData', ns).text
        ret.append(orig_text)
        text_utf = base64.b64decode(orig_text)
        ret.append(text_utf)
        text_decoded = text_utf.decode('utf8')
        ret.append(text_decoded)

        dataSourceRecordNode = media.find('.//p:dataSourceRecord', ns)
        if dataSourceRecordNode is not None:
            ret.append(et.tostring(dataSourceRecordNode))
        else:
            ret.append('')
    return ret


data = []

for root, dirs, files in os.walk('../xml'):
    for file in files:
        path = root + '/' + file
        # Exclude extraneous xml files created by PyCharm IDE
        if path.endswith('.xml') and '.idea' not in path:
            processed = process(path)
            data.append(processed)
            count += 1
            print (processed)

with open('output.csv', 'w', encoding='utf-8') as csvfile:
    w = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    headers = ['filename', 'title', 'noteData', 'propertyData', 'mediaType', 'mediaTitle', 'mediaData',
               'mediaData_utf8', 'mediaData_decoded', 'dataSourceRecord']
    headerwriter = csv.DictWriter(open('output.csv', 'wt'), headers)
    headerwriter.writeheader()

    for line in data:
        w.writerow(line)

print (count)

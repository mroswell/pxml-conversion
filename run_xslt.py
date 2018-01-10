import os
from lxml import etree

directory = "../xml/0/0/9"

"""
for roots, dirs, files in os.walk(directory):
    for dir in dirs:
        print "Dir= %s" % dir
    for file in files:
        print "File= %s" % file
"""

files = next(os.walk(directory))[2]

def transform_data(source_etree, stylesheet):
    xslt = etree.parse(stylesheet)
    transform = etree.XSLT(xslt)
    new_dom = transform(source_etree)
    return new_dom

style_xml = etree.parse('phr_xslt.xslt')
for file in files:
    ext = os.path.splitext(file)[-1].lower()
    if ext == ".xml":
        with open(directory+"/"+file, 'r') as rf:
            print rf.name
            xfile = etree.parse(rf)
            with open("output.csv", 'a') as wf:
                result = transform_data(xfile, 'phr_xslt.xslt')
                result_text = str(result)
                # result.write_output('file.csv')
                wf.write(result_text)

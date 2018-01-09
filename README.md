# pxml-conversion

## Notes

* The data is in palantir XML format, or pXML.
* This is a good overview of this format
https://www.slideshare.net/palantirtech/palantir-xml-formats

* Likewise, here’s a lecture on this format (using the slides above):
https://www.youtube.com/watch?v=NfoPmkIH0Kk&feature=youtu.be
(I haven’t watched the whole thing yet.)

* (100% of gender references in the Palantir XML documentation above are male. This is pretty standard. Extremely rare to find anything other than 100% of gender references is training documentation being male. Palantir is true to form, here.)

* This documentation mentions XSLT numerous times as the developer-friendly way to interact with pXML

* XSLT is for transforming XML documents
* For instance, we could write one template to go from pXML to CSV, while another template could go directly from pXML to Kobo XML
* XSLT version 2 lets you set a default namespace. Version 1 requires you to create a prefix the namespace to all node

* Python has a module (Pyana) for running XSLT transformations on XML. I haven’t used it yet.
* Thousands of repos use it, for instance: https://github.com/search?q=import+Pyana+&type=Code&utf8=%E2%9C%93
* Pyana also appears in the O’Reilly Python Cookbook
https://www.safaribooksonline.com/library/view/python-cookbook/0596001673/ch12s05.html

* xsltproc is a command line XSLT processor installed by default on a mac
* xsltproc template.xslt data.xml > output.txt
or
* xslstproc -o output.csv template.xslt data.xml
* xsltproc only covers version 1 of XSLT


* Many other options besides Python and xsltproc for viewing XSLT transformations:
(Many editors allow you to apply XSLT to xml, as well,  but I’m just using xsltproc so far.)
* Stylus is a standard XSLT IDE, but it only runs on Windows, and it’s expensive
* Xmplify is probably a good tool for working with XSLT/Xpath on a mac.
* Chrome doesn’t allow you to apply an XSLT file to XML, but other browsers do. But the fact that palantir had its own namespace, meant browser viewing of XSLT transforms doesn’t work by default directly in a browser. (Without the custom namespace, in a more generic XML file, could just load the XML file into the browser, and have it apply the template. Probably a way to do that, but I didn’t figure out how, so I gave up on what I thought would be a quick browser display.

* xPath allows you to access specific content in an XML document.
* xPath is sophisticated, allowing access to tags, nested tags, attributes, formulas, and related-family nodes (child, parent, first, last, sibling, etc.)
* xPath is not zero-indexed. so the first child would be, for instance note[1]

* XML can be standardized either according to a DTD or an XSD. pXML probably has an XML Schema Definition (XSD) that would help us better understand the structure of these files. For instance, to learn if more than one note is allowed or not.
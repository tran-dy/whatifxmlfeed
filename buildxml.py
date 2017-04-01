import xml.etree.ElementTree as ET
ET.register_namespace("","http://www.w3.org/2005/Atom")

#prefix for atom feed
feed = ET.Element('feed')
title = ET.SubElement(feed, 'title')
title.set("type", "text")
title.text = "What If?"
id = ET.SubElement(feed, 'id')
id.text = "http://what-if.xkcd.com/feed.atom"
link = ET.SubElement(feed, 'link')
link.set("href", "http://what-if.xkcd.com/feed.atom")
link.set("rel", "self")
author = ET.SubElement(feed, 'author')
name = ET.SubElement(author, 'name')
name.text = "xkcd"
email = ET.SubElement(author, 'email')
email.text = "whatif@xkcd.com"
icon = ET.SubElement(feed, 'icon')
icon.text = "http://what-if.xkcd.com/imgs/favicon.ico"
logo = ET.SubElement(feed, 'logo')
logo.text = "http://what-if.xkcd.com/imgs/favicon.ico"
subtitle = ET.SubElement(feed, 'subtitle')
subtitle.set("type", "text")
subtitle.text = "Answering your hypothetical questions with physics, every Tuesday."

#print ET.tostring(feed)

tree = ET.parse("testfeed.xml")
root = tree.getroot()
entries = root.findall('{http://www.w3.org/2005/Atom}entry')
for entry in entries:
	feed.append(entry)
#print ET.dump(feed)

ET.ElementTree(feed).write("testoutput.xml")
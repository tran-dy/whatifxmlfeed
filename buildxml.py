import xml.etree.ElementTree as ET
import json
import urllib2
ET.register_namespace("","http://www.w3.org/2005/Atom")

# prefix for atom feed
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

# print ET.tostring(feed)

# tree = ET.parse("testfeed.xml")

# tree = ET.ElementTree(file = urllib2.urlopen(xml_url))
# root = tree.getroot()
# entries = root.findall('{http://www.w3.org/2005/Atom}entry')
# for entry in entries:
	# feed.append(entry)
	
# ET.ElementTree(feed).write("testoutput.xml")

timestamps = ['20170328', '20170110', '20161107', '20160329', '20160218', '20160128', '20150920', '20150726', '20150328', '20150227', '20150205', '20150207', '20150115', '20141218', '20141126', '20141017', '20140924', '20140829', '20140730', '20140712', '20140625', '20140601', '20140505', '20140408', '20140325', '20140225', '20140208', '20140114', '20131218', '20131127', '20131115', '20131023', '20131009', '20130904', '20130815', '20130805', '20130704', '20130610', '20130519', '20130425', '20130408', '20130326', '20130317', '20130219', '20130131', '20130116', '20130112', '20121220', '20121212', '20121121', '20121105', '20121009', '20120918', '20120828', '20120809', '20120717']
for time in timestamps:
	time_url = 'http://archive.org/wayback/available?url=https://what-if.xkcd.com/feed.atom&timestamp={date}'.format(date = time)
	result = json.load(urllib2.urlopen(time_url))
	xml_url = str(result['archived_snapshots']['closest']['url'])
	tree = ET.ElementTree(file = urllib2.urlopen(xml_url))
	root = tree.getroot()	
	entries = root.findall('{http://www.w3.org/2005/Atom}entry')
	for entry in entries:
		feed.append(entry)

ET.ElementTree(feed).write("testoutput_long.xml")
		

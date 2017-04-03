import json
import urllib2
import xml.etree.ElementTree as ET

url = 'http://archive.org/wayback/available?url=https://what-if.xkcd.com/feed.atom'

time_url = 'http://archive.org/wayback/available?url={https://what-if.xkcd.com/feed.atom}&timestamp={timestamp}'.format(timestamp = '201602')

result = json.load(urllib2.urlopen(time_url))

# result['archived_snapshots']['closest']['url']
xml_url = str(result['archived_snapshots']['closest']['url'])


tree = ET.ElementTree(file = urllib2.urlopen(xml_url))
root = tree.getroot()
entries = root.findall('{http://www.w3.org/2005/Atom}entry')

timestamps = ['20170328', '20170110', '20161107', '20160329', '20160218', '20160128', '20150920', '20150726', '20150328', '20150227', '20150205', '20150207', '20150115', '20141218', '20141126', '20141017', '20140924', '20140829', '20140730', '20140712', '20140625', '20140601', '20140505', '20140408', '20140325', '20140225', '20140208', '20140114', '20131218', '20131127', '20131115', '20131023', '20131009', '20130904', '20130815', '20130805', '20130704', '20130610', '20130519', '20130425', '20130408', '20130326', '20130317', '20130219', '20130131', '20130116', '20130112', '20121220', '20121212', '20121121', '20121105', '20121009', '20120918', '20120828', '20120809', '20120717']
import urllib
import xml.etree.ElementTree as ET

sum=0
while True:
    serviceurl = 'http://python-data.dr-chuck.net/comments_295062.xml'
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('.//count')
    for item in results:
      print 'Count:',item.text
      sum = sum+int(item.text)
    
    print 'Sum:',sum
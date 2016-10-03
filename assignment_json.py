import urllib
import json

sum=0
while True:
    serviceurl = 'http://python-data.dr-chuck.net/comments_295066.json'
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    url = address
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    strdata = uh.read()
    print 'Retrieved',len(strdata),'characters'
    data = json.loads(strdata)
    commentslst=data['comments']
    print 'Count :',len(commentslst)
    for item in commentslst:
     sum = sum+int(item['count'])
    
    print 'Sum:',sum

#use http://python-data.dr-chuck.net/comments_42.html
#and http://python-data.dr-chuck.net/comments_295065.html for testing
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
for tag in tags:
    Contents=tag.contents[0]
    count = count+(int(Contents))
print count
    
   
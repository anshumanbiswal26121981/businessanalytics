# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
#use http://python-data.dr-chuck.net/known_by_Fikret.html for testing
import urllib  
from BeautifulSoup import *  
url = raw_input('Enter URL ')  
count = raw_input('Enter count: ')  
count = int(count)  
pos = raw_input('Enter position: ')  
pos = int(pos)-1  
html = urllib.urlopen(url).read()  
seq = ''
lstr=list()  
for i in range(0,count):  
   soup = BeautifulSoup(html)  
   tags = soup('a')  
   seq = seq + tags[pos].contents[0]+' ' 
   lstr.append(tags[pos].contents[0]) 
   html = urllib.urlopen(tags[pos].get('href', None)).read()  
print"Sequence of names- ", seq 
len=len(lstr) 
print "Last name is ", lstr[len-1]
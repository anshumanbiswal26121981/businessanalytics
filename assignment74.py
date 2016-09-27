fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
names = list()
for line in fh:
 if line.startswith('From '):
  words=line.split(' ')
  names.append(words[1])

 for name in names:  
  counts[name] = counts.get(name,0) + 1  
print counts  

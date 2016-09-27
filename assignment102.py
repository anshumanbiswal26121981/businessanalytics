fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
hours = list()
for line in fh:
 if line.startswith('From '):
  words=line.split(' ')
  time=words[6].split(':')
  hours.append(time[0])

for hour in hours:  
 counts[hour] = counts.get(hour,0) + 1  
for k in sorted(counts):
 print k,counts[k]
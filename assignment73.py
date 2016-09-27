fname = raw_input("Enter file name: ")
fh = open(fname)
lst=[]
for line in fh:
 linesplit=line.rstrip().split(' ')
 for words in linesplit:
	if words not in lst:
	 lst.append(words)
lst.sort()
print lst

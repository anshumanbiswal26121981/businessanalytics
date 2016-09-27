# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
totalfloat = 0
for line in fh:
 if not line.startswith("X-DSPAM-Confidence:") : 
  continue
 stringstr = line
 newstr=stringstr.strip()
 print newstr
 splitstr = newstr.split(":")
 num = splitstr[1].strip()
 floatnum = (float)(num)
 totalfloat=totalfloat+floatnum
 count = count+1
average = totalfloat/count
msg = "Average spam confidence: "+ str(average)
print msg
print "Done"
import re
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "assignment_data.txt"
fh = open(fname)
sum=0

for line in fh:
 numbers=re.findall('\d+',line.strip())
 for num in numbers:
  if num.isdigit:
   sum = sum + int(num)
print sum

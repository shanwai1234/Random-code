import sys

myfile = sys.argv[1]
outfile = sys.argv[2]
a = open(myfile,'r')
b = open(outfile,'w')
head = a.readline().split('\t')
mydict = {'R':'A G','Y':'C T','S':'G C','W':'A T','K':'G T','M':'A C','N':'0 0'}
nf = []
for line in a:
	new = line.strip().split('\t')
	total = len(new)
	nf.append(line)
a.close()

for num in range(16,total):
	snp = []
	for line1 in nf:
		new = line1.strip().split('\t')
		if new[num] in mydict:
			snp.append(mydict[new[num]])
		else:
			snp.append(new[num]+' '+new[num])
	final = ""
	for m in snp:
		final += m+'  '
	b.write('FAM001'+' '+head[num]+' '+'0'+' '+'0'+' '+'0'+'  '+'-9'+'  '+final+'\n')
a.close()
b.close()

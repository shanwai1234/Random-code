import sys

myfile = sys.argv[1]
outfile = sys.argv[2]
a = open(myfile,'r')
b = open(outfile,'w')
head = a.readline().split('\t')
mydict = {'R':'A G','Y':'C T','S':'G C','W':'A T','K':'G T','M':'A C'}
nf = []
for line in a:
	new = line.strip().split('\t')
	total = len(new)
	nf.append(line)
a.close()

for num in range(12,total):
	s = ''
	final = ''
	name = ''
	for line1 in nf:
		new = line1.strip().split('\t')
		alt = new[num]
		ref = new[11]
		if alt == ref:
			s = '0'
		elif alt in mydict:
			s = '1'
		elif alt == 'N':
			s = 'NA'
		else:
			s = '2'
		name += new[0]+' ' 
		final += s+' '
	if num == 12:
		b.write('FID'+' '+'IID'+' '+'PAT'+' '+'MAT'+' '+'SEX'+' '+'PHENOTYPE'+' '+name+'\n')
	b.write(head[num]+' '+head[num]+' '+'0'+' '+'0'+' '+'0'+' '+'-9'+' '+final+'\n')
b.close()

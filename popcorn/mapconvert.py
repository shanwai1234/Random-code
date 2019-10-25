import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
a = open(input_file,'r')
b = open(output_file,'w')
a.readline()

for line in a:
	new = line.strip().split('\t')
	b.write(new[2]+' '+new[0]+' '+'0'+' '+new[3]+'\n')

a.close()
b.close()


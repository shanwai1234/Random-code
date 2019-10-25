fh = open("second_filter_file.txt",'r')
cf = open("B73_9_snp.txt",'w')
#cf.write('#chrom'+'\t'+'chromStart'+'\t'+'chromEnd'+'\t'+'name'+'\t'+'gieStain'+'\n')
color_lookup = {
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'red': (255, 0, 0),
}
for line in fh:
	newline = []
	line = line.strip().split(',')
	if line[15] == 'N':continue
	if line[15] == 'X':continue 
	if line[15] == line[4]:
		name = "B73_9"+line[4]
		stain = 'blue' 
	elif line[15] == line[5]:
		name = "B73_9"+line[5]
		stain = 'yellow'
	else:
		name = "B73_9"+line[4]+"/"+line[5]
		stain = 'red'
#	newline[0] = line[2]
#	newline[1] = str(int(line[3])-1) 
#	newline[2] = line[3]
#	newline[3] = name
#	newline[4] = stain
	newline = ['chr'+line[2],str(int(line[3])-1),line[3],name,stain]
	cf.write("\t".join(newline)+'\n')
fh.close()
cf.close()

	


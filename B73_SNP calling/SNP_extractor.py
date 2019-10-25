import sys
# python SNP_extractor.py B73_1_R3 9
filename = sys.argv[1]
column = int(sys.argv[2])
fh = open("snp_statistic_30datasets_maffilter_v3_final.txt",'r')
myfile = open("{0}_MAF_v3_final.fasta".format(filename),'w')
myfile.write('\n'+'>'+filename+'\n')
count = 0
for line in fh:
#	if count != 10:
#        	count += 1
#        	continue
#	else:
#		count = 0
	new = line.strip().split(',')
	if new[column] == 'X' or new[column] == new[4]+'/'+new[5]:
		new[column] = 'N'
	myfile.write(new[column])
fh.close()
myfile.close()	
	

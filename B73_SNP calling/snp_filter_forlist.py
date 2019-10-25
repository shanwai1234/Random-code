fh = open("snp_statistic_30datasets_v3_final_ann.txt",'r')
myfh = open("snp_statistic_30datasets_maffilter_v3_final_ann.txt",'w')
for line in fh:
	line = line.strip().split(',')
	test_set = set(line[6:35])
	if len(test_set) < 2: continue
	if float(line[-2]) > 0.20: continue
        if float(line[-4]) < 0.017: continue
        if float(line[-4]) > 0.98: continue
        if not line[5] in test_set: continue
        if not line[4] in test_set: continue
	myfh.write(','.join(line)+'\n')
myfh.close()
fh.close()

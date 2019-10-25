import numpy as np
import matplotlib.pyplot as plt
import sys

a = sys.argv[1]
ped = open(a,'r')

hm = []
ht = []
miss = []
name = []
count = 0
for line in ped:
	new = line.strip().split(',')
	name.append(new[0])
	hm.append(float(new[1]))
	ht.append(float(new[2]))
	miss.append(float(new[3]))
	count += 1
ped.close()
hm = np.array(hm)
ht = np.array(ht)
miss = np.array(miss)
#wid = len(count)
N = count
ind = np.arange(N)    # the x locations for the groups
width = 1       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, hm, width, color='r',edgecolor=None)
p2 = plt.bar(ind, ht, width, color='y',edgecolor=None,
             bottom=hm)
p3 = plt.bar(ind, miss, width, color='b',edgecolor=None,bottom=hm+ht)

#plt.figure(figsize=(18,3))
plt.ylabel('Proportion')
plt.title('Proportion of snp type in pop population')
plt.xticks(ind + width/2., name, rotation='270', size='4.5')
plt.yticks(np.arange(0, 1, 0.1))
#plt.legend((p1[0], p2[0]), ('Men', 'Women'))
plt.axis('tight')
plt.savefig('image1.svg')

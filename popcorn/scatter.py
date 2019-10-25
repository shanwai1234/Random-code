import numpy as np
import matplotlib.pyplot as plt
import sys

a = sys.argv[1]
#b = sys.argv[2]

csv = open(a,'r')
#out = open(b,'w')

name_h = []
name_c = []
name_u = []
name_n = []
gh_x = []
gh_y = []
gc_x = []
gc_y = []
gu_x = []
gu_y = []
gn_x = []
gn_y = []
for line in csv:
	new = line.strip().split(',')
	if new[-1] == 'USDA':
		gu_x.append(float(new[1]))
		gu_y.append(float(new[2]))
	elif new[-1] == 'CAG':
		gc_x.append(float(new[1]))
		gc_y.append(float(new[2]))
	elif new[-1] == 'HOLDING':
		gh_x.append(float(new[1]))
		gh_y.append(float(new[2]))
	else:
		gn_x.append(float(new[1]))
		gn_y.append(float(new[2]))
x1 = np.array(gu_x)
y1 = np.array(gu_y)
x2 = np.array(gc_x)
y2 = np.array(gc_y)
x3 = np.array(gh_x)
y3 = np.array(gh_y)
x4 = np.array(gn_x)
y4 = np.array(gn_y)
#area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

csv.close()
plt.scatter(x1, y1, s=30, c='red', alpha=1,label='USDA')
plt.scatter(x2, y2, s=30, c='green', alpha=1, label='CAG')
plt.scatter(x3, y3, s=30, c='blue', alpha=1, label='Holding')
plt.scatter(x4, y4, s=30, c='yellow', alpha=1, label='mix')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()

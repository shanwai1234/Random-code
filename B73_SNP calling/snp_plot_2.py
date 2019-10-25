from matplotlib import pyplot as plt
from matplotlib.collections import BrokenBarHCollection
import pandas
import os 

def chromosome_collections(df, y_positions, height,  **kwargs):
    del_width = False
    if 'width' not in df.columns:
        del_width = True
        df['width'] = df['end'] - df['start']
    for chrom, group in df.groupby('chrom'):
        print chrom
        yrange = (y_positions[chrom], height)
        xranges = group[['start', 'width']].values
        yield BrokenBarHCollection(
            xranges, yrange, edgecolors=df['colors'],facecolors=df['colors'], **kwargs)
    if del_width:
        del df['width']

chrom_height = 0.2
chrom_spacing = 13
gene_height = 0.1
gene_padding = 0.05
figsize = (12,20)
chromosome_list = ['chr%s' % i for i in range(1, 11)]

ybase = -1.0
chrom_ybase = {}
gene_ybase = {}
chrom_centers = {}

for chrom in chromosome_list[::-1]:
    chrom_ybase[chrom] = ybase
    chrom_centers[chrom] = ybase + chrom_height / 2.
    gene_ybase[chrom] = ybase - gene_height - gene_padding - 1.0
    ybase += chrom_height + chrom_spacing

ideo = pandas.read_table(
    'ideogram.txt',
#    skiprows=1,
    names=['chrom', 'start', 'end', 'name', 'gieStain']
)

ideo = ideo[ideo.chrom.apply(lambda x: x in chromosome_list)]
ideo['width'] = ideo.end - ideo.start

color_lookup = {
    'blue': 'blue',
    'yellow': 'yellow',
    'red': 'red',
    'white': '.5'
}

ideo['colors'] = ideo['gieStain'].apply(lambda x: color_lookup[x])

myfolder = 'B73_11datasets_new10_uf'
myfile = os.listdir("B73_11datasets_new10_uf")
blist = []
tlist = ['B73_10','B73_11_m','B73_12','B73_1_R3','B73_2_R1','B73_3_R1','B73_4','B73_5_R1','B73_6','B73_7_R4','B73_8','B73_9']

for snp in sorted(myfile):
        blist.append(myfolder+'/'+snp)

#blist = [blist[0],blist[5]]
#tlist = [tlist[0],tlist[5]]

fig = plt.figure(figsize=figsize)

for newfile in sorted(blist):
	ax = fig.add_subplot(1,1,1)
	for chrom in chromosome_list:
		genes = pandas.read_table(
    		newfile,
    		names=['chrom', 'start', 'end', 'name','gieStain']) 
		genes = genes[genes.chrom.apply(lambda x: x in chromosome_list)]
		genes['width'] = genes.end - genes.start
		genes['colors'] = genes['gieStain']
	print("adding genes...")
	for collection in chromosome_collections(genes, gene_ybase, gene_height):
                ax.add_collection(collection)
        for chrom in chromosome_list[::-1]:
        	gene_ybase[chrom] -= 1.0

label_list = []
for x in chromosome_list[::-1]:
        label_list.append(x)
        for y in sorted(tlist):
                label_list.append(x+y)
name_list = []
for x1 in chromosome_list[::-1]:
	name_list.append(x1)
	for y1 in sorted(tlist):
		name_list.append(y1)

label_lib = {}
for a in chromosome_list[::-1]:
        label_lib[a] = chrom_centers[a]
	var = 0
        for b in sorted(tlist):
                label_lib[a+b] = label_lib[a] - gene_height - gene_padding - var - 1.0
                var += 1.0

print("adding ideograms...")
for collection in chromosome_collections(ideo, chrom_ybase, chrom_height):
    ax.add_collection(collection)

ax.set_yticks([label_lib[i] for i in label_list])
ax.tick_params(axis='y', labelsize=8)
ax.set_yticklabels(name_list)
ax.axis('tight')
plt.show()

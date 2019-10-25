from matplotlib import pyplot as plt
from matplotlib.collections import BrokenBarHCollection
import pandas
#import sys
import os
#import svgutils.transform as sg

#python snp_plot.py newfile
#newfile = sys.argv[1]

def chromosome_collections(df, y_positions, height,  **kwargs):
    del_width = False
    if 'width' not in df.columns:
        del_width = True
        df['width'] = df['end'] - df['start']
    print df.groupby('chrom')
    for chrom, group in df.groupby('chrom'):
        print chrom
        yrange = (y_positions[chrom], height)
        xranges = group[['start', 'width']].values
	print yrange
        yield BrokenBarHCollection(
            xranges, yrange, edgecolors=df['colors'],facecolors=df['colors'], **kwargs)
    if del_width:
        del df['width']

chrom_height = 1
chrom_spacing = 1
gene_height = 0.4
gene_padding = 0.1
figsize = (12,16)
chromosome_list = ['chr%s' % i for i in range(1, 11)]
#print chromsome_list
ybase = 0
chrom_ybase = {}
gene_ybase = {}
chrom_centers = {}

#here could be added with more lines in order to illustrate more figures together
myfolder = 'B73_11datasets_new10_uf'
myfile = os.listdir("B73_11datasets_new10_uf")
blist = []
tlist = []
for snp in sorted(myfile):
	blist.append(myfolder+'/'+snp)
	tlist.append(snp)
count = 0

print sorted(list(myfile))
fig = plt.figure(figsize=figsize)
for f in blist:
	count += 1
	for chrom in chromosome_list[::-1]:
	    chrom_ybase[chrom] = ybase
	    chrom_centers[chrom] = ybase + chrom_height / 2.
	    gene_ybase[chrom] = ybase - gene_height - gene_padding
	    ybase += chrom_height + chrom_spacing

	ideo = pandas.read_table(
    	'ideogram.txt',
#    skiprows=1,
    	names=['chrom', 'start', 'end', 'name', 'gieStain']
	)
#print ideo
	ideo = ideo[ideo.chrom.apply(lambda x: x in chromosome_list)]
	ideo['width'] = ideo.end - ideo.start

	color_lookup = {
    	'blue': 'blue',
    	'yellow': 'yellow',
    	'red': 'red',
    	'white': '.5'
	}

	ideo['colors'] = ideo['gieStain'].apply(lambda x: color_lookup[x])
#print ideo

	genes = pandas.read_table(
    	f,
    	names=['chrom', 'start', 'end', 'name','gieStain']) 
#print genes
	genes = genes[genes.chrom.apply(lambda x: x in chromosome_list)]
	genes['width'] = genes.end - genes.start
	genes['colors'] = genes['gieStain']
#print genes

	ax = fig.add_subplot(4,4,count)

	print("adding ideograms...")
	for collection in chromosome_collections(ideo, chrom_ybase, chrom_height):
    		ax.add_collection(collection)

	print("adding genes...")
	for collection in chromosome_collections(genes, gene_ybase, gene_height):
		print gene_ybase
    		ax.add_collection(collection)

#print genes[:1]
#print ideo[:1]
#	fig.subtitle(f,fontsize=16)
#	txt1 = sg.TextElement(25,20, "A", size=12, weight="bold")
#	fig.append(txt1)
	ax.set_title(tlist[count-1])
	ax.set_yticks([chrom_centers[i] for i in chromosome_list])
	ax.set_yticklabels(chromosome_list)
	ax.axis('tight')
plt.show()

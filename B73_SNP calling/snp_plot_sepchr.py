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
        yield BrokenBarHCollection(
            xranges, yrange, edgecolors=df['colors'],facecolors=df['colors'], **kwargs)
    if del_width:
        del df['width']

chrom_height = 0.5
chrom_spacing = 8
gene_height = 0.2
gene_padding = 0.5
figsize = (12,16)
chromosome_list = ['chr%s' % i for i in range(1, 11)]
#print chromsome_list
ybase = 0
chrom_ybase = {}
gene_ybase = {}
chrom_centers = {}

#here could be added with more lines in order to illustrate more figures together
myfolder = 'B73_24datasets_v3'
myfile = os.listdir("B73_24datasets_v3")
blist = []
tlist = []
for snp in sorted(myfile):
	blist.append(myfolder+'/'+snp)
count = 0
tlist = ['B73_11','B73_12','B73_1','B73_2','B73_3','B73_4','B73_5','B73_6','B73_7','B73_8','B73_9','B73_13','B73_14','B73_15','B73_16','B73_17','B73_18','B73_19','B73_20','B73_22','B73_23','B73_24','B73_25','B73_26']
name_origin = {'1':'CHN_Beijing_Lai','10':'CHN_Beijing_Chen','11':'CHN_Beijing_Wang','12':'CHN_Beijing_Xie','13':'USA_MN_Springer','14':'USA_MI_Buell','15':'USA_DE_Li','16':'USA_NY_Frank','17':'USA_NY_Scanlon','18':'USA_NE_Zhang','19':'USA_IA_Becraft','2':'USA_NY_Eveland','20':'USA_NY_Ware','21':'USA_WI_Doebley','22':'CHN_Beijing_Deng','23':'USA_MO_Brutell','24':'USA_AR_Grene','25':'USA_CA_Hake','26':'USA_FL_Kang','3':'USA_IA_Schnable','4':'DEU_Cologne_Urbany','5':'DEU_Bonn_Hochholdinger','6':'USA_NE_Schnable','7':'USA_MO_Givan'}

file_origin = {'1':'B73_14_24datasets_v3.txt','10':'B73_3_24datasets_v3.txt','11':'B73_4_24datasets_v3.txt','12':'B73_18_24datasets_v3.txt','13':'B73_1_24datasets_v3.txt','14':'B73_8_24datasets_v3.txt','15':'B73_17_24datasets_v3.txt','16':'B73_16_24datasets_v3.txt','17':'B73_25_24datasets_v3.txt','18':'B73_15_24datasets_v3.txt','19':'B73_2_24datasets_v3.txt','2':'B73_23_24datasets_v3.txt','20':'B73_20_24datasets_v3.txt','21':'B73_15_24datasets_v3.txt','22':'B73_19_24datasets_v3.txt','23':'B73_11_24datasets_v3.txt','24':'B73_22_24datasets_v3.txt','25':'B73_13_24datasets_v3.txt','26':'B73_24_24datasets_v3.txt','3':'B73_9_24datasets_v3.txt','4':'B73_6_24datasets_v3.txt','5':'B73_7_24datasets_v3.txt','6':'B73_12_24datasets_v3.txt','7':'B73_26_24datasets_v3.txt'}
keylist = file_origin.keys()
keylist.sort()

keylist2 = name_origin.keys()
keylist2.sort()

print sorted(list(myfile))
fig = plt.figure(num=None, figsize=(12, 20), dpi=300, facecolor='w', edgecolor='k')
for chrom in chromosome_list:
	chr_list = []
	label_list = []
	name_list = []
	label_lib = {}
	chrom_ybase[chrom] = ybase
	chrom_centers[chrom] = ybase + chrom_height / 2.
	gene_ybase[chrom] = ybase - gene_height - gene_padding
#	ybase += chrom_height + chrom_spacing
	count += 1
	chr_list.append(chrom)
	label_list.append(chrom)
	label_lib[chrom] = chrom_centers[chrom]
	for y in sorted(tlist):
                label_list.append(chrom+y)
	name_list.append(chrom)
	for y1 in keylist2:
		name_list.append(name_origin[y1])
	for f in keylist:
	    newfile = (myfolder+'/'+file_origin[f])
	    ideo = pandas.read_table(
    	    'ideogram.txt',
#    skiprows=1,
    	    names=['chrom', 'start', 'end', 'name', 'gieStain']
	    )
#print ideo
	    ideo = ideo[ideo.chrom.apply(lambda x: x in chr_list)]
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
    	    newfile,
    	    names=['chrom', 'start', 'end', 'name','gieStain']) 
#print genes
	    genes = genes[genes.chrom.apply(lambda x: x in chr_list)]
	    genes['width'] = genes.end - genes.start
	    genes['colors'] = genes['gieStain']
#	    print gene_ybase[chrom]
	    fig.subplots_adjust(bottom = 0.1, top = 0.9, hspace = 0.4, wspace = 0.3)
	    ax = fig.add_subplot(5,2,count)
	    print("adding genes...")
            for collection in chromosome_collections(genes, gene_ybase, gene_height):
                ax.add_collection(collection)
	    gene_ybase[chrom] -= 0.5

	var = 0
	for b in sorted(tlist):
	    label_lib[chrom+b] = label_lib[chrom] - gene_height - gene_padding - var - 0.2
	    var += 0.5
	ax.set_yticks([label_lib[i] for i in label_list])
	ax.tick_params(axis ='y', labelsize=5)
	ax.set_yticklabels(name_list)
	print("adding ideograms...")
	for collection in chromosome_collections(ideo, chrom_ybase, chrom_height):
    		ax.add_collection(collection)

#print genes[:1]
#print ideo[:1]
#	fig.subtitle(f,fontsize=16)
#	txt1 = sg.TextElement(25,20, "A", size=12, weight="bold")
#	fig.append(txt1)
	ax.set_title(chrom)
#	ax.set_yticklabels(chromosome_list)
	ax.axis('tight')
plt.show()

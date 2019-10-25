from matplotlib import pyplot as plt
import matplotlib 
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
gene_height = 0.1
gene_padding = 0.5
#figsize = (16,12)
chromosome_list = ['chr%s' % i for i in range(1, 7)]
#print chromsome_list
ybase = 0
chrom_ybase = {}
gene_ybase = {}
chrom_centers = {}

#here could be added with more lines in order to illustrate more figures together
myfolder = 'B73_30datasets_v3_final'
myfile = os.listdir("B73_30datasets_v3_final")
blist = []
tlist = []
for snp in sorted(myfile):
	blist.append(myfolder+'/'+snp)
count = 0
tlist = ['B73_11','B73_12','B73_1','B73_2','B73_3','B73_4','B73_5','B73_6','B73_7','B73_8','B73_9','B73_14','B73_15','B73_16','B73_17','B73_18','B73_19','B73_20','B73_22','B73_23','B73_24','B73_26','B73_27','B73_28','B73_29','B73_30','B73_31','B73_33','B73_34','B73_35']
name_origin ={'1':'USA_NE_Schnable','10':'USA_MO_Givan','11':'DEU_Cologne_Urbany','12':'USA_WI_Kappler2','13':'USA_IA_Schnable','14':'DEU_Bonn_Hochholdinger','15':'USA_MN_Springer_2','16':'USA_AR_Grene','17':'CHN_Beijing_Deng','18':'USA_MO_Brutnell','19':'USA_IA_Schnable_2','2':'USA_MI_Buell_2','20':'USA_NE_Schnable_2','21':'USA_MO_Brutnell_2','22':'USA_FL_Kang','23':'USA_NY_Evaland','24':'USA_WI_Doebley','25':'USA_NE_Zhang','26':'USA_CA_Hake','27':'USA_DE_Li','28':'USA_NY_Frank','29':'USA_NY_Ware','3':'USA_IA_Bercraft','4':'USA_MN_Springer','5':'USA_MI_Buell','6':'USA_WI_Kappler','7':'CHN_Beijing_Xie','8':'CHN_Beijing_Lai','9':'CHN_Beijing_Chen','90':'CHN_Beijing_Wang'}

file_origin = {'1':'B73_12_30datasets_v3.txt','10':'B73_26_30datasets_v3.txt','11':'B73_6_30datasets_v3.txt','12':'B73_34_30datasets_v3.txt','13':'B73_9_30datasets_v3.txt','14':'B73_7_30datasets_v3.txt','15':'B73_27_30datasets_v3.txt','16':'B73_22_30datasets_v3.txt','17':'B73_19_30datasets_v3.txt','18':'B73_11_30datasets_v3.txt','19':'B73_29_30datasets_v3.txt','2':'B73_28_30datasets_v3.txt','20':'B73_35_30datasets_v3.txt','21':'B73_30_30datasets_v3.txt','22':'B73_24_30datasets_v3.txt','23':'B73_23_30datasets_v3.txt','24':'B73_15_30datasets_v3.txt','25':'B73_5_30datasets_v3.txt','26':'B73_31_30datasets_v3.txt','27':'B73_17_30datasets_v3.txt','28':'B73_16_30datasets_v3.txt','29':'B73_20_30datasets_v3.txt','3':'B73_2_30datasets_v3.txt','4':'B73_1_30datasets_v3.txt','5':'B73_8_30datasets_v3.txt','6':'B73_33_30datasets_v3.txt','7':'B73_18_30datasets_v3.txt','8':'B73_14_30datasets_v3.txt','9':'B73_3_30datasets_v3.txt','90':'B73_4_30datasets_v3.txt'}
keylist = file_origin.keys()
keylist.sort()

keylist2 = name_origin.keys()
keylist2.sort()

print sorted(list(myfile))
matplotlib.rcParams['xtick.major.size'] = 0
matplotlib.rcParams['xtick.minor.size'] = 0
matplotlib.rcParams['ytick.major.size'] = 0
matplotlib.rcParams['ytick.minor.size'] = 0

fig = plt.figure(num=None, figsize=(16, 12), dpi=300, facecolor='w', edgecolor='k')
#fig = plt.figure(figsize=figsize)

for chrom in chromosome_list:
	count += 1
	ax = fig.add_subplot(3,2,count)
	chr_list = []
	label_list = []
	name_list = []
	label_lib = {}
	chrom_ybase[chrom] = ybase
	chrom_centers[chrom] = ybase + chrom_height / 2.
	gene_ybase[chrom] = ybase - gene_height - gene_padding
#	ybase += chrom_height + chrom_spacing
	chr_list.append(chrom)
#	label_list.append(chrom)
	label_lib[chrom] = chrom_centers[chrom]
	for y in sorted(tlist):
                label_list.append(y)
#	name_list.append(chrom)
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
	    mylength = int(ideo['end'])
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
	    fig.subplots_adjust(bottom = 0.1, top = 0.9, hspace = 0.2, wspace = 0.12)
#	    ax = fig.add_subplot(5,2,count)
	    print("adding genes...")
            for collection in chromosome_collections(genes, gene_ybase, gene_height):
                ax.add_collection(collection)
	    gene_ybase[chrom] -= 0.3

	if count%2 != 0 or count == 1:
		var = 0
		for b in sorted(tlist):
	    		label_lib[b] = label_lib[chrom] - gene_height - gene_padding - var - 0.2
	    		var += 0.3
		ax.set_yticks([label_lib[i] for i in label_list])
		ax.tick_params(axis ='y', labelsize=6)
		ax.set_yticklabels(name_list)
	else:
		var = 0
                for b in sorted(tlist):
                        label_lib[b] = label_lib[chrom] - gene_height - gene_padding - var - 0.2
                        var += 0.3
                ax.set_yticks([label_lib[i] for i in label_list])
		ax.set_yticklabels([])
	
	xtick_list = []
	xtick_label = []
	for pos in range(0,mylength,50000000):
		xtick_list.append(pos)
		xtick_label.append("{0}".format(pos/1000000))
	if count == 5:
		label = plt.xlabel("Megabases")
		ax.xaxis.set_label_coords(1.06,-0.08)

	ax.set_xticks(xtick_list)
	ax.set_xticklabels(xtick_label)
	ax.set_title("Chromosome {0}".format(count))
	ax.set_ylim([-9.6,-0.2])
	ax.set_xlim([0,mylength])
#	ax.set_yticklabels(chromosome_list)
#	ax.axis('tight')
plt.show()

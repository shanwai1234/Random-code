#requires two files, the input to fast structure and the "meanQ" file
#example command
#python alternative_distruct.py /home/jschnable/software/fastStructure-master/panicum80v2.str test.8.meanQ

#loading libraries
import sys
import numpy as np
import matplotlib.pyplot as plt
import brewer2mpl
import matplotlib as mpl

#setting parameters that will influence how matplotlib draws the final image
mpl.rcParams['patch.linewidth'] = 0
mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['xtick.minor.size'] = 0
mpl.rcParams['ytick.major.size'] = 0
mpl.rcParams['ytick.minor.size'] = 0
mpl.rcParams['xtick.labelsize'] = '4.5'

#parsing input files
ifile = sys.argv[1]
qfile = sys.argv[2]
#ofile = sys.argv[3]
#out = open(ofile,'w')

#reads in the names list from the input file
nlist = []
for x in open(ifile):
    y = x.strip().split(' ')
    nlist.append(y[1])

#corrects for the fact that in the "str" format there are two lines for each individual by only taking every second line    
n2list = nlist[::2]

#reading in the meanQ file
qlist = []
for x in open(qfile):
    y = x.strip().split('  ')
    qlist.append(map(float,y))
    popn = len(y)

#combining sample names with the meanQ values (ie the predicted contribution from each ancestral population to each group)
ml = []
for n,v in zip(nlist,qlist):
    t = [n]
    t.extend(v)
    ml.append(t)

#for nf in ml:
#	for a in nf:
#		out.write(str(a)+' ')
#	out.write('\n')

#print "Done!"

subsort = []
for x in range(popn):
    subsort.append([])

#splits up the samples based on which inferred ancestral genepool made the largest contribution to that sample
for asample in ml:
    myvals = asample[1:]
    myvals.sort()
    mymax = myvals[-1]
    for zind,z in enumerate(asample[1:]):
        if z == mymax:
            subsort[zind].append(asample)
            break

#sorts the data based on how "pure" each sample is. In other words, sorting by what genepool made the biggest contribution
for x in range(popn):
    subsort[x].sort(key=lambda a:a[x+1])
    subsort[x].reverse()

#puts all the samples back together in one big list in the order they will be displayed    
final_order = []
for x in subsort:
    for asample in x:
        final_order.append(asample)


#splits up the data into a number of different lists.

#This is the names in the order they'll be plotted
mynames = []

#This is a list of lists, and within each list, we have the contribution of a particular population to each sample in the order they'll be plotted
pop_vals = []
for x in range(popn):
    pop_vals.append([])
for asample in final_order:
    mynames.append(asample[0])
    for zind,z in enumerate(asample[1:]):
        pop_vals[zind].append(z)

#for stacked bar plots, we need to tell matplot lib both the length of the bar and where to start drawing the bar. "bottoms" is the list we used to keep track of that.
bottoms = []
for x in range(len(mynames)):
    bottoms.append(0)
       
#now it's time to start actually drawing the figure        
fig = plt.figure()
ax = fig.add_subplot('111')
ind = np.arange(len(mynames))

#for some reason, matplotlib wanted to make all the different bars blue, which wasn't very informative. I'm using the ColorBrewers colors instead.
bmap = brewer2mpl.get_map("Set3","Qualitative",popn)
mycolors = bmap.mpl_colors

#Plots the stacked bars for each of the inferred ancestral genepools one after the next
for x in range(popn):
    ax.bar(ind,pop_vals[x],width=1,bottom=bottoms,color=mycolors[x])
    #each time we update "bottoms" so that for each sample, it reflects the sum of the contributions of all the previously plotted populations. This keeps the bars from overlapping
    for zind,z in enumerate(pop_vals[x]):
        bottoms[zind] = bottoms[zind] + pop_vals[x][zind]

#This tells matplotlib where we want to draw labels (one under each sample).
ax.set_xticks(ind+.5)
#This tells matplotlib what we'd like to call each sample
ax.set_xticklabels(mynames,rotation='270')
#plt.tight_layout()
plt.axis('tight')
plt.show()

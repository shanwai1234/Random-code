import os
import subprocess as sp
import sys

def call_SNPs(mylist):
    mycount = mylist[0]
    mychr = mylist[1]
    mystart = mylist[2]
    mystop = mylist[3]
    fh = open("SNP_list/temp.var.raw.{0}.bcf".format(mycount),'w')
    snp_call = sp.Popen('samtools mpileup -I -F 0.01 -r {2}:{3}-{4} -uf {0} {1} | bcftools call -mv -Vindels -Ob'.format(fasta_reference," ".join(blist),mychr,mystart,mystop),shell=True,stdout=fh)
    snp_call.wait()
    fh.close()
#    print fh

#What you need to do
#1. Define fasta_reference to post to the maize fasta file you aligned against
#2. Make a list of the paths to the sorted BAM files for the 10 datasets you analyzed can tall it "blist"
#3. Make a list of all the regions in the genome you want to call SNPs for
#Example

#val1 = sys.argv[1]
ef = open("exon_region.txt","r")
initial = []
for n in ef:
        initial.append(n.rstrip().split(','))
temp = []
for x in range(1,11):
        temp.append(str(x))
good_chromosomes = set(temp)
ef.close()
snp_call_list = []
for m in initial:
        if not m[1] in good_chromosomes: continue
        m = map(int,m)
        snp_call_list.append(m)

bam_folder = 'Bam_files'
fasta_reference = '/home/zliang/storage/maize_10/Zea_mays.AGPv3.22.dna_rm.genome.fa'
myfiles = os.listdir("./{0}".format(bam_folder))
#myfiles = os.listdir("./{0}".format(bam_folder))
blist = []
for x in myfiles:
	if not x[-3:] == 'bam':continue
	blist.append(bam_folder + "/" + x)
#'/home/zliang/storage/maize_10/B73_2_R1/B73_2_R1_results-sorted.bam','/home/zliang/storage/maize_10/B73_3_R1/B73_3_R1_results-sorted.bam','/home/zliang/storage/maize_10/B73_4/B73_4_results-sorted.bam','/home/zliang/storage/maize_10/B73_5_R1/B73_5_R1_results-sorted.bam','/home/zliang/storage/maize_10/B73_6/B73_6_results-sorted.bam','/home/zliang/storage/maize_10/B73_4_R4/B73_7_R4_results-sorted.bam','/home/zliang/storage/maize_10/B73_8/B73_8_results-sorted.bam','/home/zliang/storage/maize_10/B73_9/B73_9_results-sorted.bam','/home/zliang/storage/maize_10/B73_10/B73_10_results-sorted.bam']
from multiprocessing import Pool

p = Pool(15)
p.map(call_SNPs,snp_call_list)
"""
    fh = open("samtools_snps/temp.var.raw.{0}.bcf".format(count),'w')
    snp_call = sp.Popen('samtools mpileup -m 50 -F 0.1 -r {2}:{3}-{4} -uf {0} {1} | bcftools call -mv -Vindels -Ob'.format(fasta_reference,' '.join(blist),mychr,mystart,mystop),shell=True,stdout=fh)
    snp_call.wait()
    fh.close()
"""

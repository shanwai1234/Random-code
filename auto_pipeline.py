import sys
import os
import subprocess as sp

a = sys.argv[1]
mfold = os.listdir(a)
for line in mfold:
	fq = '{0}/{1}'.format(a,line)
	data = line.replace('.fastq','')
	trim = sp.Popen(['java','-jar','/work/schnablelab/zliang4/Trimmomatic-0.38/trimmomatic-0.38.jar','SE','-threads','10','-phred33',fq,'{0}_trim.fastq'.format(a),'LEADING:3','TRAILING:3','SLIDINGWINDOW:4:15','MINLEN:36'])
	trim.wait()
	sam_file = open('{0}.sam'.format(a),'w')
	gsnap = sp.Popen(['gsnap','-D','./','-d','../AGPv4','--nthreads=12','-B','4','-N','1','-n','2','-Q','--nofails','--format=sam','{0}_trim.fastq'.format(a)], stdout=sam_file)
	gsnap.wait()
	sam_file.close()
	bam_out = open('{0}.bam'.format(data),'w')
	samt = sp.Popen(['samtools','view','-bS','{0}.sam'.format(a)],stdout=bam_out)
	samt.wait()
	bam_out.close()
	samt_s = sp.Popen(['samtools','sort','{0}.bam'.format(data),'-O','BAM','-o','{0}_sort.bam'.format(data)])
	samt_s.wait()
#	cuff = sp.Popen(['cufflinks','-p','12','-G','../Zea_mays.AGPv4.39.gtf','{0}_sort.bam'.format(a)])
#	cuff.wait()
#	os.rename('genes.fpkm_tracking','{0}_genes.fpkm_tracking'.format(data))
#	os.rename('isoforms.fpkm_tracking','{0}_isoforms.fpkm_tracking'.format(data))

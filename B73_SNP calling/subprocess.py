import subprocess
import sys

#example command: python example.py forward_file.fastq reverse_file.fastq output.sam output.bam output-sorted.bam


"""
dataset1,forward_file1.fq,forwardfile2.fq,output_file1.sam
dataset2

fh = open("dataset_spreadsheet")
for x in fh
	y = x.strip().split(',')
	mg1 = y[1]
	mg2 = y[2]
	sam_file = y[3]
"""
mg1 = sys.argv[1]
mg2 = sys.argv[2]
sam_file = sys.argv[3]
bam_file = sys.argv[4]
sort_file = sys.argv[5]
#mg1 = raw_input("Please enter the first merged file name\n")
#mg2 = raw_input("Please enter the second merged file name\n")
#f_mg = raw_input("Please enter the final merged file name\n")
#sam = raw_input("Please enter the name for sam file\n")
merge = subprocess.Popen(['java','-jar','/home/zliang/software/trimmomatic-0.33.jar','PE','-phred33','-threads','8',mg1,mg2,"temp.f.p.fq","temp.f.u.fq","temp.r.p.fq","temp.r.u.fq",'LEADING:3','TRAILING:3','SLIDINGWINDOW:4:15','MINLEN:36'])
merge.wait()
sam_out = open(sam_file,'w')
gsnap = subprocess.Popen(['gsnap','-D','./','-d','Zea_mays.AGPv3.22.rm','--nthreads=6','-B','3','-N','1','-n','2','-Q','--nofails','--format=sam','temp.f.p.fq','temp.r.p.fq'], stdout=sam_out)
gsnap.wait()
sam_out.close()
bam_out = open(bam_file,'w')
samt = subprocess.Popen(['samtools','view','-bS',sam_file],stdout=bam_out)
samt.wait()
bam_out.close()
samt_s = subprocess.Popen(['samtools','sort',bam_file,sort_file])
samt_s.wait()
print samt_s

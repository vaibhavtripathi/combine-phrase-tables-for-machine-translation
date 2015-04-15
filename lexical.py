import codecs
from sets import Set

src = codecs.open('src-phrase-table', encoding='utf-8')
pt = open('final-merged-phrase-table', 'w')

def pdict(dic):
  for key,val in dic.iteritems():
    print key.encode('utf-8'), dic[key]

counts_f={}
counts_e={}
paired_counts={}

for line in src:
  vec = line.split('|||')
  alignments = vec[3]
  processed_f = []
  processed_e = []
  for a in alignments.split():
    if vec[0].split()[int(a[0])]+vec[1].split()[int(a[2])] not in paired_counts:
      paired_counts[vec[0].split()[int(a[0])]+vec[1].split()[int(a[2])]] = 1
    else:
      paired_counts[vec[0].split()[int(a[0])]+vec[1].split()[int(a[2])]] = paired_counts[vec[0].split()[int(a[0])]+vec[1].split()[int(a[2])]] + 1
    if vec[0].split()[int(a[0])] not in processed_f:
      processed_f.append(vec[0].split()[int(a[0])])
    if vec[1].split()[int(a[2])].strip() not in processed_e:
      processed_e.append(vec[1].split()[int(a[2])].strip())

  for p in processed_f:
    if p in counts_f:
      counts_f[p] = counts_f[p]+1
    else:
      counts_f[p] = 1
    
  for p in processed_e:
    if p in counts_e:
      counts_e[p] = counts_e[p]+1
    else:
      counts_e[p] = 1   

src.close()
src = codecs.open('merged-phrase-table', encoding='utf-8')
   
for line in src:
  revlex={}
  fwdlex={}
  rev = []
  fwd = []
  revlexprob = 1
  fwdlexprob = 1
  vec = line.split('|||')
  prob = vec[2].split()
  alignments = vec[3]
  for a in alignments.split():
    if a[0] not in revlex:		
      list = []
      list.append(paired_counts[vec[0].split()[int(a[0])]+vec[1].split()[int(a[2])]]/float(counts_e[vec[1].split()[int(a[2])].strip()]))
      revlex[a[0]] = list
    else:
      list = revlex[a[0]] 
      list.append(paired_counts[vec[0].split()[int(a[0])]+vec[1].split()[int(a[2])]]/float(counts_e[vec[1].split()[int(a[2])]]))
      revlex[a[0]] = list
    if a[2] not in fwdlex:		
      list = []
      list.append(paired_counts[vec[0].split()[int(a[0])]+vec[1].split()[int(a[2])]]/float(counts_f[vec[0].split()[int(a[0])].strip()]))
      fwdlex[a[2]] = list
    else:
      list = fwdlex[a[2]] 
      list.append(paired_counts[vec[0].split()[int(a[0])]+vec[1].split()[int(a[2])]]/float(counts_f[vec[0].split()[int(a[0])]]))
      fwdlex[a[2]] = list
  for i in revlex:
    rev.append(sum(revlex[i])/float(len(revlex[i])))
  for i in fwdlex:
    fwd.append(sum(fwdlex[i])/float(len(fwdlex[i])))
  for i in rev:
    revlexprob = revlexprob*i
  for i in fwd:
    fwdlexprob = fwdlexprob*i
  print revlexprob, fwdlexprob
  continue
  pt.write(vec[0].strip().encode('utf-8')+' ||| '+vec[1].strip().encode('utf-8')+' ||| ')
  pt.write(prob[0])
  pt.write(' ')
  pt.write(str(revlexprob))
  pt.write(' ')
  pt.write(prob[2])
  pt.write(' ')
  pt.write(str(fwdlexprob))
  pt.write(' ')
  pt.write(prob[4])
  pt.write(' ||| '+vec[3].strip()+' ||| '+vec[4].strip()+'\n')
  
    

      
    
      
    

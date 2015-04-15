import pickle
import codecs
import sys

src = codecs.open(sys.argv[1], encoding='utf-8')
destfilename = str(sys.argv[1])+'-thresh'
dest = open(destfilename, 'w')
thresh = float(sys.argv[2])

score = {}
phrase = {}

for line in src:
  vec = line.split('|||')
  if vec[0] not in score:
    probvec = vec[2]
    prob = probvec.split()[2]
    score[vec[0]] = prob
    phrase[vec[0]] = line
  else:
    probvec = vec[2]
    prob = probvec.split()[2]
    if score[vec[0]] < prob:
      score[vec[0]] = prob
      phrase[vec[0]] = line

src.close()
src = codecs.open(sys.argv[1], encoding='utf-8')

for line in src:
  vec = line.split('|||')
  probvec = vec[2]
  prob = probvec.split()[2]
  if float(prob) > thresh*float(score[vec[0]]):
    dest.write(line.encode('utf-8'))
  
    
    
    
    
    

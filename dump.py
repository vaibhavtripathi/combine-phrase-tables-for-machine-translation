import pickle
import codecs
import sys

src = codecs.open(sys.argv[1], encoding='utf-8')
destfile = str(sys.argv[1])+'.dump'

def pdict(dic):
  for key,val in dic.iteritems():
    print key.encode('utf-8')
    for i in val:
      print i.encode('utf-8')

phrases={}

for line in src:
  vec = line.split('|||')
  if vec[0] not in phrases:
    list=[]
    list.append(line)
    phrases[vec[0]]=list
  else:
    l=phrases[vec[0]]
    l.append(line)
    phrases[vec[0]]=l

pickle.dump(phrases, open(destfile, "wb"))

  


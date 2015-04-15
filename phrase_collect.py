import pickle
import codecs
src = codecs.open('src-phrase-table', encoding='utf-8')


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
    list.append(vec[1])
    phrases[vec[0]]=list
  else:
    l=phrases[vec[0]]
    l.append(vec[1])
    phrases[vec[0]]=l

pickle.dump(phrases, open("save.p", "wb"))

  


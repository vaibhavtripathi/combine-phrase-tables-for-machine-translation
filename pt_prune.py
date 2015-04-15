import pickle
import codecs
import nltk

src = codecs.open('hi-en', encoding='utf-8')
src2 = codecs.open('en-bn', encoding='utf-8')
test = codecs.open('test.hi', encoding='utf-8')
p = open('hi-en-pruned', 'w')
p2 = open('en-bn-pruned', 'w')
temp = open('temp', 'w')
escape = codecs.open('escapewords', encoding='utf-8')

escapelist=[i[:-1] for i in escape]

wordlist={}

def get_word_features(wordlist):
  wordlist = nltk.FreqDist(wordlist)
  wordlist_keys = wordlist.keys()
  word_features = [w for w in wordlist_keys if wordlist[w]>5]
  return word_features

def pdict(dic):
  for key,val in dic.iteritems():
    print key.encode('utf-8')
    for i in val:
      print i.encode('utf-8')

ext_phrases = [] 
words = [] 
eng_words = set()

for line in test:
  vec = line.split()
  words.extend(vec)

imp_words = get_word_features(words)[33:]

for i in imp_words:
  temp.write(i.encode('utf-8'))
  temp.write('\n')

print len(imp_words)

print escapelist

for line in src:
  flag=0
  vec = line.split('|||')
  for i in vec[0].split():
    if i in imp_words:
      if i not in escapelist:
        flag=1
        break
  if flag==1:
    p.write(line.encode('utf-8'))
    eng_words.update(vec[1].split())



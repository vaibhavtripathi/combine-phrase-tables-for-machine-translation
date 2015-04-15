import codecs
import pickle

src = codecs.open('src-phrase-table', encoding='utf-8')

pt = open('hi-en-bn-merged-phrase-table', 'w')
p = open('newphrases', 'w')

alpha = 0.9
phrase_penalty = 2.718

p1 = pickle.load(open("hi-en-pruned.dump", "rb"))
p2 = pickle.load(open("en-bn-pruned.dump", "rb"))
phrases = pickle.load(open("save.p", "rb"))

def product(t1, t2):
  minlen = 0
  result_tup=[]
  if len(t1) < len(t2):
    minlen = len(t1)
  else:
    minlen = len(t2) 
  for i in range(minlen):
    result_tup.append(t1[i]*t2[i])
  return tuple(result_tup)

def tupsum(t1, t2):
  result_tup=[]
  minlen = 4 
  for i in range(minlen):
    result_tup.append(t1[i]*(1-alpha) + t2[i]*alpha)
  result_tup.append(float(phrase_penalty))
  return tuple(result_tup)

def addtup(t1, t2):
  result_tup=[]
  minlen = 4 
  for i in range(minlen):
    result_tup.append(t1[i] + t2[i])
  result_tup.append(float(phrase_penalty))
  return tuple(result_tup)

def combine_align(a1, a2):
  a=a1.split()
  b=a2.split()
  c=[]
  for i in a:  
    for j in b:	
      if i[2]==j[0]:
        c.append(i[0]+'-'+j[2])
  return c
    
# Load the pivot table values.

'''p1_prob={}
align={}

for key in p1:
  for i in p1[key]:
    vec = i.split('|||')
    strprobval = vec[2]
    probval = [float(x) for x in strprobval.split()]
    templist = [vec[0], vec[1]]
    p1_prob[tuple(templist)] = tuple(probval)

p2_prob={}

for key in p2:
  for i in p2[key]:
    vec = i.split('|||')
    strprobval = vec[2]
    probval = [float(x) for x in strprobval.split()]
    templist = [vec[0], vec[1]]
    p2_prob[tuple(templist)] = tuple(probval)
    align[tuple(templist)] = vec[3]'''

num_new_phrases=0

for line in src:
  matched_piv_phrases={}
  phrases_to_update={}
  alignment={}
  vec = line.split('|||')
  strprobval = vec[2]
  probval = [float(x) for x in strprobval.split()]

# f is phrase from source language	

  f = vec[0]

# e is phrase from target language

  e = vec[1]

# search for f in PT 1

  if f in p1:
    print f
    for i in p1[f]:
      vector = i.split('|||')
      print vector[2]
      if vector[2] in p2:
        for j in p2[vector[2]]:
          print vector[0], j.split('|||')[1]

  
  '''for key1 in matched_piv_phrases:
    for key2 in p2_prob:
      if key1.strip() == key2[0].strip():
        if key2[1] in phrases_to_update:
          phrases_to_update[key2[1]] = addtup(phrases_to_update[key2[1]], product(matched_piv_phrases[key1], p2_prob[key2]))
          alignment[key2[1]] = align[key2]
        else:
          phrases_to_update[key2[1]] = product(matched_piv_phrases[key1], p2_prob[key2])
          alignment[key2[1]] = align[key2]

  orig_phrase_written=0

  if len(phrases_to_update) > 0:
    for key in phrases_to_update:
      if key.strip() == vec[1].strip():
        orig_phrase_written=1
        pt.write(vec[0].strip().encode('utf-8')+' ||| '+key.strip().encode('utf-8')+' ||| '+' '.join(map(str, tupsum(phrases_to_update[key], tuple(probval)))))
        pt.write(' ||| ')
        pt.write(vec[3])
        pt.write(' ||| ')
        pt.write(vec[4])
      else: 
        if key not in phrases[vec[0]]:
          num_new_phrases=num_new_phrases+1
          print num_new_phrases
          pt.write(vec[0].strip().encode('utf-8')+' ||| '+key.strip().encode('utf-8')+' ||| '+' '.join(map(str, tupsum(phrases_to_update[key], tuple([0, 0, 0, 0, 0])))))
          pt.write(' ||| ')
          pt.write(' '.join(map(str, combine_align(vec[3],alignment[key]))))
          pt.write(' ||| ')
          pt.write(vec[4])

          p.write(vec[0].strip().encode('utf-8')+' ||| '+key.strip().encode('utf-8')+' ||| '+' '.join(map(str, tupsum(phrases_to_update[key], tuple([0, 0, 0, 0, 0])))))
          p.write(' ||| ')
          p.write(' '.join(map(str, combine_align(vec[3],alignment[key]))))
          p.write(' ||| ')
          p.write(vec[4])

          l=phrases[vec[0]]
          l.append(key)
          phrases[vec[0]]=l  

  if orig_phrase_written == 0:
    pt.write(line.encode('utf-8'))'''
  
  
     
  

from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000/')
from gensim.utils import lemmatize
s = 'Didn\'t know how to cross the road'
print lemmatize(s)
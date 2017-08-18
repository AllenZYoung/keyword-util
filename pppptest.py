from stanfordcorenlp import StanfordCoreNLP
from gensim.utils import lemmatize

# s1 = 'In her first Reaping , 12-year-old Primrose Everdeen is chosen from District 12 .'
# s2 = 'Since Woody is broke as usual , he sneaks in and gets thrown out by Buzz . '
# s3 = 'is'
# nlp = StanfordCoreNLP('http://localhost:9000/')
# # print(nlp.pos_tag(s1))
# # print(nlp.pos_tag(s2))
#
# # from nltk.stem.wordnet import WordNetLemmatizer
# # lemmatizer = WordNetLemmatizer()
# # a = lemmatizer.lemmatize('is', 'v')
# b = lemmatize(s1)
#
# print(b)
# b = lemmatize(s2)
# print b
# b = lemmatize(s3)
# s = str(b[0])
# print s[:s.find('/')]
#
# s = 'a'
# s = 'b' + s
# print s
# print s.find('EXCEPTION')
import operator
x = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
sorted_dict = sorted(x.items(), key=operator.itemgetter(1))
# sorted_dict.reverse()
list_raw = sorted_dict[0]
print list_raw


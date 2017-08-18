from gensim.models import word2vec
import logging
from gensim.models.keyedvectors import KeyedVectors


word_vectors = KeyedVectors.load_word2vec_format('/Users/zhangyang/PycharmProjects/GoogleNews-vectors-negative300.bin.gz', binary=True)
print("Load done!")

score = word_vectors.similarity('woman', 'man')
print score
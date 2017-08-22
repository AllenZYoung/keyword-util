import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
import os

class MySentences(object):
  def __init__(self, dirname):
    self.dirname = dirname

  def __iter__(self):
    for fname in os.listdir(self.dirname):
      for line in open(os.path.join(self.dirname, fname)):
        yield line.split()


# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# filename = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/book_summaries_filter.txt'
# model = Word2Vec(LineSentence(filename), size=300, window=5, min_count=5, workers=4)
# # print model['marry']
# model.save('model-16')
# model1 = Word2Vec.load('model-16')
# print model1.similarity('japan','live')

model = Word2Vec.load('model-17')
print model.similarity('otaku','Manchester')
from gensim.models import Word2Vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.models.word2vec import LineSentence,PathLineSentences

filename = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/book_summaries_filter.txt'

filename2 = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/movie_summaries_filter.txt'
filename3 = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/stories-100word_filter.txt'
filename4 = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/wikiPlots_filter.txt'

ls_final = PathLineSentences('/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/')

model = Word2Vec(ls_final, size=300, window=5, min_count=0, workers=4)

# model.train(LineSentence(filename2), total_examples=174723, epochs=model.iter)
print model.similarity('boy', 'man')
print model.similarity('Dupond','Otaku')
# model2 = Word2Vec.load('model-16-2')
# filename3 = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/stories-100word_filter.txt'
# model.train(LineSentence(filename3), total_examples=174723, epochs=model.iter)
# print model.similarity('boy', 'man')

# print model2.similarity('boy','man')
# model1.save('model-16-3')
#
# model.train(LineSentence(filename4), total_examples=174723, epochs=model.iter)
# print model.similarity('boy', 'man')

# model1 = Word2Vec.load('model-16')
# model2 = Word2Vec.load('model-16-2')
# model3 = Word2Vec.load('model-16-3')
# print model1.similarity('boy','boy')
# print model2.similarity('boy','man')
# print model3.similarity('London','Philadelphia')
#
model.save('model-17-c')
#

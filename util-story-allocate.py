import logging
from stanfordcorenlp import StanfordCoreNLP
import nltk
from pprint import pprint
from gensim.utils import lemmatize
import nltk.data
import nltk.tokenize
import os

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


def sentence_split(str_centence):
  list_ret = list()
  for s_str in str_centence.split('.'):
    if '?' in s_str:
      list_ret.extend(s_str.split('?'))
    elif '!' in s_str:
      list_ret.extend(s_str.split('!'))
    else:
      list_ret.append(s_str)
  return list_ret


def sentence_spliter(str_sentence):
  sentences = tokenizer.tokenize(str_sentence)
  return sentences


raw_file = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/wikiPlots_filter.txt',
]
for rawfile in raw_file:
  with open(rawfile, 'r') as rf:
    output_path = rawfile[rawfile.find('-001') + 5:]
    allo_path1 = 'newdir/ALLOCATE-source-1-V2' + output_path
    allo_path2 = 'newdir/ALLOCATE-source-2-V2' + output_path
    f1 = open(os.path.join(os.getcwd(), allo_path1), 'a')
    f2 = open(os.path.join(os.getcwd(), allo_path2), 'a')
    print allo_path1
    # print allo_path2
    for case in rf:  # EVERY LINE
      sentences = []

      try:
        senten_splits = sentence_spliter(case)
      except (UnicodeDecodeError,UnicodeEncodeError):
        excep_Unicode = True
        # f1.write('UNICODE ERROR\t')
        # f2.write('UNICODE ERROR\t')
        continue

      if len(senten_splits) < 5:
        f1.write('SHORTER THAN 5 SENTENCES\t')
        f2.write('SHORTER THAN 5 SENTENCES\t')
        continue

      for str_sentence in senten_splits:
        sentences.append(str_sentence)

      pprint(sentences)

      s1 = str(sentences[0]).replace('\n', '')
      s2 = str(sentences[1]).replace('\n', '')
      s3 = str(sentences[2]).replace('\n', '')
      s4 = str(sentences[3]).replace('\n', '')
      s5 = str(sentences[4]).replace('\n', '')

      str1 = s1 + ' ' + s2
      str2 = str1 + ' ' + s3
      str3 = str2 + ' ' + s4
      f1.write(str1 + '\n')
      f1.write(str2 + '\n')
      f1.write(str3 + '\n')

      f2.write(s3 + '\n')
      f2.write(s4 + '\n')
      f2.write(s5 + '\n')

    f1.close()
    f2.close()

  print 'Got one source file done!'

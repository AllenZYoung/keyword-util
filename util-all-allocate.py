import logging
from stanfordcorenlp import StanfordCoreNLP
import nltk
from pprint import pprint
from gensim.utils import lemmatize
import nltk.data
import nltk.tokenize
import os

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


# str = 'cat dog me\n'
# print str.split(' ')


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


raw_file_KW = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/KEYWORD-ULTRA-ranked-V-ULTRA-LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/KEYWORD-ULTRA-ranked-V-ULTRA-LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/KEYWORD-ULTRA-ranked-V-ULTRA-LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/KEYWORD-ULTRA-ranked-V-ULTRA-LOWERSOURCE-wikiPlots_filter.txt',
]

raw_file_SOURCE = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-wikiPlots_filter.txt',
]


def Line_num_checker(path1, path2):
  ctr1 = 0
  ctr2 = 0
  with open(path1, 'r') as f1:
    for line1 in f1:
      ctr1 += 1

  with open(path2, 'r') as f2:
    for line2 in f2:
      ctr2 += 1

  if ctr1 == ctr2:
    print ctr1, ctr2
    return True
  else:
    return False


line_ctr1_list1 = []

line_ctr1_list = [[], [], [], []]

# 1
for i in range(0, len(raw_file_KW)):
  rawfile_KW = raw_file_KW[i]
  rawfile_SOURCE = raw_file_SOURCE[i]

  if Line_num_checker(rawfile_KW, rawfile_SOURCE):

    with open(rawfile_KW, 'r') as rf:
      line_ctr1 = 0

      output_path = rawfile_KW[rawfile_KW.find('ranked'):]
      allo_path1 = 'newdir/ALLOCATE-ULTRA-KEYWORD-' + output_path
      f1 = open(os.path.join(os.getcwd(), allo_path1), 'a')
      print allo_path1

      for line in rf:  # EVERY LINE
        write_str = ''

        line_ctr1 += 1

        if line.find('EXCEPTION') != -1:
          print 'GOT EXCEPTION'
          line_ctr1_list[i].append(line_ctr1)
          continue
          # f1.write('<' + line)
          # f1.write('\n')
          # f1.write('EXCEPTION case end>\n')
        else:
          words = line.split(' ')
          # print words
          if len(words) < 3:
            print '---NOT 3 WORDS, ERROR!---'
            break
            # break
          w3 = words[0].replace('\n', '')
          w4 = words[1].replace('\n', '')
          w5 = words[2].replace('\n', '')

          f1.write(w3 + '\n')
          f1.write(w4 + '\n')
          f1.write(w5 + '\n')

      f1.close()

    print 'Got one source file done!'

  else:
    print "ERROR!"
    break

# 2
for i in range(0, len(raw_file_SOURCE)):
  rawfile_source = raw_file_SOURCE[i]
  with open(rawfile_source, 'r') as rf:
    ctr2 = 0
    output_path = rawfile_source[rawfile_source.find('wdir/') + 5:]
    allo_path1 = 'newdir/ALLOCATE-ULTRA-SOURCE-1-V3' + output_path
    allo_path2 = 'newdir/ALLOCATE-ULTRA-SOURCE-2-V3' + output_path
    f1 = open(os.path.join(os.getcwd(), allo_path1), 'a')
    f2 = open(os.path.join(os.getcwd(), allo_path2), 'a')
    # print allo_path1
    # print allo_path2
    for case in rf:  # EVERY LINE
      ctr2 += 1
      sentences = []

      if ctr2 in line_ctr1_list[i]:
        print 'KEYWORD FILE GAVE AN EXCEPTION'
        continue

      try:
        senten_splits = sentence_spliter(case)
      except (UnicodeDecodeError, UnicodeEncodeError):
        excep_Unicode = True
        f1.write('UNICODE ERROR\n')
        f2.write('UNICODE ERROR\n')
        continue

      if len(senten_splits) < 5:
        f1.write('SHORTER THAN 5 SENTENCES\t\n')
        f2.write('SHORTER THAN 5 SENTENCES\t\n')
        print 'SHORTER THAN 5 SENTENCES'
        break

      for str_sentence in senten_splits:
        sentences.append(str_sentence)

      # pprint(sentences)

      s1 = sentences[0].replace('\n', '')
      s2 = sentences[1].replace('\n', '')
      s3 = sentences[2].replace('\n', '')
      s4 = sentences[3].replace('\n', '')
      s5 = sentences[4].replace('\n', '')

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

# 3
for i in range(0, len(raw_file_SOURCE)):
  rawfile_source = raw_file_SOURCE[i]
  with open(rawfile_source, 'r') as rf:
    ctr3 = 0
    output_path = rawfile_source[rawfile_source.find('wdir/') + 5:]
    allo_path = 'newdir/ALLOCATE-ULTRA-SOURCE-ALL-V3' + output_path
    f = open(os.path.join(os.getcwd(), allo_path), 'a')
    # print allo_path1
    # print allo_path2
    for case in rf:  # EVERY LINE
      ctr3 += 1
      sentences = []

      if ctr3 in line_ctr1_list[i]:
        print 'KEYWORD FILE GAVE AN EXCEPTION'
        continue

      try:
        senten_splits = sentence_spliter(case)
      except (UnicodeDecodeError, UnicodeEncodeError):
        excep_Unicode = True
        print ' Unicode ERROR!'
        f1.write('UNICODE ERROR\n')
        f2.write('UNICODE ERROR\n')
        continue

      if len(senten_splits) < 5:
        f1.write('SHORTER THAN 5 SENTENCES\t\n')
        f2.write('SHORTER THAN 5 SENTENCES\t\n')
        print 'SHORTER THAN 5 SENTENCES'
        break

      for str_sentence in senten_splits:
        sentences.append(str_sentence)

      # pprint(sentences)

      s1 = sentences[0].replace('\n', '')
      s2 = sentences[1].replace('\n', '')
      s3 = sentences[2].replace('\n', '')
      s4 = sentences[3].replace('\n', '')
      s5 = sentences[4].replace('\n', '')

      str1 = s1 + ' ' + s2 + ' ' + s3 + ' ' + s4 + ' ' + s5

      f.write(str1 + '\n')

    f.close()

  print 'Got one source file done!'

import logging
from stanfordcorenlp import StanfordCoreNLP
import nltk
from pprint import pprint
from gensim.utils import lemmatize
import nltk.data
import nltk.tokenize

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
  tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = tokenizer.tokenize(str_sentence)
  return sentences


nlp = StanfordCoreNLP('http://localhost:9000/')
# print(nlp.pos_tag("I am a boy"))

ctr1 = 0
sum_all = 0
list_nosense = ['be', 'should', 'will', 'do', 'could', 'would', 'may', 'have', 'want', 'get', 'make']
with open(
        '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/wikiPlots_filter.txt',
        'r') as text:
  with open('n&v-X-movie.txt', 'a') as wf:
    for case in text:
      excep = False
      sentences = []
      write_str = ''

      for str_sentence in sentence_split(case):
        sentences.append(str_sentence)
        # print(content)
      ctr1 += len(sentences) - 1

      for one in sentences[:len(sentences) - 1]:
        res = nlp.pos_tag(one)
        list_verb = []
        list_noun = []
        for one in res:

          if str(one[1])[0] == 'N' and str(one[1]) != 'NNP' and str(one[1]) != 'NNPS':
            list_noun.append(one[0])

          if str(one[1])[0] == 'V':
            list_verb.append(one[0])

        # sum_all += len(list_noun)
        for one in list_noun:
          res = lemmatize(one)
          if len(res) <= 0:
            continue
          else:
            s = str(res[0])
            word = s[:s.find('/')]
            try:
              write_str += word
            except UnicodeDecodeError:
              continue

            write_str += ' '
        print len(list_noun)
        if len(list_noun) == 0:
          verb_ctr = 0
          for one in list_verb:
            res = lemmatize(one)
            if len(res) <= 0:
              pass
            else:
              s = str(res[0])
              word_base = s[:s.find('/')]
              if word_base in list_nosense:
                continue
            try:
              write_str += one
            except UnicodeDecodeError:
              continue

            write_str += ' '
            verb_ctr += 1

          if verb_ctr == 0 and len(list_noun) == 0:
            excep = True
            break
        # print("Nouns:\n", list_noun)
        # print("Verbs:\n", list_verb)
        write_str += '\t'

        del list_verb
        del list_noun
      write_str += '\n'
      if excep:
        write_str = 'EXCEPTION\t' + write_str
      print(write_str)
      wf.write(write_str)
      del sentences

      # print(sum_all/ctr1)

import logging
from stanfordcorenlp import StanfordCoreNLP
import nltk
from pprint import pprint
from gensim.utils import lemmatize
import nltk.data
import nltk.tokenize
from random import randint

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


nlp = StanfordCoreNLP('http://localhost:9000/')
# print(nlp.pos_tag("I am a boy"))

raw_source_list = [
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-book_summaries_filter.txt',
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-movie_summaries_filter.txt',
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-wikiPlots_filter.txt',
]

ctr1 = 0
sum_all = 0
list_nosense = ['be', 'should', 'will', 'do', 'could', 'would', 'may', 'have', 'want', 'get', 'make']
for raw_source in raw_source_list:
  with open(
          raw_source,
          'r') as text:
    output_name = raw_source[raw_source.find('dir') + 4:]
    dir_path = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/'
    output_path = dir_path + 'NV-ULTRA-' + output_name
    with open(output_path, 'a') as wf:
      for case in text:

        excep_NounVerb = False
        excep_Unicode = False

        sentences = []
        write_str = ''

        try:
          senten_splits = sentence_spliter(case)
        except UnicodeDecodeError:
          excep_Unicode = True
          wf.write('EXCEPTION: UNICODE ERROR\n')
          continue

        for str_sentence in senten_splits:
          sentences.append(str_sentence)
          # print(content)
        # print len(senten_splits)

        # TODO one sentence began
        for one_sen in sentences:
          res = nlp.pos_tag(one_sen)
          list_verb = []
          list_noun = []
          list_others = []

          for one in res:

            if str(one[1])[0] == 'N' and str(one[1]) != 'NNP' and str(one[1]) != 'NNPS':
              list_noun.append(one[0])

            elif str(one[1])[0] == 'V':
              list_verb.append(one[0])

            else:
              list_others.append(one[0])

          # sum_all += len(list_noun)
          for one_noun in list_noun:
            res = lemmatize(one_noun)
            if len(res) <= 0:
              continue
            else:
              s = str(res[0])
              word = s[:s.find('/')]
              try:
                write_str += word
              except UnicodeDecodeError:
                excep_Unicode = True
                continue

              write_str += ' '
          # print len(list_noun)
          write_str += ' <noun end> '
          verb_ctr = 0

          for one_verb in list_verb:
            res = lemmatize(one_verb)
            if len(res) <= 0:
              pass
            else:
              s = str(res[0])
              word_base = s[:s.find('/')]
              if word_base in list_nosense:
                continue
              try:
                write_str += word_base
              except UnicodeDecodeError:
                excep_Unicode = True
                continue
              write_str += ' '
              verb_ctr += 1

          list_others_filtered = [word for word in list_others if (word == 'i' or word == 'a' or len(word) > 1)]

          if verb_ctr == 0 and len(list_noun) == 0:  # TODO WE GOT NO V or V here!

            if len(str(one_sen).replace('\n', '')) > 2:

              if len(list_others_filtered) == 0:
                excep_NounVerb = True
                selected_word = ''
              else:
                selected_word = list_others_filtered[randint(0, len(list_others_filtered) - 1)]

              try:
                write_str += selected_word
              except UnicodeDecodeError:
                excep_Unicode = True

            else:
              excep_NounVerb = True
              print '<SHORT>The SHORT strange one:\t' + one_sen + '<end>'  # TODO WE CAN NOT HANDLE THIS CONDITION
              continue

          # print("Nouns:\n", list_noun)
          # print("Verbs:\n", list_verb)
          write_str += '\t'

          del list_verb
          del list_noun
        # TODO one sent ends

        write_str += '\n'

        if excep_NounVerb:
          write_str = 'EXCEPTION: NO NV\t' + write_str
        if excep_Unicode:
          write_str = 'EXCEPTION: UNICODE ERROR\t' + write_str

        # print(write_str)
        # print '----- '
        try:
          wf.write(write_str)
        except UnicodeDecodeError as uni_error:
          wf.write('EXCEPTION: UNICODE ERROR\n')
          print uni_error.message
        except UnicodeEncodeError as uni_error:
          wf.write('EXCEPTION: UNICODE ERROR\n')
          print uni_error.message

        del sentences

        # print(sum_all/ctr1)

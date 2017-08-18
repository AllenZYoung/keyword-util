import numpy
from gensim.models.keyedvectors import KeyedVectors
from pprint import pprint
import logging
import operator

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

word_vectors = KeyedVectors.load_word2vec_format(
  '/Users/zhangyang/PycharmProjects/GoogleNews-vectors-negative300.bin.gz', binary=True)

print("Load done!")


def Similarity(word1, word2):
  score = word_vectors.similarity(word1, word2)
  return score
  # return 1


read_path = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/n&v-X-movie.txt'
write_path = 'keyword-n&v-movie.txt'
with open(read_path, 'r') as rf:
  with open(write_path, 'a') as wf:
    for line in rf:
      NOT_IN_VOC = False
      print 'New case'
      dict_raw = dict()
      if str(line).find('EXCEPTION') != -1:
        EXCEP_str = 'EXCEPTION\n'
        wf.write(EXCEP_str)
        continue  # we got an EXCEPTION here
      else:
        sentences = line.split('\t')
        pprint(sentences)
        pprint(len(sentences))

        if len(sentences) < 6: # we got a '\n' here
          pprint("ERROR, too short!")
          TOOSHORT_str = 'TOO SHORT, LESS THAN 5 SENTENCES\n'
          wf.write(TOOSHORT_str)
          continue

        s3 = sentences[2]
        s4 = sentences[3]
        s5 = sentences[4]
        s3w = s3.split(' ')
        s4w = s4.split(' ')
        s5w = s5.split(' ')
        del s3w[-1]
        del s4w[-1]
        del s5w[-1]

        if len(s3w) == 0 or len(s4w) == 0 or s5w == 0:
          EXCEP_str = 'EXCEPTION\n'
          wf.write(EXCEP_str)
          continue  # we got an EXCEPTION here

        for word1 in s3w:
          for word2 in s4w:
            for word3 in s5w:
              try:
                sim1 = Similarity(word1, word2)
                sim2 = Similarity(word1, word3)
                sim3 = Similarity(word2, word3)
              except KeyError:
                NOT_IN_VOC = True
                sim1 = 0
                sim2 = 0
                sim3 = 0
                # diminish its similarity

              sim_sum = sim1 + sim2 + sim3
              t3 = tuple()
              t3 = (word1, word2, word3,)
              dict_raw[t3] = sim_sum

        sorted_dict = sorted(dict_raw.items(), key=operator.itemgetter(1))
        sorted_dict.reverse()
        print 'SORTED DICT:'
        pprint(sorted_dict)
        print '-------'
        if len(sorted_dict) > 3:
          top3_list_raw = sorted_dict[:3]
        else:
          top3_list_raw = sorted_dict
        # print top3_list_raw
        dict_w_v = dict()
        for one in top3_list_raw:
          tup0 = one[0]  # words
          tup1 = one[1]  # values
          word_list = []
          for word in tup0:
            word_list.append(word)
          if not NOT_IN_VOC:
            sim1 = Similarity(word_list[0], word_list[1])
            sim2 = Similarity(word_list[1], word_list[2])
            sim3 = Similarity(word_list[0], word_list[2])
          else:
            sim2 = 1
            sim1 = 0
            sim3 = 2
            # since here we havn't take care of sum of sim, but we now pay
            # attention to var
          var_list = []
          var_list.append(sim1)
          var_list.append(sim2)
          var_list.append(sim3)
          print tup0, tup1
          var = numpy.var(var_list)
          print var
          dict_w_v[tup0] = var

        pprint(dict_w_v)
        print '-------'
        sorted_dict_wv = sorted(dict_w_v.items(), key=operator.itemgetter(1))
        pprint(sorted_dict_wv)

        if len(sorted_dict_wv) == 0:
          EXCEP_str = 'EXCEPTION\n'
          wf.write(EXCEP_str)
          continue  # we got an EXCEPTION here

        ans_raw = sorted_dict_wv.pop(0)
        print ans_raw
        print '-------'
        NORMAL_str = ''
        if NOT_IN_VOC:
          NORMAL_str += 'GOT WORD NOT IN VOC\t'
        for word in ans_raw[0]:
          NORMAL_str += word
          NORMAL_str += ' '

        NORMAL_str += '\n'
        wf.write(NORMAL_str)

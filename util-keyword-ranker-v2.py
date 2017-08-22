import numpy
from gensim.models.keyedvectors import KeyedVectors
from gensim.models import Word2Vec
from pprint import pprint
import logging
import operator

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

word_vectors = KeyedVectors.load_word2vec_format(
  '/Users/zhangyang/PycharmProjects/GoogleNews-vectors-negative300.bin.gz', binary=True)

# word_vectors = Word2Vec.load(
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/model-17-c')

print("Load done!")


def Similarity(word1, word2):
  score = word_vectors.similarity(word1, word2)
  return score
  # return 1


read_list = [
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/NV-ULTRA-LOWERSOURCE-book_summaries_filter.txt',
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/NV-ULTRA-LOWERSOURCE-movie_summaries_filter.txt',
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/NV-ULTRA-LOWERSOURCE-stories-100word_filter.txt'
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/NV-ULTRA-LOWERSOURCE-wikiPlots_filter.txt',

]
for read_path in read_list:
  output_name = read_path[read_path.find('V-'):]
  out_dir = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/'
  write_path = out_dir + 'KEYWORD-ULTRA-ranked-' + output_name

  with open(read_path, 'r') as rf:
    with open(write_path, 'a') as wf:
      for line in rf:
        NOT_IN_VOC = False
        # print 'New case'
        TARGET_WORDS = ''
        dict_raw = dict()
        sim_dict = dict()

        if str(line).find('EXCEPTION') != -1:
          EXCEP_str = 'EXCEPTION:from NV file\n'
          wf.write(EXCEP_str)
          continue  # we got an EXCEPTION here

        else:
          sentences = line.split('\t')
          # pprint(sentences)
          # pprint(len(sentences))

          if len(sentences) < 6:  # we got a '\n' here
            # pprint("ERROR, too short!")
            TOOSHORT_str = 'EXCEPTION: TOO SHORT, LESS THAN 5 SENTENCES\n'
            wf.write(TOOSHORT_str)
            continue

          s3 = sentences[2]
          s4 = sentences[3]
          s5 = sentences[4]
          s3w = []
          s4w = []
          s5w = []

          for one in s3.split(' <noun end> '):
            s3w_n = one.split(' ')
            del s3w_n[-1]
            s3w += s3w_n
          for one in s4.split(' <noun end> '):
            s4w_n = one.split(' ')
            s4w += s4w_n
            del s4w_n[-1]
          for one in s5.split(' <noun end> '):
            s5w_n = one.split(' ')
            del s5w_n[-1]
            s5w += s5w_n

          if len(s3w) == 0 or len(s4w) == 0 or len(s5w) == 0:
            EXCEP_str = 'EXCEPTION: NO WORD FOUND\n'
            wf.write(EXCEP_str)
            continue  # we got an EXCEPTION here

          target_word_set = set()

          for word1 in s3w:
            if word1 not in word_vectors.vocab:
              continue
            for word2 in s4w:
              if word2 not in word_vectors.vocab:
                continue
              if word1 == word2:
                continue
              for word3 in s5w:
                if word3 not in word_vectors.vocab:
                  continue
                if word1 == word3 or word2 == word3:
                  continue
                try:
                  sim1 = Similarity(word1, word2)
                  sim2 = Similarity(word1, word3)
                  sim3 = Similarity(word2, word3)
                  str1 = str(word1 + '--' + word2)
                  str2 = str(word1 + '--' + word3)
                  str3 = str(word2 + '--' + word3)
                  sim_dict[str1] = sim1
                  sim_dict[str2] = sim2
                  sim_dict[str3] = sim3
                except KeyError as e:
                  NOT_IN_VOC = True
                  target_word = e.message[6:e.message.find('not in') - 2]
                  target_word_set.add(target_word)
                  # print target_word
                  # target_word = KeyError.message
                  sim1 = 0
                  sim2 = 0
                  sim3 = 0
                  # diminish its similarity

                sim_sum = sim1 + sim2 + sim3
                t3 = tuple()
                t3 = (word1, word2, word3,)
                dict_raw[t3] = sim_sum

          if len(dict_raw) == 0:
            # WE HAVE NO WORD here!
            pass

          for one in target_word_set:
            TARGET_WORDS += one
            TARGET_WORDS += ', '

          sorted_dict = sorted(dict_raw.items(), key=operator.itemgetter(1))
          sorted_dict.reverse()

          # print 'SORTED DICT:'
          # pprint(sorted_dict)
          # print '-------'

          if len(sorted_dict) > 3:
            top3_list_raw = sorted_dict[:3]
          else:
            top3_list_raw = sorted_dict

          # print top3_list_raw
          dict_w_v = dict()
          for one in top3_list_raw:
            tup0 = one[0]  # words
            tup1 = one[1]  # sim sum
            word_list = []

            for word in tup0:
              word_list.append(word)

            if not NOT_IN_VOC:
              # sim1 = Similarity(word_list[0], word_list[1])
              # sim2 = Similarity(word_list[1], word_list[2])
              # sim3 = Similarity(word_list[0], word_list[2])
              str1 = str(word_list[0] + '--' + word_list[1])
              str2 = str(word_list[0] + '--' + word_list[2])
              str3 = str(word_list[1] + '--' + word_list[2])
              sim1 = sim_dict.get(str1)
              sim2 = sim_dict.get(str2)
              sim3 = sim_dict.get(str3)
            else:
              # TODO literally, we cannot reach this code!
              sim2 = 1
              sim1 = 0
              sim3 = 2
              # since here we havn't take care of sum of sim, but we now pay
              # attention to var

            var_list = []
            var_list.append(sim1)
            var_list.append(sim2)
            var_list.append(sim3)

            # print tup0, tup1
            var = numpy.var(var_list)
            # print var
            dict_w_v[tup0] = var

          del sim_dict

          # pprint(dict_w_v)
          # print '-------'

          sorted_dict_wv = sorted(dict_w_v.items(), key=operator.itemgetter(1))
          # pprint(sorted_dict_wv)

          if len(sorted_dict_wv) == 0:
            EXCEP_str = 'EXCEPTION :NO VAR\n'
            wf.write(EXCEP_str)
            continue  # we got an EXCEPTION here

          ans_raw = sorted_dict_wv.pop(0)
          print ans_raw
          print '-------'
          NORMAL_str = ''

          if NOT_IN_VOC:
            NORMAL_str += 'EXCEPTION: GOT WORD NOT IN VOC:\t'
            NORMAL_str += TARGET_WORDS
            NORMAL_str += '<end>\t'

          for word in ans_raw[0]:
            NORMAL_str += word
            NORMAL_str += ' '

          NORMAL_str += '\n'
          wf.write(NORMAL_str)

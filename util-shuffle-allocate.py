list1 = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-wikiPlots_filter.txt',

]

list2 = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-wikiPlots_filter.txt',
]

list_kwpath = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-wikiPlots_filter.txt',
]

from allocate_new import Linenum_counter
from random import shuffle

output1_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-1-SHUFFLE.txt'
output1_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-1-UNSHUFFLE.txt'
output3_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-2-SHUFFLE.txt'
output3_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-2-UNSHUFFLE.txt'
output_kw_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/KW-SHUFFLE.txt'
output_kw_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/KW-UNSHUFFLE.txt'

list_s1 = []
list_kw = []
list_s2 = []
SHUFFLE = True

for i in range(0, 4):
  if Linenum_counter(list1[i]) == Linenum_counter(list2[i]) == Linenum_counter(list_kwpath[i]):
    path1 = list1[i]
    path2 = list2[i]
    path_kw = list_kwpath[i]
    if not (Linenum_counter(path1) % 3 == 0 and Linenum_counter(path2) and Linenum_counter(path_kw) % 3 == 0):
      print 'ERROR'
      break

    case_kw = ''
    case_source1 = ''
    case_source2 = ''

    ctr_line = 0
    f1_r = open(path1, 'r')
    for line in f1_r:
      ctr_line += 1
      case_source1 += line
      if ctr_line % 3 == 0:
        list_s1.append(case_source1)
        case_source1 = ''
    f1_r.close()

    ctr_line = 0
    f2_r = open(path2, 'r')
    for line in f2_r:
      ctr_line += 1
      case_source2 += line
      if ctr_line % 3 == 0:
        list_s2.append(case_source2)
        case_source2 = ''
    f2_r.close()

    f3_r = open(path_kw, 'r')
    for line in f3_r:
      ctr_line += 1
      case_kw += line
      if ctr_line % 3 == 0:
        list_kw.append(case_kw)
        case_kw = ''
    f3_r.close()

  else:
    print 'ERROR!'
    break

list_whole = zip(list_s1, list_s2, list_kw)
print 'all list len:{}, and cases is {}'.format(len(list_whole),len(list_whole)/3)
if SHUFFLE:
  shuffle(list_whole)

if SHUFFLE:
  f1o = open(output1_shuffle, 'a')
  f2o = open(output3_shuffle, 'a')
  fkwo = open(output_kw_shuffle, 'a')
  for one in list_whole:
    f1o.write(one[0])
    f2o.write(one[1])
    fkwo.write(one[2])
  f1o.close()
  f2o.close()
  fkwo.close()

else:
  f1o = open(output1_unshuffle, 'a')
  f2o = open(output3_unshuffle, 'a')
  fkwo = open(output_kw_unshuffle, 'a')
  for one in list_whole:
    f1o.write(one[0])
    f2o.write(one[1])
    fkwo.write(one[2])
  f1o.close()
  f2o.close()
  fkwo.close()

print "-----ALl DONE!------"

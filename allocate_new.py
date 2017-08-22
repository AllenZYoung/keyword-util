from random import shuffle

list1 = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALLOCATE-ULTRA-KEYWORD-LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALLOCATE-ULTRA-KEYWORD-LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALLOCATE-ULTRA-KEYWORD-LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALLOCATE-ULTRA-KEYWORD-LOWERSOURCE-wikiPlots_filter.txt',
]

list2 = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALLOCATE-ULTRA-SOURCE-ALL-LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALLOCATE-ULTRA-SOURCE-ALL-LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALLOCATE-ULTRA-SOURCE-ALL-LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALLOCATE-ULTRA-SOURCE-ALL-LOWERSOURCE-wikiPlots_filter.txt',

]
output_kw_path = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALL-KW.txt'
output_source_path = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/ALL-SOURCE.txt'


def Linenum_counter(path):
  ctr = 0
  with open(path, 'r') as f:
    for line in f:
      ctr += 1
  return ctr


list_kw = []
list_source = []
for i in range(0, 4):  # write keywords
  path1 = list1[i]
  with open(path1, 'r') as kw_f:
    # f_out = open(output_kw_path, 'a')
    if Linenum_counter(path1) % 3 != 0:
      print 'ERROR!'
      break
    ctr_line = 0
    case_kw = ''

    for line in kw_f:
      ctr_line += 1
      case_kw += line
      if ctr_line % 3 == 0:
        list_kw.append(case_kw)
        # f_out.write(case_kw)
        case_kw = ''

        # f_out.close()

for i in range(0, 4):  # write cases
  path2 = list2[i]
  with open(path2, 'r') as case_f:
    # f_out = open(output_source_path, 'a')

    ctr_line = 0

    for line in case_f:
      ctr_line += 1
      list_source.append(line)
      # f_out.write(case_source)
      case_source = ''

      # f_out.close()
print len(list_kw)
print len(list_source)
list_whole = zip(list_kw, list_source)

shuffle(list_whole)

f_out_kw = open(output_kw_path, 'a')
f_out_source = open(output_source_path, 'a')
for one in list_whole:
  keyword = one[0]
  case = one[1]
  f_out_kw.write(keyword)
  f_out_source.write(case)
f_out_kw.close()
f_out_source.close()

del list_kw
del list_source
print Linenum_counter(output_kw_path)
print Linenum_counter(output_source_path)

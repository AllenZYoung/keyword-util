list1 = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-wikiPlots_filter.txt',

]

list2 = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-wikiPlots_filter.txt',

]

list3 = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-wikiPlots_filter.txt',
]
list4 = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-ALL-V3LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-ALL-V3LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-ALL-V3LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-ALL-V3LOWERSOURCE-wikiPlots_filter.txt',

]
total = 0
for i in range(0, 4):
  path1 = list1[i]
  path2 = list2[i]
  path3 = list3[i]
  path4 = list4[i]
  ctr1 = ctr2 = ctr3 = ctr4 = 0
  with open(path1, 'r') as f1:
    for line in f1:
      ctr1 += 1
  with open(path2, 'r') as f2:
    for line in f2:
      ctr2 += 1
  with open(path3, 'r') as f3:
    for line in f3:
      ctr3 += 1
  with open(path4, 'r') as f4:
    for line in f4:
      ctr4 += 1
  print ctr1
  print ctr2
  print ctr3
  print ctr4 * 3
  total += ctr4
print ' Total:\t%d' % total

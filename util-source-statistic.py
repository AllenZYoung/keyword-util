raw_file = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/LOWERSOURCE-wikiPlots_filter.txt',
]

for file_path in raw_file:
  with open(file_path, 'r') as f:
    ctr_line = 0
    for line in f:
      ctr_line += 1
  print ctr_line

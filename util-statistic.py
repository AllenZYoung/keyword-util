filenames = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/wikiPlots_filter.txt',

  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-100word.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-book.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-movie.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-wikiPlot.txt',

  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-xxx-BOOK-20.txt',
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-xxx-MOVIE.txt',
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-xxx-WIKI.txt',
  # '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-xxx-100WORD.txt'
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/KEYWORD-n&v-100STORY-raw-18.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/KEYWORD-n&v-BOOK-raw-18.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/KEYWORD-n&v-MOVIE-raw-18.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/KEYWORD-n&v-WIKIP-raw-18.txt',



]
# set counters
ctr_total = 0
cat_ctr = 0

for filename in filenames:
  if cat_ctr % 4 == 0:
    print '-------------'
  cat_ctr += 1

  ctr_EXCEPTION = 0.0
  ctr_WORDNOTINVOC = 0.0
  ctr_CASE = 0.0
  ctr_SHORT = 0.0
  if filename.find('keyword') != -1:
    tag_index = filename.find('keyword')
  else:
    tag_index = filename.find('KEYWORD')

  briefname = filename[tag_index:]
  with open(filename) as rawfile:
    for line in rawfile:
      if str(line).find('NO VAR') != -1 or str(line).find('WORD NOT IN VOC') != -1:
        ctr_WORDNOTINVOC += 1
      if str(line).find('EXCEPTION\n') != -1:
        ctr_EXCEPTION += 1
      if str(line).find('TOO SHORT') != -1:
        ctr_SHORT += 1
      ctr_CASE += 1

    print 'For {}\n,There are {} cases contain the word not in voc, the proportion is {}, with {} cases in total. The exception is {}'.format(
      briefname,
      ctr_WORDNOTINVOC,
      round(
        float(
          ctr_WORDNOTINVOC / ctr_CASE),
        3),
      ctr_CASE,
      round(ctr_EXCEPTION / ctr_CASE, 3)
    )
    print 'TOO SHORT:{}, is {}'.format(ctr_SHORT, ctr_SHORT/ctr_CASE)
  ctr_total += ctr_CASE
  # print total


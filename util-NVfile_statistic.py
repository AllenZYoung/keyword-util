list_f = [

  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/NV-ULTRA-LOWERSOURCE-book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/NV-ULTRA-LOWERSOURCE-movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/NV-ULTRA-LOWERSOURCE-stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/NV-ULTRA-LOWERSOURCE-wikiPlots_filter.txt',

]

ctr = 0
for filename in list_f:
  if ctr % 4 == 0:
    print '--------'
  ctr += 1
  # print filename[filename.find('NV'):]
  ctr_line = 0
  ctr_E_NV = 0.0
  ctr_UNICODE = 0.0
  with open(filename, 'r') as f:
    for line in f:
      ctr_line += 1
      if line.find('NO NV') != -1:
        ctr_E_NV += 1
      if line.find('EXCEPTION: UNICODE ERROR') != -1:
        ctr_UNICODE += 1
        # print line

  print filename[filename.find('NV'):] + \
        '\n Lines: {}, Exception NV:{} Proportion:{} \n' \
        'Exception UNICODE:{} Proportion: {}\n'.format(ctr_line,
                                                     ctr_E_NV,
                                                     ctr_E_NV / ctr_line,
                                                     ctr_UNICODE,
                                                     ctr_UNICODE / ctr_line)

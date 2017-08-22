list_f = [

'/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/KEYWORD-ULTRA-ranked-V-ULTRA-LOWERSOURCE-book_summaries_filter.txt',
'/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/KEYWORD-ULTRA-ranked-V-ULTRA-LOWERSOURCE-movie_summaries_filter.txt',
'/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/KEYWORD-ULTRA-ranked-V-ULTRA-LOWERSOURCE-stories-100word_filter.txt',
]
ctr = 0
for filename in list_f:
  if ctr % 4 == 0:
    print '--------'
  ctr += 1
  # print filename[filename.find('NV'):]
  ctr_line = 0
  ctr_E_NV = 0.0
  ctr_SHORT = 0.0
  ctr_NOWORD = 0.0
  ctr_NOVAR = 0.0
  ctr_NOTINVOC = 0.0
  with open(filename, 'r') as f:
    for line in f:
      ctr_line += 1
      if line.find('NV file') != -1:
        ctr_E_NV += 1
      if line.find('TOO SHORT') != -1:
        ctr_SHORT += 1
      if line.find('NO WORD') != -1:
        ctr_NOWORD += 1
      if line.find('NOT IN VOC') != -1:
        ctr_NOTINVOC += 1
      if line.find('NO VAR') != -1:
        ctr_NOTINVOC += 1

        # if ctr_NOWORD == ctr_NOVAR == ctr_NOTINVOC == 0:
        #   print filename[filename.find('KEY'):] + \
        #   '\n Lines: {}, Exception NV:{} Proportion:{} \n'.format(ctr_line,
        #                                                           ctr_E_NV,
        #                                                           ctr_E_NV / ctr_line)
        # else:
    print filename[filename.find('KEY'):] + \
          '\n Lines: {}, Exception NV:\t{} Proportion:{} \n' \
          'Exception SHORT:\t{} Proportion: {}\n' \
          'Exception NO WORD:\t{} Proportion: {}\n' \
          'Exception NO VAR:\t{} Proportion: {}\n' \
          'Exception NOT IN VOC:\t{} Proportion: {}\n'.format(ctr_line,
                                                              ctr_E_NV,
                                                              ctr_E_NV / ctr_line,
                                                              ctr_SHORT,
                                                              ctr_SHORT / ctr_line,
                                                              ctr_NOWORD,
                                                              ctr_NOWORD / ctr_line,
                                                              ctr_NOVAR,
                                                              ctr_NOVAR / ctr_line,
                                                              ctr_NOTINVOC,
                                                              ctr_NOTINVOC / ctr_line
                                                              )

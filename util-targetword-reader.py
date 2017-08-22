filepath = r'/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/keyword-n&v-xxx-MOVIE-withwordsnotin.txt'
rawpath = r'/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/movie_summaries_filter.txt'
line_ctr = 0
import linecache
with open(filepath,'r') as f:
  # with open(rawpath,'r') as rf:
    word_list = set()
    for line in f:
      word_string = ''
      line_ctr += 1
      if line.find('NOT IN VOC') != -1:
        # words = line[]

        l = line[line.find('\t') + 1:line.find('<end>')].split(', ')[:-1]
        for one in l:
          word_list.add(one)
          word_string += one
          word_string +=' '

        word_string+='\n'
        print word_string
        print linecache.getline(rawpath,line_ctr)
    print word_list


  # s = 'GOT WORD NOT IN VOC:	hyp, interspecy, <end>	peace peace cohort '
  #
  # l = s[s.find('\t')+1:s.find('<end>')].split(', ')[:-1]
  # print l

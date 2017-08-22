import os

list_sourcefile = [
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/book_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/movie_summaries_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/stories-100word_filter.txt',
  '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/drive-download-20170817T081935Z-001/wikiPlots_filter.txt',
]
total = 0
for sourcefile in list_sourcefile:
  output_dir = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/'
  output_path = output_dir + 'LOWERSOURCE-' + sourcefile[sourcefile.find('-001') + 5:]
  ctr = 0

  with open(sourcefile) as sf:

    output_file = open(output_path, 'a')
    for line in sf:

      if ctr % 5000 == 0:
        print '5000 lines gone'

      ctr += 1
      line_lower = line.lower()
      output_file.write(line_lower)
    output_file.close()
  total += ctr
  print '{} lines in this file!'.format(ctr)
print '{} lines in total'.format(total)

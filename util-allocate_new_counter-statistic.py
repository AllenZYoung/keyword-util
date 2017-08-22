# list1 = [
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-book_summaries_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-movie_summaries_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-stories-100word_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-1-V3LOWERSOURCE-wikiPlots_filter.txt',
#
# ]
#
# list3 = [
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-book_summaries_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-movie_summaries_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-stories-100word_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-KEYWORD-ranked-V-ULTRA-LOWERSOURCE-wikiPlots_filter.txt',
# ]
#
# list2 = [
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-book_summaries_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-movie_summaries_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-stories-100word_filter.txt',
#   '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/ALLOCATE-ULTRA-SOURCE-2-V3LOWERSOURCE-wikiPlots_filter.txt',
# ]
#
# from allocate_new import Linenum_counter
#
# total = 0
# for i in range(0, 4):
#   f1 = open(list1[i], 'r')
#   f2 = open(list2[i], 'r')
#   f3 = open(list3[i], 'r')
#   print '------'
#   print 'File1'
#   a1 = Linenum_counter(list1[i])
#   total += a1
#   print a1
#   print 'File2'
#   print Linenum_counter(list2[i])
#   print 'File3'
#   print Linenum_counter(list3[i])
#
#   for line in f1:
#     if line.find('EXCEPTION') != -1:
#       print 'EXCEPTION'
#
#   for line in f2:
#     if line.find('EXCEPTION') != -1:
#       print 'EXCEPTION'
#   for line in f3:
#     if line.find('EXCEPTION') != -1:
#       print 'EXCEPTION'
#
#   f1.close()
#   f2.close()
#   f3.close()
# print 'total = %d' % (total / 3)


output1_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-1-SHUFFLE.txt'
output1_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-1-UNSHUFFLE.txt'
output3_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-2-SHUFFLE.txt'
output3_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-2-UNSHUFFLE.txt'
output_kw_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/KW-SHUFFLE.txt'
output_kw_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/KW-UNSHUFFLE.txt'

from allocate_new import Linenum_counter
print '---------------'
print Linenum_counter(output1_unshuffle)
print Linenum_counter(output1_shuffle)
print Linenum_counter(output3_unshuffle)
print Linenum_counter(output3_shuffle)
print Linenum_counter(output_kw_unshuffle)
print Linenum_counter(output_kw_shuffle)

from allocate_new import Linenum_counter

output1_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-1-SHUFFLE.txt'
output1_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-1-UNSHUFFLE.txt'
output3_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-2-SHUFFLE.txt'
output3_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/SOURCE-2-UNSHUFFLE.txt'
output_kw_shuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/KW-SHUFFLE.txt'
output_kw_unshuffle = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/winrar/KW-UNSHUFFLE.txt'

list_raw = []
list_raw.append(output1_shuffle)
list_raw.append(output1_unshuffle)
list_raw.append(output3_shuffle)
list_raw.append(output3_unshuffle)
list_raw.append(output_kw_shuffle)
list_raw.append(output_kw_unshuffle)

border1 = 302070
border2 = 339828


def process_one_raw(input, o_train, o_valid, o_test):
  if input.find('-SHUFFLE') != -1:
    print 'SHUFFLE FILE HERE'
  if input.find('-UNSHUFFLE') != -1:
    print 'UNSHUFFLE FILE HERE'

  f1_r = open(input, 'r')
  f1_o1 = open(o_train, 'a')
  f1_o2 = open(o_valid, 'a')
  f1_o3 = open(o_test, 'a')

  ctr1 = 0
  for line in f1_r:
    ctr1 += 1
    if ctr1 <= border1:
      f1_o1.write(line)
    elif ctr1 <= border2:
      f1_o2.write(line)
    else:
      f1_o3.write(line)

  f1_o1.close()
  f1_o2.close()
  f1_o3.close()
  f1_r.close()
  print '------\nDone!'
  INPUT = Linenum_counter(input)
  O1 = Linenum_counter(o_train)
  O2 = Linenum_counter(o_valid)
  O3 = Linenum_counter(o_test)
  print 'I :{}\tO1:{}\tO2:{}\tO3:{}\tSUMO:\t{}'.format(INPUT, O1, O2, O3, O1 + O2 + O3)
  print '----'


def path_maker(rawpath, choice):
  if choice == 1:
    tail = '-train.txt'
  elif choice == 2:
    tail = '-valid.txt'
  elif choice == 3:
    tail = '-test.txt'
  else:
    print 'ERROR'
    return None
  path = '/Users/zhangyang/PycharmProjects/IdiomSpider/stage-nd/newdir/811/' + rawpath[
                                                                               rawpath.find('winrar/') + 7:rawpath.find(
                                                                                 '.txt')] + tail
  return path

def ultra_process(raw):
  process_one_raw(raw, path_maker(raw,1),path_maker(raw,2),path_maker(raw,3))


if __name__ == '__main__':
  for one in list_raw:
    ultra_process(one)
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''

from utility import CHARACTERS

def approach1(fpath):
  scores = []
  f = open(fpath, 'r')
  names = [name[1:-1] for name in f.readline().split(",")]
  names.sort()
  for name in names:
    scores.append((names.index(name)+1) * sum([CHARACTERS.index(s)+1 for s in name]))

  print sum(scores)

approach1('names.txt')

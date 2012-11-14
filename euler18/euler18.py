from MyTimer import Timer

def euler18(fpath):
  tri = []
  for line in open(fpath, 'r'):
    tri.append([int(num) for num in line.split(" ")])

  cost = costMax(tri)
  for line in cost:
    print line


def routeMax(tri):
  if len(tri) != 1:
    head = tri[0][0]
    left = map((lambda line, count: line[:count]), 
                tri[1:], [i for i in range(1, len(tri))])
    right = [line[1:] for line in tri[1:]]
    if routeMax(left) > routeMax(right):
      return head + routeMax(left)
    else:
      return head + routeMax(right)
  else:
    return tri[0][0]


def costMax(tri):
  tri.reverse()
  cost = tri[:]
  for i in range(1, len(tri)):
    line = tri[i]
    prev = tri[i-1]
    for j in range(len(line)):
      larger = max(prev[j], prev[j+1])
      cost[i][j] += larger

  return cost

euler18('complex.txt')
t = Timer("euler18('triangle.txt')", "euler18")
t.timeit()

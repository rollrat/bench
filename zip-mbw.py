# [줄:1 -> 첫번째 total bytes<->block size 쌍 - memcpy]: [200개의 결과값 가로줄]
# [줄2: 같은 경우의 dumb]: [...]
# [줄3: 같은 경우의 mcblock]: [...]
# [줄4: 다음 경우의 memcpy]: ...

src_dir = 'result/mbw/10'
result_fn = 'r-mbw-10.csv'

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]


target_sizes='1024 2048 4096 6120 8192'.split(' ')
block_sizes='1 32 64 128 256 512 1024 1536 2048 3072 4096 6120 8192 12288 16384 20480 25600 31200 32768 40000 45000 50000 65000 65536'.split(' ')

mode = 'debug'

result = {}
result_cnt = {}

for i in range(5):
  for tsz in target_sizes:
    for bsz in block_sizes:
      f = str(i)+ '.'+tsz+'.'+bsz+'.'+mode
      body = open(join(src_dir, f), 'r').readlines()

      # memcpy = body[0].split('\t')
      # dumb = body[1].split('\t')
      # mcblock = body[2].split('\t')

      n = '('+tsz+'-'+bsz+')'
      if not n in result:
        result[n] = []
        result_cnt[n] = []

        for j in range(3):
          result[n].append([])
          result_cnt[n].append(0)

      for j in range(3):
        for a1 in body[j].split('\t'):
          if a1.isnumeric():
            result[n][j].append(int(a1))
            result_cnt[n][j] += 1

# output
o = open(result_fn, 'w')
for p in result:
  o.write(p)
  o.write(',')
o.write('\n')

for j in range(3):
  for p in result:
    def avg(n):
      s = 0
      for z in result[p][n]:
        s += z
      return s/result_cnt[p][n]
    o.write(str(avg(j)))
    o.write(',')
  o.write('\n')

o.close()
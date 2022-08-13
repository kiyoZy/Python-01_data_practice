# 縦横変換
# 最初の文字列だけを取り出し
# 縦の文字列を横に変換する


import sys

from pyparsing import line
from sympy import Idx

print('起動ファイルと引数', sys.argv)

try:
    path = sys.argv[1]
except:
   print('ファイルをドラッグしていないからexcept')
   input('stop except')

#path=r'C:\data_02.txt'

# ファイル読み込み
with open(path, encoding='utf-8', mode='r') as f:
    lines = f.readlines()


# ファイル書き出し
with open('y_out.txt', 'w', encoding='SHIFT-JIS') as fw:
    for l in lines:
        l = ','.join(l.split())
        idx = l.find(',')
        s = l[:idx]

        fw.write(s)
        fw.write('\t')


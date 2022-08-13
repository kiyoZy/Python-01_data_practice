# そのままpyファイルにドラッグ出来ない場合
# batにpyの起動が書いてある
# python 05_read_argument.py %*
# batに読み込ませたいファイルをドロップ

# [読み込みと整形]
# 連続した空白は1つにする
# 区切りは「,」カンマにする　※print()の場合タブ（joinによる「\t」の追加は微妙）
# 「月」の後の「空白→，」を削除する

# てきとーなファイル名で出力。　ひとまずcsv

import sys
print('起動ファイルと引数', sys.argv) # [hoge.py, c:\hoge.txt] など

# 全行読み取り
#path = 'data.txt'

print('csv\t','テスト')
print('csv\tテスト')

try:
    path = sys.argv[1]
except:
    print('ファイルをドラッグしていないからexcept')
    input('stop except')

print('ファイルドラッグOK!')

with open(path, encoding='utf-8', mode='r') as f:
    lines = f.readlines()
'''
    for l in lines:
#        l = '\t'.join(l.split())
        l = l.split()
        print(l)
        l = '  '.join(l)
 #       l = ''.join(l.replace('月\t', '月'))
        print(l)
'''

with open('z_out.csv', 'w', encoding='SHIFT-JIS') as fw:
    for l in lines:
        l = ','.join(l.split())
        l = ''.join(l.replace('月,', '月'))
        fw.write(l)
        fw.write('\n')
    fw.write('タブ,テスト')
        
with open('z_out.txt', 'w', encoding='UTF-8') as fw:
    for l in lines:
        l = '\t'.join(l.split())
        l = ''.join(l.replace('月\t', '月'))
        fw.write(l)
        fw.write('\n')

    fw.write('タブ\tテスト')

#input('enter to exit')

#　リストをシリーズに変換
import pandas as pd

list = ['a', 'bb', 'ccc', 'd']
print(list)
#　↓
#['a', 'bb', 'ccc', 'd']


sr = pd.Series(list)
print(sr)
#　↓
#0      a
#1     bb
#2    ccc
#3      d
#dtype: object

print('\n')
#　シリーズをリストに変換
import pandas as pd

sr = pd.Series( ['aa', 'bb', 'cc', 'd'])
print(sr)
#　↓
#0      a
#1     bb
#2    ccc
#3      d
#dtype: object

str = sr.values.tolist()
print(str)
#['aa', 'bb', 'cc', 'd']

#　リストを文字列へ
#　文字数を合わせ最後に「コロン（:）」をくっつけて一つの文字列へ
list = ['', '1', '12', '123', '1234', '12345', '1234567890']


#　もうちょっとスマートに出来ないかなぁ？
con = ''
for str in list:
    str = str[0:3]+'_' #　文字数で切り取る
    #str =str.ljust(4)+':' #　5個目
    con += str

print(con)

'''
#　joinを使うと楽だけど文字数が合わせられない
A = ["a", "b", "c"]
StrA = "".join(A)
print(StrA)
## StrA is "abc"
'''



print('\n')
#　「0（ゼロ）」埋め
#　元の文字数が大きいと指定文字より大きくなる

list = ['aa', 'bb', 'cc', 'd', '1234567890']

con = ''
con02 = ''
for str in list:
    con += str.ljust(8)+':'
    con02 += str.zfill(8)

print(con)
print(con02)


print('\n')
#　長さをそろえたいけど　でも文字ははみ出しちゃう
print("[" + "Apple".ljust(8) + "]")
print("[" + "Apple".center(8) + "]")
print("[" + "Apple".rjust(8) + "]")
print("[" + "AppleJuice".rjust(8) + "]")


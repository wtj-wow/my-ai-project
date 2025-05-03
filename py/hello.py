#自介
name='王泰鈞' #名
dream='工程師'#夢想職業

import datetime#時間模組

birth_year=2009 #出生年
current_year=+datetime.datetime.now().year#當前年分

age=current_year-birth_year #年齡

#自介
print('hello,world')
print('大家好我叫',name)
print('今年',age,'歲')
print('我想成為一個傑出的',dream)
print('我超愛寫程式未來想上成大資工~')

#詢問
name=input('你叫什麼名字?')
dream=input("你的夢想職業是甚麼?")
print('hi',name,'你想成為',dream,'要加油喔!!')

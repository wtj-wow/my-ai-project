#基本資料
name= "王泰鈞" #名字
dream = 'Software Engineer' #夢想職業

#我的年齡 (用 datetime 自動取得今年年份)
import datetime#引入時間模組
birth_year=2009 #出生年
current_year = datetime.datetime.now().year#目前年分
age=current_year-birth_year #年齡計算

#自介
print("大家好，我是", name)
print("I'm", age, "years old.")
print("My dream is to become a", dream + "!")
print("我超喜歡寫程式，未來想上成大資工～🚀")
print('我正在學python!')

#對話
name=input("你的名字是?")

dream=input("你未來想成為甚麼?")

#鼓勵語鼓勵語
print("Hi", name + "！")
print("你想當", dream + "，太酷了！要為了夢想努力唷，加油！！💪🔥")

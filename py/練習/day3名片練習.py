#收集各資變數
name=input("你的名字叫甚麼?")
hobby=input("你的興趣是什麼?")
dream=input("你有什麼夢想?")
skill=input("你想學會甚麼實用的技能?")

# 將 age 轉換為整數
try:
    age = int(input("你今年幾歲?"))  
except ValueError:
    print("請輸入有效的數字！")
    exit()

#日期加變數設定
import datetime
today=datetime.datetime.now()

#輸出
line="_"*30
print(f"\n{line}\n{name.upper().center(30)}的名片\n{line}")
print(f"👤姓名:{name.ljust(10)}")
print(f"🎂年齡:{age}")
print(f"💖興趣:{hobby.ljust(10)}")
print(f"🚀夢想:{dream.ljust(10)}")
print(f"🧠想學的技能:{skill.ljust(10)}")

#祝福與判斷式祝福與判斷式
if age >= 20:
    print(f"你完成{dream}的夢想了嗎?如果還沒，加油你可以的!!!")
elif age >=13:
    print(f"你找到目標了嗎?找到了就要努力去做!!!")
else:
    print(f"好好玩吧!")
print(f"{today.year}/{today.month}/{today.day}")
print(f"\n{line}\n{line}")
      
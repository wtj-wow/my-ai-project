import random

a = random.randint(1, 5)

b = int(input("數字是幾？"))  # 將輸入轉換為整數
if a == b:
    print("答對了！")
else:
    print("是", a)
#基本資料變數設定
name=input('你叫什麼呢?')#詢問名字
hobby=input('你喜歡甚麼呢?')#詢問興趣
skill=input("你想學習什麼技能呢?")#詢問想學的技能
age=input('你幾歲?')#詢問年齡
dream=input('你的夢想職業是什麼?')#詢問夢想職業

line='_'*10#10個底線

print(f"{line}Your COOL ID{line}")#第一段底線#f-string格式
print("Hi,my name is ",(name),"!")
print("I'm ",(age),"years old")
print(f"I love{hobby}my dream is to become a{dream}!") #f-string格式
print("now I'm learning",(skill),)
print(line*4)
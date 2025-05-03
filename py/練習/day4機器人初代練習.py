#開場輸入語句
print("🌞 歡迎使用你的每日心情AI小幫手，今天過得如何?")
print("輸入[q]離開")

#引入模組
import datetime

#建立清單
records=[]

#迴圈
while True:
    try:
        today=datetime.datetime.now().strftime("%Y-%m-%d %H")#今天時間
        mood=input("今天心情如何?是開心?是難過?是悲傷?還是其他?")#輸入心情

        if mood=="q" or mood=="Q":
            print('明天見，掰掰')
            break#離開程式
        record={"date":today,"mood":mood}#建字典
        records.append(record)#加入文件
        #輸入成功
        print(f"✅ 已記錄：🗓️ {today} \n😊 心情：{mood}")
        print("GPT:有時候你覺得自己在原地打轉，其實你是在蓄力開大招。別急，等你轉夠圈，一出手就會超帥✨")

    except Exception as e:
        print(f"發生錯誤{e}")
    #開場輸入語句
print("🌞 歡迎使用你的每日心情AI小幫手，今天過得如何?")
print("輸入[q]離開")

#引入模組
import datetime

#建立清單
records=[]

#迴圈
while True:
    try:
        today=datetime.datetime.now().strftime("%Y-%m-%d %H")#今天時間
        mood=input("今天心情如何?是開心?是難過?是悲傷?還是其他?")#輸入心情

        if mood=="q" or mood=="Q":
            print('明天見，掰掰')
            break#離開程式
        record={"date":today,"mood":mood}#建字典
        records.append(record)#加入文件
        #輸入成功
        print(f"✅ 已記錄：🗓️ {today} \n😊 心情：{mood}")
        print("GPT:有時候你覺得自己在原地打轉，其實你是在蓄力開大招。別急，等你轉夠圈，一出手就會超帥✨")

    except Exception as e:
        print(f"發生錯誤{e}")
    


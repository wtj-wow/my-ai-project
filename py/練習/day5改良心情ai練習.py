#開場
print("歡迎使用你專屬的心情小日記😇")
print("我會記錄下你所有的小心情，讓你隨時回顧！🥰")
print("如果想要結束，請輸入 (q)，謝謝！🙏")
print("若要回顧請輸入(view)")
print("讀完了嗎?進入你的心情世界吧!!📝")
print("===============================================")
#引入模組
import datetime

#建資料夾
records=[]

#迴圈
while True:
    try:
        today=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        mood=input("🤖:今天你的心情如何呢?")
        if mood=="q":
            print("🤖:謝謝你使用心情小日記，期待下次見面！")
            break
        record={"date":today,"mood":mood}
        print(f"🤖:今天的心情是:{mood},{today}")
        print("已記錄到心情日記當中了📂")
        
        #加入資料
        records.append(record)

        #顯示所有紀錄
        if mood.lower()=="view":
            print("\n這是你之前的心情🔐:/n")
            for record in records:
                print(f"🗓️ {record['date']} | 😊 心情：{record['mood']}")
    except Exception as e:
        print(f"發生錯誤{e}")
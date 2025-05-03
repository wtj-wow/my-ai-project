#開場
print('🤖:歡迎來到專屬於你的心情記錄小助手!')
print("🤖:輸入心情就會記錄\n輸入[view]查看紀錄\n輸入[q]可以離開程式")
print("================================================")

#模組
import datetime

#資料庫建立
records=[]

#主程式
while True:
    try:
        today=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        mood=input(f"🤖:今天心情如何呢過的怎麼樣?")
        record={"date":today,"mood":mood}
        records.append(record)
        print("✅ 心情已記錄完成")
        if mood.lower()=='q':
            print("🤖:謝寫使用明天見，助你天天快樂，掰掰")
            break
        elif mood.lower()=='view':
            if len(records)==0:
                print("🤖:沒有資料喔")
            else:
                print("🤖:讓我們看看你之前的紀錄吧\n")
                for r in records:
                    print(f"{r['date']} : {r['mood']}")
    except Exception as e:
        print(f"🤖:發生錯誤{e}")
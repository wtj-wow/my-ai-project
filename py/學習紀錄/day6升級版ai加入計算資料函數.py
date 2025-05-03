import datetime

print("🌈 歡迎來到你的心情日記本！")
print("輸入心情開始記錄，輸入 view 查看記錄，輸入 q 離開")

records = []  # 建立一個空清單來存放心情記錄

while True:
    try:
        mood = input("📝 今天心情如何？ ")

        if mood.lower() == "q":
            print("📕 日記關閉囉，明天見！")
            break

        elif mood.lower() == "view":
            print("\n🔍 目前的心情記錄：")
            for r in records:
                print(f"🗓️ {r['date']} | 😊 心情：{r['mood']}")
            print(f"🧮 你一共記錄了 {len(records)} 筆心情。")
            continue

        # 建立記錄
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        record = {"date": today, "mood": mood}
        records.append(record)

        print("✅ 已記錄你的心情 ✔")
    except Exception as e:
        print(f"⚠️ 發生錯誤：{e}")

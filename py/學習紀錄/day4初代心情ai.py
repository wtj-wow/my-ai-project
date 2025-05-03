# Day 4 任務：心情日記 AI + 基礎語法練習

# 📝 今日目標：學會 try...except、for 迴圈、list 概念，並能應用在簡單的「心情紀錄 AI」中

# ✅ 任務一：輸入今天的心情（搭配日期）
import datetime

# 建立空的紀錄清單
records = []

while True:
    try:
        today = datetime.datetime.now().strftime("%Y-%m-%d %H ")
        mood = input("今天心情如何？（開心/難過/普通...）: ")
        if mood == "q":
            break
        record = {"date": today, "mood": mood}
        records.append(record)
        print("紀錄完成！輸入 q 可以離開，或繼續紀錄下一筆。")
    except Exception as e:
        print("發生錯誤：", e)

# ✅ 任務二：顯示所有紀錄
print("\n🔎 目前的心情紀錄：")
for record in records:
    print(f"🗓️ {record['date']} | 😊 心情：{record['mood']}")

# ✅ 小補充：for in 是什麼？
# for record in records 的意思是：
# 逐一取出 records（list）中的每個元素，並用 record 這個變數代表它。

# ✅ 小補充：list 是什麼？
# list 就是一串資料的集合，例如：
# records = [ {'date': '2025-04-21', 'mood': '開心'}, {'date': '2025-04-22', 'mood': '普通'} ]
# 它裡面可以放很多字典（dict）或數字、文字等資料

# ✅ 小補充：try...except 是什麼？
# 是用來捕捉錯誤的，避免程式中斷。try 裡放可能出錯的程式碼，except 接住錯誤。
# 如果 user 亂輸入，也能好好顯示錯誤，不讓程式爆掉。

# ✅ 今日任務結束！
# 如果你完成以上任務，代表你已經學會：
# 1. 用 list 儲存紀錄
# 2. 用 for 讀取每筆紀錄
# 3. 用 try...except 保護程式不當機
# 4. 用 while 讓使用者可以一直輸入資料

# 明天我們會再練習 while + if 的更進階應用，並試著讓資料存進檔案中！🚀

# 💬 GPT 勵志語錄
print("\n💡 今天的勵志一句：")
print("就算是 while 迴圈，也得不斷嘗試，才會找到正確的 exit！😂")

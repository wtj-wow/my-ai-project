import datetime

# 讀取歷史紀錄（如果有的話）
def read_previous_records():
    try:
        with open("mood_records.txt", "r") as file:
            records = file.readlines()
            print("\n過去的心情紀錄：")
            for record in records:
                print(record.strip())
    except FileNotFoundError:
        print("目前沒有任何歷史紀錄。\n")

# 保存當前紀錄到檔案
def save_record(mood, note):
    today = datetime.datetime.now()
    with open("mood_records.txt", "a") as file:
        file.write(f"{today.strftime('%Y/%m/%d')} - 心情: {mood} - 註解: {note}\n")

# 主程式
print("👋 歡迎來到每日心情紀錄 AI")
print("輸入你的心情（數字 1～10）和一句話描述吧～")
print("輸入 'q' 可以離開\n")

# 顯示過去的紀錄
read_previous_records()

while True:
    mood_input = input("你的今天心情指數 (1~10) 是？👉 ")

    if mood_input.lower() == "q":
        print("📔 感謝使用，明天見！")
        break

    try:
        mood = int(mood_input)
        if mood < 1 or mood > 10:
            print("⚠️ 請輸入 1 到 10 的數字！\n")
            continue
    except ValueError:
        print("⚠️ 請輸入有效的數字喔！\n")
        continue

    note = input("你想對今天說的一句話是？📝 ")

    # 保存紀錄到檔案
    save_record(mood, note)

    print(f"\n🗓️ 今天是：{datetime.datetime.now().strftime('%Y/%m/%d')}")
    print(f"😃 你的心情指數：{mood}")
    print(f"💬 你今天想說的是：{note}\n")

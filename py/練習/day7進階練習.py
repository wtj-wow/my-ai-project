#開場白
print("🤖:歡迎使用計算機小助手!!!")

#可愛的函數們
def add(x, y):
    return x + y 
        
def subtract(x, y):
    return x - y
        
def multiply(x, y):
    return x * y
        
def divide(x, y):
    return x / y

#迴圈
while True:
    try:
        x=int(input("🤖:第一個數字?"))
        z=input("🤖:請選擇運算（+、-、*、/）")
        y=int(input("🤖:第二個要運算的數字?"))
        
        
        if z=="+":
            print(f"🤖:結果是{add(x, y)}")
        elif z=="-":
            print(f"🤖:結果是{subtract(x, y)}")
        elif z=="*":
            print(f"🤖:結果是{multiply(x, y)}")
        elif z=="/":
            print(f"🤖:結果是{divide(x, y)}")
        else:
            print("🤖:請輸入正確的計算符號!!!")    
    except Exception as e:
        print(f"發生錯誤{e}，請輸入正正確的符號!!!")
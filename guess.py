password = "a123456"
input_num = 3
while True:
    pw = input("請輸入密碼")
    if pw != password:
        input_num -= 1
        print("密碼錯誤！還有 " + str(input_num) + " 次機會")
        if input_num == 0:
            print("密碼錯誤！沒有輸入機會了")
            break
    elif pw == password:
        print("登入成功")
        break

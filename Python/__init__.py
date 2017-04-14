#line = int(input("Diamond 의 길이를 입력하세요(2~30) : "))
line = int(10)
for p in range(1, line * 2, 2):
    print((" " * ((line * 2 - 1 - p) // 2)) + ("*" * p))

print("====================================================")

#임시 배열 생성
#tmp_arr = [11,20,33,99,10,11,13,12]
tmp_arr = [11,20,33,11]
print(tmp_arr)

print("====================================================")

cnt = 0;

# 가지고 있는 데이터 만큼
for x in tmp_arr:
    tmp = str(x)
    print ("들어온 문자열: %s (%d)자리" % (x, len(tmp)))

    # 해당 데이터의 사이즈만큼 확인
    for y in tmp:
        print(y)

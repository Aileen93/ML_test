import re

# http://www.flowdas.com/thinkpython/08-strings/

# 848757.정규식 체크
print ('848757) 정규식 match 확인 : ', bool(re.match('[a-c]{3}', 'aaa')))
print ('-------------------------------------------------------');

# 사용할 함수 정의 ---------------------------------------------------------

# {} 반복할 숫자
def repeatExp (num):
    num = str(num)
    val =  '{' + num + '}'
    return val

# -------------------------------------------------------------------------------------------
# 3204844.String 배열로 출력
inputArr = ['ff7d8ff88']; #,'djfieojifeji123','123hud22','anwlro88'
print ('3204844) inputArr :', inputArr);
print ('-------------------------------------------------------');

# 특정 문자열을 기준으로 자르고 싶을 경우, String.split('|^|')을 사용하여 가능
# 623154. inputArr에서의 n번째 String
i = 0; #inputArr 개수
j = 0; #inputArr[i]번째의 String 문자

delimiter = '||'  # 각 배열의 순서를 확인할 구분자 ||

cLower = 'a' #소문자 형식
cNum = '0' #숫자 형식
cUpper = 'A' #대문자 형식
cSpe = '@' # 특수문자 형식

# 78787878) 숫자, 영소문, 영대문, 특수문자
numExp = '[0-9]' # 숫자 정규식
lowerExp = '[a-z]' # 소문자 정규식
upperExp = '[A-Z]' # 대문자 정규식
speExp = '' # 특수문자 정규식
permitArr = '@|^|-|^|_|^|.'.split('|^|') #허용할 특수문자

#가장 높은 알파벳
#가장 낮은 알파벳

# inputArr[i][j]
#tmp_pattern  = ['']*len(inputArr[i]) #초기화 # ★ 동적으로 배열 할당하고 쓰는 방법 알아보기
tmp_pattern = [''] * len(inputArr)  # 초기화 # ★ 동적으로 배열 할당하고 쓰는 방법 알아보기
#print('==>', len(tmp_pattern), ', ', tmp_pattern)

# 새로운 문자열들로 바꿀 tmp
newInputArr = ['']*len(inputArr)

# 각 알파벳으로 바꾸어서 새로운 tmpArr에 넣어주기

# ======================================> 실제
while (i < len(inputArr)):
    print('\n ===문자열 변경하기===☞ inputArr[',i,'] 문자열 ',inputArr[i], '패턴 검색 시작! [',len(inputArr[i]),'] 자리 ☜=====')
    while (j < len(inputArr[i])):
        print ('현재 문자열 :',inputArr[i][j], (i,j))

        repeatStr = ''
        num = 1
        # ============================================================ 소문자
        if (bool(re.match(lowerExp, inputArr[i][j]))):
            newInputArr[i] = newInputArr[i] + 'a'
            print('------------------->',num, ', 최종 :'+newInputArr[i])

        # ============================================================ 대문자
        elif (bool(re.match(upperExp, inputArr[i][j]))):
            newInputArr[i] = newInputArr[i] + 'A'
            print('------------------->',num, ', 최종 :'+newInputArr[i])

        # ============================================================ 숫자
        elif (bool(re.match(numExp, inputArr[i][j]))):
            newInputArr[i] = newInputArr[i] + '0'
            print('------------------->',num, ', 최종 :'+newInputArr[i])

        # ============================================================ 특수문자
        elif (bool(re.match(upperExp, inputArr[i][j]))):
            newInputArr[i] = newInputArr[i] + '@'
            print('------------------->',num, ', 최종 :'+newInputArr[i])

        isDiffer = False
        j = j+1
        if( j == len(inputArr[i])):
            j = 0
            break
    i = i+1

print('★신규 문자열 :::::::::::::::::::::::::::::: 최종',newInputArr)
print('-------------------------------------------------------');

# ======================================> 실제
while (i < len(inputArr)):
    print('\n =====☞ inputArr[',i,'] 문자열 ',inputArr[i], '패턴 검색 시작! [',len(inputArr[i]),'] 자리 ☜=====')
    while (j < len(inputArr[i])):
        print ('현재 문자열 :',inputArr[i][j], (i,j))

        repeatStr = ''
        num = 1
        # ============================================================ 소문자
        if (bool(re.match(lowerExp, inputArr[i][j]))):
            # 현재 문자열과 다음 문자열이 같을 경우,
            if (j < len(inputArr[i]) - 1 and (inputArr[i][j] == inputArr[i][j + 1])):
                num = num + 1 #카운트 수만 늘려줌
                #print ('====> (',inputArr[i][j],') next char :', inputArr[i][j+1], 'num :', num)

            tmp_pattern[i] = tmp_pattern[i] + '[a-z]'+repeatExp(num)
            if(num >= 2):
                j = j + 1
                print (j)
            print('------------------->',num, ', 최종 :'+tmp_pattern[i])

        # ============================================================ 대문자
        elif (bool(re.match(upperExp, inputArr[i][j]))):
            if (j < len(inputArr[i]) - 1 and (inputArr[i][j] == inputArr[i][j + 1])):
                num = num + 1 #카운트 수만 늘려줌

            tmp_pattern[i] = tmp_pattern[i] + '[A-Z]'+repeatExp(num)
            print('------------------->',num, ', 최종 :'+tmp_pattern[i])
            if(num >= 2):
                j = j + 1

        # ============================================================ 숫자
        elif (bool(re.match(numExp, inputArr[i][j]))):
            if ( j < len(inputArr[i])-1 and (inputArr[i][j] == inputArr[i][j + 1])):
                num = num + 1 #카운트 수만 늘려줌

            tmp_pattern[i] = tmp_pattern[i] + '[0-9]'+repeatExp(num)
            print('------------------->',num, ', 최종 :'+tmp_pattern[i])
            if(num >= 2):
                j = j + 1

        # ============================================================ 특수문자
        elif (bool(re.match(upperExp, inputArr[i][j]))):
            if (j < len(inputArr[i]) - 1 and (inputArr[i][j] == inputArr[i][j + 1])):
                num = num + 1 #카운트 수만 늘려줌

            tmp_pattern[i] = tmp_pattern[i] + '[특문]'+repeatExp(num)
            print('------------------->',num, ', 최종 :'+tmp_pattern[i])
            if(num >= 2):
                j = j + 1

        if( j == len(inputArr[i])):
            j = 0
            break
    i = i+1

print('★최종',tmp_pattern)
print ('-------------------------------------------------------');

# 패턴 매치 실행해보기
print ('100001) 정규식 match 확인! input :[',inputArr[0],'] ==☞ result :', bool(re.match(tmp_pattern[0], inputArr[0])))
#print ('100001) 정규식 match 확인! input :[',inputArr[1],'] ==☞ result :', bool(re.match(tmp_pattern[1], inputArr[1])))
#print ('100001) 정규식 match 확인! input :[',inputArr[2],'] ==☞ result :', bool(re.match(tmp_pattern[2], inputArr[2])))
#print ('100001) 정규식 match 확인! input :[',inputArr[3],'] ==☞ result :', bool(re.match(tmp_pattern[3], inputArr[3])))

print ('-------------------------------------------------------');
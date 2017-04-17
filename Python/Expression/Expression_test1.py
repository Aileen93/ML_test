import re
import numpy as np
import matplotlib.pyplot as plt

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

# ---------------------------------------------------------------------- 파일 읽어들이기

# mjk2072 82 01031332072 @naver.com 11

# ---------------------------------------------------------------------------------------

# 제재를 당한 아이디들을 모두 가져옵니다.
idArr = ['usb07fl','o377jja','bdi3p77', 'rlsns1h','y12655u','usb07fl']
emailArr = ['@textnow.me','@textnow.me','@textnow.me','@naver.com','@textnow.me','@textnow.me']

cntryArr = ['88','88','88','82','88','88']
phoneArr = ['01072341111','01033331111','01072341112','01072341113','01072341114','01072341119']
regPathArr = ['11','11','11','11','11','11']


# -------------------------------------------------------------------------------------------
# 3204844.String 배열로 출력
inputArr = idArr
print ('3204844) inputArr :', inputArr)
print ('-------------------------------------------------------');

# 특정 문자열을 기준으로 자르고 싶을 경우, String.split('|^|')을 사용하여 가능
# 623154. inputArr에서의 n번째 String
i = 0; #inputArr 개수
j = 0; #inputArr[i]번째의 String 문자

cLower = 'a' #소문자 형식
cNum = '0' #숫자 형식
cUpper = 'A' #대문자 형식

# 78787878) 숫자, 영소문, 영대문, 특수문자
numExp = '[0-9]' # 숫자 정규식
lowerExp = '[a-z]' # 소문자 정규식
upperExp = '[A-Z]' # 대문자 정규식
speExp = '([-_.@])' # 특수문자 정규식 (허용할 특수문자들을 넣읍시다.
permitArr = '@|^|-|^|_|^|.'.split('|^|') #허용할 특수문자





# 이 값들을 어떻게 수치화 할 것인가? =====================================================
# 이메일 전체 건수, 각 도메인별 건수, 그래서 최종 도메인별 랭킹에 따른 점수화
# 국가번호 전체 건수, 각 국가번호별 건수, 그래서 최종 국가번호 랭킹에 따른 점수화
# 이건 휴대폰 번호 반복되는 패턴을 찾아놔야함 > 랭킹화
# 가입경로는 번호로 따져있으니까 이미, 이건 그냥 더합시다.

zzzzzzzzzzzzz = 'usb07fl'
trASC = ''
k = 0
while len(zzzzzzzzzzzzz):
    trASC = trASC + str(ord(zzzzzzzzzzzzz[k]))
    k = k + 1
    if(k == len(zzzzzzzzzzzzz)):
        break

ulen = 0

print('===================================>>>>', chr(65))

intStartCharNum = 0
intEndCharNum = 2
print('최종 :::',trASC) # usb07fl

while len(trASC):

    # 소문자 형식인지 확인
    if (bool(re.match(lowerExp, chr(int(trASC[intStartCharNum:intEndCharNum]))))):
        print('=====> [결과] ::',bool(re.match(lowerExp, chr(int(trASC[intStartCharNum:intEndCharNum])))),'소문자 성공 ::', chr(int(trASC[intStartCharNum:intEndCharNum])))
        intStartCharNum = intEndCharNum
        intEndCharNum = intStartCharNum + 2
    elif (bool(re.match(numExp, chr(int(trASC[intStartCharNum:intEndCharNum]))))):
        print('=====> [결과] ::', bool(re.match(lowerExp, chr(int(trASC[intStartCharNum:intEndCharNum])))), '숫자 성공 ::', chr(int(trASC[intStartCharNum:intEndCharNum])))
        intStartCharNum = intEndCharNum
        intEndCharNum = intStartCharNum + 2
    else:
        #print('[실패] intStartCharNum:',intStartCharNum,',intEndCharNum:',intEndCharNum)
        intStartCharNum = intStartCharNum
        intEndCharNum = intEndCharNum +1
        if(intEndCharNum-intStartCharNum > 4):
            intEndCharNum = intStartCharNum+3
    ulen = ulen + 1
    if(intEndCharNum == len(trASC)):
        break
print ('-------------------------------------------------------');

# 도메인을 카운트하고 전체 몇건인지 확인해보자







#가장 높은 알파벳
#가장 낮은 알파벳

# inputArr[i][j]
#tmp_pattern  = ['']*len(inputArr[i]) #초기화 # ★ 동적으로 배열 할당하고 쓰는 방법 알아보기
tmp_pattern = [''] * len(inputArr)  # 초기화 # ★ 동적으로 배열 할당하고 쓰는 방법 알아보기
#print('==>', len(tmp_pattern), ', ', tmp_pattern)

# 새로운 문자열들로 바꿀 tmp
newInputArr = ['']*len(inputArr)

# 각 알파벳으로 바꾸어서 새로운 tmpArr에 넣어주기 ====================
while (i < len(inputArr)):
    while (j < len(inputArr[i])):
        # ============================================================ 소문자
        if (bool(re.match(lowerExp, inputArr[i][j]))):
            newInputArr[i] = newInputArr[i] + 'a'

        # ============================================================ 대문자
        elif (bool(re.match(upperExp, inputArr[i][j]))):
            newInputArr[i] = newInputArr[i] + 'A'

        # ============================================================ 숫자
        elif (bool(re.match(numExp, inputArr[i][j]))):
            newInputArr[i] = newInputArr[i] + '0'

        # ============================================================ 특수문자
        elif (bool(re.match(speExp, inputArr[i][j]))):
            newInputArr[i] = newInputArr[i] + inputArr[i][j]

        j = j+1
        if( j == len(inputArr[i])):
            j = 0
            break
    i = i+1
print('★ 신규 문자열 :::::::::::::::::::::::::::::: 최종',newInputArr, len(newInputArr), len(newInputArr[0]))

# ======================================> 실제
i = 0
repeatStr = ''
while (i < len(newInputArr)):
    #print('\n =====☞ newInputArr[',i,'] 문자열 ',newInputArr[i], '패턴 검색 시작! [',len(newInputArr[i]),'] 자리 ☜=====')
    num = 1
    while (j < len(newInputArr[i])):
        # print ('현재 문자열 :',newInputArr[i][j], (i,j))
        # ============================================================ 소문자
        if (bool(re.match(lowerExp, newInputArr[i][j]))):
            # 현재 문자열과 다음 문자열이 같을 경우,
            if (j < len(newInputArr[i]) - 1 and (newInputArr[i][j] == newInputArr[i][j + 1])):
                num = num + 1 #카운트 수만 늘려줌
                #print('다음에도 소문자네요! :', num)
                #print ('====> (',newInputArr[i][j],') next char :', newInputArr[i][j+1], 'num :', num)
            else:
                tmp_pattern[i] = tmp_pattern[i] + '[a-z]'+repeatExp(num)
                num = 1
                #j = j+1
                #print('최종 :'+tmp_pattern[i])

        # ============================================================ 대문자
        elif (bool(re.match(upperExp, newInputArr[i][j]))):
            if (j < len(newInputArr[i]) - 1 and (newInputArr[i][j] == newInputArr[i][j + 1])):
                num = num + 1 #카운트 수만 늘려줌
                #print('다음에도 대문자네요! :', num)
            else:
                tmp_pattern[i] = tmp_pattern[i] + '[A-Z]'+repeatExp(num)
                num = 1
                #j = j+1
                #print('최종 :' + tmp_pattern[i])

        # ============================================================ 숫자
        elif (bool(re.match(numExp, newInputArr[i][j]))):
            if ( j < len(newInputArr[i])-1 and (newInputArr[i][j] == newInputArr[i][j + 1])):
                num = num + 1 #카운트 수만 늘려줌
               #print('다음에도 숫자네요! :', num)
            else:
                tmp_pattern[i] = tmp_pattern[i] + '[0-9]'+repeatExp(num)
                num = 1
                #j = j+1
                #print('최종 :' + tmp_pattern[i])

        # ============================================================ 특수문자
        elif (bool(re.match(speExp, newInputArr[i][j]))):
            if (j < len(newInputArr[i]) - 1 and (newInputArr[i][j] == newInputArr[i][j + 1])):
                num = num + 1 #카운트 수만 늘려줌
                #print('다음에도 특수문자네요! :', num)
            else:
                tmp_pattern[i] = tmp_pattern[i] + newInputArr[i][j]
                num =1
                #j = j+1
                #print('최종 :' + tmp_pattern[i])

        j = j+1
        if( j == len(newInputArr[i])):
            j = 0
            break
    i = i+1
print('★최종', tmp_pattern)
print ('-------------------------------------------------------');

#결과로 나온 패턴끼리 한번 더 비교해보기
p = 0
while p < len(tmp_pattern):
    print('case',p,'= \''+tmp_pattern[p]+ '\'')
    print('case',p,'_name = \'' + inputArr[p] + '\'')
    # ****정규화된 패턴 뒤에 이메일을 붙여서 보면?
    # 영문으로 시작하고, 숫자로 끝나는구나!
    p = p+1

print ('-------------------------------------------------------');
# 패턴 매치 실행해보기
print ('100001) 정규식 match 확인! input :[',inputArr[0],'] ==☞ result :', bool(re.match(tmp_pattern[0], inputArr[0])))
print ('100001) 정규식 match 확인! input :[',inputArr[1],'] ==☞ result :', bool(re.match(tmp_pattern[1], inputArr[1])))
print ('100001) 정규식 match 확인! input :[',inputArr[2],'] ==☞ result :', bool(re.match(tmp_pattern[2], inputArr[2])))


# numpy를 이용한 3차원 텐서 만들기
tensor_3d = np.array([[1,2], [3,4], [5,6], [7,8]])
print (tensor_3d)

number_of_points = 100
x_point = []
y_point = []

a = 0.22
b = 0.78
for l in range(number_of_points):
    x = np.random.normal(0.0, 0.5)
    y = a*x +b+np.random.normal(0.0, 0.1)
    x_point.append([x])
    y_point.append([y])

plt.plot(x_point, y_point, '0', label='Input data')
plt.legend()
plt.show()


#학습결과 hdf5 파일로 결과 남기기
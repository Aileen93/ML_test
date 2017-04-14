def diff_commonPrefix(text1, text2):
    # Quick check for common null cases.
    if not text1 or not text2 or text1[0] != text2[0]:
        return 0
        # Binary search.
    pointermin = 0
    pointermax = min(len(text1), len(text2))
    pointermid = pointermax
    pointerstart = 0
    while pointermin < pointermid:
        if text1[pointerstart:pointermid] == text2[pointerstart:pointermid]:
            pointermin = pointermid
            pointerstart = pointermin
        else:
            pointermax = pointermid
        pointermid = int((pointermax - pointermin) / 2 + pointermin)
    return pointermid


def diff_commonSuffix(text1, text2):
    # Quick check for common null cases.
    if not text1 or not text2 or text1[-1] != text2[-1]:
        return 0
        # Binary search.
    pointermin = 0
    pointermax = min(len(text1), len(text2))
    pointermid = pointermax
    pointerend = 0
    while pointermin < pointermid:
        if (text1[-pointermid:len(text1) - pointerend] ==
                text2[-pointermid:len(text2) - pointerend]):
            pointermin = pointermid
            pointerend = pointermin
        else:
            pointermax = pointermid
        pointermid = int((pointermax - pointermin) / 2 + pointermin)
    return pointermid

def edit_distance(s1, s2):
    l1, l2 = len(s1), len(s2)
    if l2 > l1:
        return edit_distance(s2, s1)
    if l2 is 0:
        return l1
    prev_row = list(range(l2 + 1))
    current_row = [0] * (l2 + 1)
    for i, c1 in enumerate(s1):
        current_row[0] = i + 1
        for j, c2 in enumerate(s2):
            d_ins = current_row[j] + 1
            d_del = prev_row[j + 1] + 1
            d_sub = prev_row[j] + (1 if c1 != c2 else 0)
            current_row[j + 1] = min(d_ins, d_del, d_sub)
        prev_row[:] = current_row[:]
    return prev_row[-1]

case0 = '[a-z]{3}[0-9]{4}@[a-z]{4}.[a-z]{3}'
case0_name = 'mjk2072@'
case1 = '[a-z]{1}[0-9]{3}[a-z]{3}@[a-z]{7}.[a-z]{2}'
case1_name = 'o377jja'
case2 = '[a-z]{3}[0-9]{1}[a-z]{1}[0-9]{2}@[a-z]{7}.[a-z]{2}'
case2_name = 'bdi3p77'
case3 = '[a-z]{7}[0-9]{5}@[a-z]{5}.[a-z]{3}'
case3_name = 'mzseobi12344'
case4 = '[a-z]{1}[0-9]{5}[a-z]{1}@[a-z]{7}.[a-z]{2}'
case4_name = 'y12655u'
case5 = '[a-z]{12}@[a-z]{4}.[a-z]{3}'
case5_name = 'designweaver' #현수매니저님

print('abc 와 abc (정규식을)를 비교하면? :',edit_distance('abc', 'abc'))
print(case0,'(',case0_name,')와 ',case1,'(',case1_name,') 를 비교하면? :',edit_distance(case0, case1))
print(case0,'(',case0_name,')와 ',case2,'(',case2_name,') 를 비교하면? :',edit_distance(case0, case2))
print(case0,'(',case0_name,')와 ',case3,'(',case3_name,') 를 비교하면? :',edit_distance(case0, case3))
print(case0,'(',case0_name,')와 ',case4,'(',case4_name,') 를 비교하면? :',edit_distance(case0, case4))
print(case0,'(',case0_name,')와 ',case4,'(',case5_name,') 를 비교하면? :',edit_distance(case0, case5))

print('아이디를 비교하면?')
print(case0_name,'과 ',case1_name,'을 비교하면?',edit_distance(case0_name, case1_name)) # 12+15 = 27
print(case0_name,'과 ',case2_name,'을 비교하면?',edit_distance(case0_name, case2_name)) # 19+14 = 31
print(case0_name,'과 ',case3_name,'을 비교하면?',edit_distance(case0_name, case3_name)) # 12+3 = 15
print(case0_name,'과 ',case4_name,'을 비교하면?',edit_distance(case0_name, case4_name)) # 12+15 = 27
print(case0_name,'과 ',case5_name,'을 비교하면?',edit_distance(case0_name, case5_name)) # 9+13 = 21
print("================================================================================================")

print('==>',case2_name,'과 ',case3_name,'을 비교하면?',edit_distance(case2_name, case3_name))
print('==>',case2_name,'과 ',case4_name,'을 비교하면?',edit_distance(case2_name, case4_name))
print('==>',case5_name,'과 ',case4_name,'을 비교하면?',edit_distance(case5_name, case4_name))


# 새로운 값에 대한 해석 학습결과(hdf5)를 기준으로 새로운 input에 대한 의심
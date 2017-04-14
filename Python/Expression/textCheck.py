#!/usr/bin/python
# -*- coding: cp949 -*-

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

print (isNumber("123"));
# 출력 결과: True
print (isNumber("123.0"));
# 출력 결과: True
print (isNumber("+.5"));
# 출력 결과: True
print (isNumber(123));
# 출력 결과: True
print (isNumber("123ZZZ"));
# 출력 결과: False
print (isNumber("0xFF"));
# 출력 결과: False         # 16진수 문자열은 인식 못함. 다만, 16진수 숫자는 됨
print (isNumber(''));        # 빈 문자열
# 출력 결과: False
print (isNumber('     '));   # 공백 문자
# 출력 결과: False
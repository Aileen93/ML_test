#!/usr/bin/python
# -*- coding: cp949 -*-

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

print (isNumber("123"));
# ��� ���: True
print (isNumber("123.0"));
# ��� ���: True
print (isNumber("+.5"));
# ��� ���: True
print (isNumber(123));
# ��� ���: True
print (isNumber("123ZZZ"));
# ��� ���: False
print (isNumber("0xFF"));
# ��� ���: False         # 16���� ���ڿ��� �ν� ����. �ٸ�, 16���� ���ڴ� ��
print (isNumber(''));        # �� ���ڿ�
# ��� ���: False
print (isNumber('     '));   # ���� ����
# ��� ���: False
# 测试python中传入参数的可变性
from os import *
str1='hello'
n=0
list1=['a','b']
def test1(n):
	n='world'
def test2(n):
	n=100
def test3(n):
	n[1]='hello'
test1(str1)
# 不变
test2(n)
# 不变
test3(list1)
# 改变
print(str1)
print(n)
print(list1)
system('pause')
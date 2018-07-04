from os import *
from copy import *
# 列表的组合
list1=['a','b','c',65,64]
list2=list1[0:3]
list3=[list1,list2]
list4=[list3,list1]
# 列表取值
print(list1[2])
print(list1[0:3])
print(list1[-1])
print(list2)
print(list3)
print(list4)
print(list4[0][1])
#列表操作
list1.append('hello')
print(list1)
del list1[0]
print(list1)
print(list1+list2)
print(list1*2)
# map
map1={
    'a':36,
    'b':21,
    'c':'hello',
    'name':'xiaoming'
}
print(map1['name'])
# 元组
fib1=(1,2,'fib')
try:
    fib1[0]='test'
except Exception:
    print('e')
print(fib1[2])
# 字符串
str1='abcdefg'
print(str1[0])
print('a' in str1)
print('3' not in str1)
c,b,a=str1[0:3]
print(a,b,c)
# tuple() list()实现列表字符串元组转换
print(list(str1))
print(tuple(list1))
#copy and deepcopy
list5=copy(list3)
list6=deepcopy(list3)
print(list5)
print(list6)
list3[0][1]='copy'
print(list5)
print(list6)
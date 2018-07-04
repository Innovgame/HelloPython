from random import *
from os import *
# while 实现求和
def whileSum(n):
    i=0
    theSum=0
    while i<=n :
        theSum+=i        
        i+=1
    return theSum
# for实现求和
def forSum(n):
    theSum=0
    for i in range(0,n+1,1):
        theSum+=i
    return theSum
# 猜数字
def guesswhat():
    num=randint(0,100)
    print('please input a number 1-100')   
    while True :
        try:
            n=int(input())
        except:
            print('please input int')
            continue
        if num==n :
            print('well down,you are right')
            break
        elif n<num :
            print('too small')
        elif n>num :
            print('too big')       
print(whileSum(100))
print(forSum(100))
guesswhat()
system('pause')

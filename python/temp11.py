# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

def guest():
    presetnum = 3
    active = True
    while active:#设置一个标志，交通信号灯。
        player = input("请输入一个0-9的整数： ")
        player = int(player)
        if player > presetnum:
            print("太高，请重新输入 ")
        elif  player < presetnum:
            print("太低，请重新输入")
        else:
            print("你猜对了")
            break
guest()

def buysth():
    sin,money=input('请输入第一种水笔的包装和价格（逗号隔开）：\n').split(',')
    sin2,money2=input('请输入第二种水笔的包装和价格（逗号隔开）：\n').split(',')
    sing=int(money)/int(sin)
    sing2=int(money2)/int(sin2)
    listL=[]
    listL.append(sing)
    listL.append(sing2)
    L=sorted(listL)
    print(L)
buysth()

def is_order():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def _primes():
    yield 2
    it=is_order()
    while True:
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)
listL=[]
x=0
for n in _primes():
    if n<1000:
        listL.append(n)
        x+=n
    else:
        break
print(listL)
print('素数之和为'+str(x))

def countdate():
    hour, minute, second = input('请输入一个时间( h:m:s): \n').split(':')
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    second = second + 30
    if second >= 60:
        second = second - 60
        minute = minute + 1
    minute = minute + 5
    if minute >= 60:
        minute = minute - 60
        hour = hour + 1
    if hour == 24:
        hour = 0
    print('经过5分30秒后：')
    print('%d:%d:%d' % (hour, minute, second))
countdate()
    

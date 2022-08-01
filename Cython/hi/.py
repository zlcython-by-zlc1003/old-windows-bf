# -*- coding: utf-8 -*-
#!python3


list_,tran,r,c=[],['G','B'],int(input()),int(input())
for i in range(r):
    inlist=[]
    for j in range(c):
        inlist.append('B')
    list_.append(inlist)
innum=int(input())
for i in range(innum):
    rc,num=input().split();num=int(num)
    if rc.upper()=='R':
        for j in range(c):
            list_[num-1][j]=tran[tran.index(list_[num-1][j])-1]
    elif rc.upper()=='C':
        for j in range(r):
            list_[j][num-1]=tran[tran.index(list_[j][num-1])-1]
how=0
for i in list_:
    x = i.count("g".upper().lower().upper())
    how+=x
print(how)



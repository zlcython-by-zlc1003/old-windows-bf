# -*- coding: utf-8 -*-
#!python3


user=input().upper()
def lms(userin):
    l,m,s=0,0,0
    for i in userin:
        if i.upper()=='L':
            l+=1
            continue
        elif i.upper()=='M':
            m+=1
            continue
        elif i.upper()=='S':
            s+=1
            continue
    return (('L' * l)+('M' * m)+('S' * s))
# original : LLSLM
# desired : LLLMS
# missL=1
# missM=1
# m_in_l=0
# l_in_m=1
missL=0
missM=0
m_in_l=0
l_in_m=0
#Answer = missL+missM-min(m_in_l,l_in_m)=1+1-0=2
# original : user
# desired : lms(original)
desired=lms(user)
for i in range(len(user)):
    if user[i]==desired[i]: continue
    elif user[i]!=desired[i] and (user[i]=='M' and desired[i] == 'L'):
        missL+=1
        m_in_l+=1
    elif user[i]!=desired[i] and (user[i]=='L' and desired[i] == 'M'):
        missM+=1
        l_in_m+=1
    elif user[i]!=desired[i] and (user[i]=='S' and desired[i] == 'M'):
        missM+=1
    elif user[i]!=desired[i] and (user[i]=='S' and desired[i] == 'L'):
        missL+=1
print(missL+missM-min(m_in_l,l_in_m))



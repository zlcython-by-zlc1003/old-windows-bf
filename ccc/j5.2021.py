r,c,list_,haw=int(input()),int(input()),[],0
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
            if list_[num-1][j]=='B':
                list_[num-1][j]='G'
            elif list_[num-1][j]=='G':
                list_[num-1][j]='B'
    elif rc.upper()=='C':
        for j in range(r):
            if list_[j][num-1]=='B':
                list_[j][num-1]='G'
            elif list_[j][num-1]=='G':
                list_[j][num-1]='B'
for i in list_:
    for j in i:
        if j=='g'.upper():
            haw+=1
print(haw)
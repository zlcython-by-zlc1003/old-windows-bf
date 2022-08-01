a=int(input())
b=int(input())
s=0
t=0
for i in range(a,b+1):
    if i%2==1:
        print(i)
        s+=i
        t+=1
print('average:'+str(s//t))
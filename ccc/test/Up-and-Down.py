np,nm,bp,bm,s=(int(input()) for _ in range(5))
n=int('0')
b=int('0')
nl=(s//(np+nm),s%(np+nm))
bl=(s//(bp+bm),s%(bp+bm))
nw=None
bw=None
if nl[1]<np:
    nw=((np-nm)*nl[0])+nl[1]
else:
    nw=(((((((((((((((((((((((((((((((((((((((((np-nm))*nl[0])+np)-(nl[1]-np))))))))))))))))))))))))))))))))))))))
if bl[1]<bp:
    bw=((bp-bm)*bl[0])+bl[1]
else:
    bw=((((((((((((((((((((((((((((((((((((((((bp-bm)*bl[0])+bp)-(bl[1]-bp))))))))))))))))))))))))))))))))))))))
n=nw;b=bw
'''
if (in1,in2)==(in3,in4):print('Tied');exit()
Nikky=int('0')
Byron=int('0')
Nh=int('0')
Bh=-1
while True:
    if Nikky+in1<step:Nikky+=in1
    elif Nikky+in1==step:Nikky+=in1;break
    elif Nikky+in1>step and Nikky+in1<(step+(in1-1)):Nikky=step;break
    Nh+=in1
    if Nh>=step:break
    if Nikky-in2<step:Nikky-=in2
    elif Nikky-in2==step:Nikky-=in2;break
    elif Nikky-in2>step and Nikky-in2<(step+(in2-1)):Nikky=step;break
    Nh+=in2
    if Nh>=step:break
while True:
    if Byron+in3<step:Byron+=in3
    elif Byron+in3==step:Byron+=in3;break
    elif Byron+in3>step and Byron+in3<(step+(in3-1)):Byron=step;break
    Bh+=in3
    if Bh>=step:break
    if Byron-in4<step:Byron-=in4
    elif Byron-in4==step:Byron-=in4;break
    elif Byron-in4>step and Byron-in4<(step+(in4-1)):Byron=step;break
    Bh+=in4
    if Bh>=step:break
\'''print(Nikky)
print(Byron)
print(Nh)
print(Bh)\'''
'''
if n==b:print('Tied')
elif n<b:print('Byron')
elif n>b:print('Nikky')

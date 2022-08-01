# 中级 结课展示
print('calculator:')
list=[]
input=input('equation:')
if '+' in input:
    list=input.split('+')
    list.append('+')
elif '-' in input:
    list=input.split('-')
    list.append('-')
elif '*' in input:
    list=input.split('*')
    list.append('*')
elif '/' in input:
    list=input.split('/')
    list.append('/')
else:
    print('error')
    exit()
num1=int(list[0])
num2=int(list[1])
pmtd=list[2]
if pmtd=='+':
    print('%d+%d=%d'%(num1,num2,num1+num2))
elif pmtd=='-':
    print('%d-%d=%d'%(num1,num2,num1-num2))
elif pmtd=='*':
    print('%d*%d=%d'%(num1,num2,num1*num2))
elif pmtd=='/':
    if num2==0:
        print('you can not divide by zero')
    elif num1%num2==0:
        print('%d/%d=%d'%(num1,num2,num1/num2))
    else:
        print('%d/%d=%d r %d'%(num1,num2,num1//num2,num1%num2))
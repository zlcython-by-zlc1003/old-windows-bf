# 初级 结课展示
print('calculator:')
num1=int(input('first number:'))
pmtd=input('operator:')
num2=int(input('second number:'))
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
        print('%d/%d=%dr%d'%(num1,num2,num1//num2,num1%num2))
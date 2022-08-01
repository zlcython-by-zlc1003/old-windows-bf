checknumlist,least=[],''
while True:
    input_=input()
    if int(input_) == 99999:
        break
    checknumlist.append(input_)


for i in checknumlist:
    text=i[1+1:]# 12345 -> 345
    num1=int(i[0])# 12345 -> 1
    num2=int(i[1])# 12345 -> 2
    if num1 == 0 and num2 == 0:
        print(f'{least} {text}')
        continue
    son12=num1+num2
    if son12%2==0:# even
        least='right'
        print(f'{least} {text}')
    else:# odd
        least='left'
        print(f'{least} {text}')
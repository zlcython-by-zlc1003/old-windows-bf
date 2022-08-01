image=['*x*x','* xx','*  *']
times,out=int(input()),''
for i in image:
    for j in i:out+=(j*times)
    out+='\n'
outcopy=out[:];out=''
for i in outcopy.split('\n'):out+=(i+'\n')*times
outcopy=out[:];out=''
for i in outcopy.split('\n'):
    if i != '':out+=(i+'\n')
print(out,end='')
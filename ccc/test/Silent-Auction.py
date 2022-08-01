input1,namelist,msn,msnum = int(input()),[],'',0
for i in range(input1):
    namelist.append((input(),int(input())))
for i in namelist:
    if i[1]>msnum:
        msnum=i[1]
        msn=i[0]
print(msn)
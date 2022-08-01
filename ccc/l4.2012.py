K,pwd,out,letter=int(input()),input().upper(),'','abcdefghijklmnopqrstuvwxyz'.upper()
for P in range(len(pwd)):S = 3*(P+1) + K;out += letter[(letter.index(pwd[P])-S)%26]
print(out)
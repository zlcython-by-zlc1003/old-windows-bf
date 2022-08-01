import json,zlcytopy
with open('liblist.json', 'r', encoding='utf-8') as f:
    libusedict = json.load(f)
zlcython='''Zlcython 2.2.0 (tags/v2.2.0)
Type ".exit" or press Control+C to exit.
Copyright (c) 2022, LucasZ228.
All rights reserved.'''
allfuncandclass=''
print(zlcython)
exit_=False
while True:
    try:
        while True:
            incode=input('>>>')
            if incode=='.exit':raise SystemExit
            if incode=='':continue
            else:
                code,libusedict,_=zlcytopy.zlcytopy(incode,1,libusedict)
                if code.split()!=[]:
                    if code.split()[0]=='def' or code.split()[0]=='class':allfuncandclass+=(code+'\n')
                print('result:'+code,end='')
                print('runing...')
                runcode= (allfuncandclass+'\n'+code) if code != '' else 'print("",end="")'
                exec(runcode)
    except KeyboardInterrupt or SystemExit:
        print('\nexit')
        exit_=True
    except Exception as e:
        print('error.')
        print(e)
    if exit_:break
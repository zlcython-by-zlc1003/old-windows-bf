# pip install opencc-python-reimplemented
import sys,zlcytopy,json
import opencc
cc = opencc.OpenCC('t2s')
codefile = sys.argv[1]
encodefile = sys.argv[2]
decodecode = ''
code = []
with open('liblist.json', 'r', encoding='utf-8') as f:
    libusedict = json.load(f)
with open(codefile, encoding="utf-8") as f:
    _code = f.readlines()
    for i in _code:
        code.append(cc.convert(i))
for linenum in range(len(code)):
    jghfkaghdbjv,libusedict,out__,exit__=zlcytopy.zlcytopy(code[linenum],linenum,libusedict)
    if exit__:exit()
    print(out__)
    decodecode+=jghfkaghdbjv
with open(encodefile, mode="w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("#!python3"+"\n"*3)
    for lib, info in libusedict.items():
        if info[0]:
            f.write(info[1]+'\n')
    f.write(decodecode)
    f.write("\n"*2)
print("编译完成！\n输出文件："+encodefile)
print('\n退出。code：0')
import zlcytopy,json,opencc,coderun

def runcode(codes):
    decodecode=''
    for code in codes:
        with open('liblist.json', 'r', encoding='utf-8') as f:
            libusedict = json.load(f)
        for lib, info in libusedict.items():
            if info[0]:
                code = info[1]+'\n'+code
        code = opencc.OpenCC('t2s').convert(code)
        linenum = 0
        jghfkaghdbjv,libusedict,out__,exit__=zlcytopy.zlcytopy(code,linenum,libusedict)
        if exit__:return '<err_exit.err>'
        decodecode+=jghfkaghdbjv+'\n'
    return decodecode
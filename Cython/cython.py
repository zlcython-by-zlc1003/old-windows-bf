import functools

class blclass:
    def __init__(self,  In, func):
        self.In = In
        self.func = func
    def __call__(self):
        for i in self.In:
            self.func(i)
def 遍历列表(In):
    return functools.partial(blclass, In)

class ifclass:
    def __init__(self,  In, func):
        self.In = In
        self.func = func
    def __call__(self):
        if self.In:self.func()
def 如果(In):
    return functools.partial(ifclass, In)

def 等于(a,b):return a==b
def 大于(a,b):return a>b
def 小于(a,b):return a<b
def 大于等于(a,b):return a>=b
def 小于等于(a,b):return a<=b
def 或(a,b):return a or b
def 和(a,b):return a and b
def 输出(a,**kw):print(a,**kw)
def 非(a):return not a
def 不(a):return not a
def 排序列表(a):return sorted(a)
def 列表长度(a):return len(a)

def 等于(a,b):return a==b
def 大于(a,b):return a>b
def 小于(a,b):return a<b
def 大于等于(a,b):return a>=b
def 小于等于(a,b):return a<=b
def 或(a,b):return a or b
def 和(a,b):return a and b
def 输出(a,**kw):print(a,**kw)
def 非(a):return not a
def 排序列表(a):return sorted(a)
def 列表长度(a):return len(a)
输入一,输入二,事情列表,可在时间内执行的事=int(input()),int(input()),[],0
for i in range(输入二):事情列表.append(int(input()))
排序后列表=排序列表(事情列表)
for i in range(列表长度(排序后列表)):
    if 小于等于(sum(排序后列表[0:i]),输入一):可在时间内执行的事=i
    else:break
print(可在时间内执行的事)
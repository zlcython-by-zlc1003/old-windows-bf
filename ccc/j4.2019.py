列表=[1,2,3,4]

输入=input()

def 等于(a,b):return a==b
def 大于(a,b):return a>b
def 小于(a,b):return a<b
def 大于等于(a,b):return a>=b
def 小于等于(a,b):return a<=b
def 或(a,b):return a or b
def 和(a,b):return a and b
def 输出(a,**kw):print(a,**kw)
def 非(a):return not a

def 左右移动列表(列表):return [列表[1],列表[0],列表[3],列表[2]]
def 上下移动列表(列表):return [列表[2],列表[3],列表[0],列表[1]]

for i in 输入:
    if 等于(i,'H'):
        列表=上下移动列表(列表)
    elif 等于(i,'V'):
        列表=左右移动列表(列表)

out=f'{列表[0]} {列表[1]}\n{列表[2]} {列表[3]}'
输出(out)
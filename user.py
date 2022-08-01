import urllib.request as us, json,tkinter,threading,time,tkinter.messagebox,urllib.error as uerr
class TkGuiApp(object):# class _main
    def __init__(self,errorl=0,l=1,debugmode=False) -> None:# class _main
        import tkinter as tk# import random,sys,tkinter as tk
        from tkinter import simpledialog# from tkinter import simpledialog
        from tkinter import messagebox# from tkinter import messagebox
        self.tk=tk
        self.messagebox=messagebox
        self.simpledialog=simpledialog
    def init(self):
        self.root=self.tk.Tk()
        self.root.withdraw()
    def inputbox(self,text):
        return self.simpledialog.askstring('quiz', text)# askstring quiz text
    def mbox(self,text):# mbox
        self.messagebox.showinfo('message', text)
    def warning(self,text):
        self.messagebox.showwarning('warning', text)
    def error(self,text):
        self.messagebox.showerror('error', text)
    def question(self,text):
        return self.messagebox.askquestion('question', text)
    def questionyesno(self,text):
        return self.messagebox.askyesno('question', text)
    def questionyesnocancel(self,text):
        return self.messagebox.askyesnocancel('question', text)
    def questionokcancel(self,text):
        return self.messagebox.askokcancel('question', text)
    def questionretrycancel(self,text):
        return self.messagebox.askretrycancel('question', text)
app=TkGuiApp()
app.init()
input_ = app.inputbox('请输入服务器地址')
if input_ == None or input_ == '':
    app.warning('exit')
    exit(0)
try:
    iszx=json.loads(str(us.urlopen(input_+'/cs/').read().decode('utf-8')))[0]
    if iszx != 'imhere':
        raise ValueError
except ValueError or TimeoutError or uerr.URLError:
    app.error('url错误')
    exit(0)
SERVER_URL = input_
ENCDE_C= us.quote('搞到some_no_all用户哈哈哈进入噶*^_^*')
null=None
listbox,bf=null,null
# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
def fin(a):
    return [f'{a[1]}: {a[0]}',a[2]]

def recv():
    global listbox,bf
    while True:
        data=json.loads(str(us.urlopen(SERVER_URL).read().decode('utf-8')))
        encode_data=list(map(fin,data))
        encode_data=encode_data[::1]
        if bf!=encode_data:
            if listbox != None :listbox.delete(0, tkinter.END)
            for i in range(1,len(encode_data)):
                listbox.insert(i,encode_data[0][i-1])
                # listbox.itemconfig(i,{'bg':'OrangeRed3'})
        bf=encode_data
    
def Creat():
    global name,rE1,listbox
    t=tkinter.Tk()
    t.title("多人聊天室")
    t.geometry("300x200+500+200")
    name=us.quote(name if name!= '' or name != None else 'empty')
    non_utf8_name=name if name!= '' or name != None else 'empty'
    tr = threading.Thread(target=recv,daemon=True)
    # daemon=True 表示创建的子线程守护主线程，主线程退出子线程直接销毁
    tr.start()
    t.title("聊天室")
    t.geometry("500x600")
    rL0 = tkinter.Label(t,text='%s的聊天室'%non_utf8_name,width=40)
    rL0.pack()
    rL1 = tkinter.Label(t,text='请输入消息：',width=20, height=1)
    rL1.place(x=0,y=450)
    rE1 = tkinter.Entry(t)
    rE1.place(x=200,y=450) 
    rB1 = tkinter.Button(t, text="发送",command=left)
    rB1.place(x=380,y=450)
    listbox=tkinter.Listbox(t,width=40,height=20)
    listbox.pack()
    t.mainloop()
def left():
    global rE1
    key=us.quote(rE1.get() if rE1.get() else 'empty')
    us.urlopen(SERVER_URL+'/add/%s/%s/%s'%(key,name,userid))
    # 清除输入框
    rE1.delete(0,tkinter.END)
def JieShu():
    tkinter.messagebox.showwarning(title='你确定退出吗？', message='刚才你点击了关闭按钮')
    us.urlopen(SERVER_URL+'/_del_/_user_/%s'% userid)
    exit(0)   
# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
userdata=json.loads(str(us.urlopen(SERVER_URL+f'/{ENCDE_C}/').read().decode('utf-8')))
name=app.inputbox('请输入你的名字')
while name in userdata:
    app.warning('你的名字和其他人的名字重复了')
    name=app.inputbox('请输入你的名字')
userid=json.loads(str(us.urlopen(SERVER_URL+'/a_d_d_u_s_e_r/'+name).read().decode('utf-8')))[0]
Creat()
# XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX
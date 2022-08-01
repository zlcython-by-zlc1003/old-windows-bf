from __future__ import print_function
import tkinter, random,time
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
    def askyesno(self,text):
        return self.messagebox.askyesno('question', text)
app=TkGuiApp();app.init()
wordlist=['drive','alert','index','fault','width','input','print','while','light','break','clear','ADIEU','TARES','SOARE','DUCAT','OUIJA','CAROM','ERGOT','CRAIC','SQUAB','ENOKI','AZURE']
for i in range(len(wordlist)):
    wordlist[i]=wordlist[i].upper()
colortime=0
ringtword=random.choice(wordlist)
wordlewindow=tkinter.Tk()
wordlewindow.title('Wordle')
wordlewindow.geometry('700x700')
wordlewindow.configure(background='white')
wordlewindow.resizable(0,0)
canvas=tkinter.Canvas(wordlewindow,width=275,height=30,bg='white',highlightthickness=0)
canvas.grid(row=0,column=0)
wordinputlist=[]
def setTextInput(en,text):
    en.delete(0,"end")
    en.insert(0, text)
def _number_check(_):
    wordinputlist_=wordinputlist[0]
    data = wordinputlist_.get().strip()
    if len(data) <= 5: return
    setTextInput(wordinputlist_, data[:5])
def addwordinputbox():
    global wordinputlist
    wordinputlist.append(tkinter.Entry(wordlewindow,width=5,font=('Arial',30),state='disable',highlightthickness=0))
    wordinputlist[-1].grid(row=len(wordinputlist),column=1)
    wordinputlist[-1].bind('<KeyRelease>', _number_check)
    return wordinputlist[-1]
def check(rightword,word) -> list:
    if rightword==word:
        return ['green','green','green','green','green']
    else:
        out=[]
        for i in range(len(word)):
            if word[i]==rightword[i]:
                out.append('green')
            elif word[i] in rightword:
                out.append('yellow2')
            else:
                out.append('gray')
        return out
def coloring(inputclass:tkinter.Entry,row:int,index:int=0):
    global colortime
    iswin=(ringtword==inputclass.get())
    word=inputclass.get()
    word=word.upper()
    if len(word)!=5 or (word not in wordlist):
        inputclass.config(bg='red')
        wordlewindow.update()
        time.sleep(0.5)
        wordlewindow.update()
        inputclass.config(bg='white')
        wordlewindow.update()
        return
    if iswin:
        color=['green','green','green','green','green']
    else:
        color=check(ringtword,word)
    colortime+=1
    inputclass.destroy()
    wordcanvas=tkinter.Canvas(wordlewindow,width=150,height=30,bg='white',highlightthickness=0)
    wordcanvas.grid(row=row,column=1)
    for i in range(len(word)):
        label=tkinter.Label(wordcanvas,text=word[i].upper(),font=('Arial',30),fg=color[i],bg='white',highlightthickness=0)
        label.grid(row=0,column=i)
    if color==['green','green','green','green','green']:
        wordlewindow.update()
        time.sleep(2)
        app.mbox('You win!')
        exit()
    if len(wordinputlist)!=1:
        del wordinputlist[index]
        wordinputlist[index].config(state='normal')
        wordinputlist[index].focus()
    else:app.mbox('game over\nthe ringt word is '+ringtword.lower());exit()
def exitfunc():
    if app.askyesno('Are you sure to exit?'):exit()
for i in [1,2,3,4,5]:
    inputbox1=addwordinputbox()
# canvas=tkinter.Canvas(wordlewindow,width=275,height=700,bg='white')
# canvas.grid(row=0,column=2)
wordinputlist[0].focus()
wordinputlist[0].config(state ='normal')
btn=tkinter.Button(wordlewindow,text='run',command=lambda:coloring(wordinputlist[0],colortime,0))
btn.grid(row=5,column=0)
wordlewindow.protocol("WM_DELETE_WINDOW", exitfunc)
wordlewindow.mainloop()
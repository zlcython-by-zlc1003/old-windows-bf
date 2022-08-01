# import tkinter
# win = tkinter.Tk()
# win.attributes('-alpha',1)
# win.title("Kahn Software v1")    # #窗口标题
# win.geometry("500x300+0+0")   # #窗口位置500后面是字母
# menubar = tkinter.Menu(win, tearoff=False)    # #创建菜单条
# xMenu = tkinter.Menu(menubar, tearoff=False)      # #创建子菜单
# for item in ["√", "×", "子菜单3", "子菜单4", "子菜单5"]:
#     xMenu.add_command(label=item)
# menubar.add_cascade(label="右键总菜单1", menu=xMenu)      # #创建总菜单，将子菜单绑定进来
# def xShowMenu(event):
#     menubar.post(event.x_root, event.y_root)   # #将菜单条绑定上事件，坐标为x和y的root位置
# win.bind("<Button-3>", xShowMenu)     # #设定鼠标右键触发事件，调用xShowMenu方法
# win.mainloop()   # #窗口持久化
import tkinter as tk,random
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("hello")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_527=tk.Button(root)
        GButton_527["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_527["font"] = ft
        GButton_527["fg"] = "#000000"
        GButton_527["justify"] = "center"
        GButton_527["text"] = "hello"
        GButton_527.place(x=280,y=240,width=70,height=25)
        def func__():GMessage_636['text']=[random.choice('qwertyuiopasdfghjklmnbvcxz1234567890-=[]\';./,!@#$%^&*()_+{}|":<>?QWERTYUIOPLKJHGFDSAZXCVBNM') for i in range(10)]
        GButton_527["command"] = func__

        GMessage_636=tk.Message(root)
        GMessage_636["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_636["font"] = ft
        GMessage_636["fg"] = "#333333"
        GMessage_636["justify"] = "center"
        GMessage_636["text"] = "123"
        GMessage_636.place(x=10,y=10,width=200,height=200)

        GCheckBox_838=tk.Checkbutton(root)
        GCheckBox_838["cursor"] = "trek"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_838["font"] = ft
        GCheckBox_838["fg"] = "#333333"
        GCheckBox_838["justify"] = "center"
        GCheckBox_838["text"] = "CheckBox"
        GCheckBox_838.place(x=400,y=140,width=70,height=25)
        GCheckBox_838["offvalue"] = "0"
        GCheckBox_838["onvalue"] = "1"
        GCheckBox_838["command"] = self.GCheckBox_838_command


    def GCheckBox_838_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

import json,random
import re
from flask import Flask
mesages = []
users = []
app = Flask(__name__)
def rid():
    ranid=''
    for i in range(10):
        ranid+=random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnm_+{|}":<>?!@#$%^&*()~`-=][\\\';/.,'))
    return ranid
@app.route('/')
def index():
    return json.dumps(mesages)

@app.route('/add/<string:message>/<name>/<userid>')
def add(message,name,userid):
    # 黑底白字
    return__=[]
    for i in users:
        return__.append(i[1])
    if userid not in return__:
        return '{"code":-1,"message":"error_user_id"}'
    print(name,' ',userid,':',message)
    mesages.append([message,name,userid])
    return '{"code":200,"message":"success"}'

@app.route('/del/all')
def del_all():
    mesages=[]
    print('清空聊天记录')
    return '{"code":200,"message":"success"}'

@app.route('/a_d_d_u_s_e_r/<name>')
def adduser(name):
    user_data=[name,rid()]
    while user_data in users:
        user_data=[name,rid()]
    users.append(user_data)
    print('adduser:',name)
    return json.dumps([user_data[1]])

@app.route('/_del_/_user_/<userid>')
def del_user(userid):
    if users==[]:return
    for i in range(len(users)):
        if users[i][1]==userid:
            del users[i]
            break
    print('删除用户,id：',userid,'name:',users[i][0])
    return '{"code":200,"message":"success"}'

@app.route('/搞到some_no_all用户哈哈哈进入噶*^_^*/')
def hfga():
    return__=[]
    for i in users:
        return__.append(i[0])
    return json.dumps(return__)

@app.route('/cs/')
def sas():
    return json.dumps(['imhere'])
if __name__ == '__main__':
    # 黑底黑字
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='0.0.0.0',port=5555)
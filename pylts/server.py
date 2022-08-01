import socket
import flask
import os
import threading
import config

ADMINPWD = 'zlcython-is-best'


class Server(object):
    def __init__(self):
        # 在线客户端
        self.online_pool = {}
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server.bind(config.settings['addr_port'])

    # 消息广播方法
    def broadcast(self, msg):
        for i in self.online_pool:
            self.online_pool[i].send(msg.encode('gbk'))

    # 客户端登录方法
    def login(self, client_socket, info):
        print('{} Login'.format(info))
        if len(self.online_pool) >= 1:
            self.broadcast('{} now is online...'.format(info))
        self.online_pool[info] = client_socket
        # 通知新用户当前在线列表
        msg = 'online user:\n'
        for i in self.online_pool:
            msg += (str(i) + '\n')
        print(msg)
        msg = msg.encode('gbk')
        client_socket.send(msg)

    # 客户端登出方法
    def logout(self, info):
        del self.online_pool[info]
        msg = '{} is offline'.format(info)
        self.broadcast(msg)

    # 发送消息方法
    def send_msg(self, info, msg):
        print(msg)
        msg = msg.encode('gbk')
        if info in self.online_pool:
            self.online_pool[info].send(msg)

    # 会话管理方法
    def session(self, client_socket, info):
        # 新用户登录,执行login()
        self.login(client_socket, info)
        while True:
            try:
                data = client_socket.recv(1024).decode('gbk')
                # 如果收到长度为0的数据包,说明客户端 调用了secket.close()
                if len(data) == 0:
                    print('{}客户端断开...'.format(info))
                    # 此时需要调通客户端 登出 方法
                    self.logout(info)
                    break
                else:
                    print(info, ':', data)
                    # 此时服务端接收到正常的消息,广播给其他所有客户端
                    # content = str(info) + ': '
                    # data
                    for i in self.online_pool:
                        if i != info:
                            self.send_msg(i, data)
            except Exception as err:
                print(err)
                # 如果抛出异常,说明客户端强制退出,并没有调用socket.close()
                # 此时需要调通客户端 登出 方法
                self.logout(info)
                break

    def start(self):
        self.server.listen(128)
        while True:
            client_socket, info = self.server.accept()
            thread = threading.Thread(
                target=self.session, args=(client_socket, info))
            thread.setDaemon(True)
            thread.start()


flaskapp = flask.Flask(__name__)


@flaskapp.route('/')
def index():
    return 'pychat.lucasz228.repl.run'


@flaskapp.route('/chatadmin/<pwd>/<msg>')
def adminsend(pwd, msg):
    global ADMINPWD, server
    if pwd == ADMINPWD:
        server.broadcast('admin:'+msg)
        return '200 OK', 200
    else:
        return 'wrong password'


@flaskapp.route('/clear/<pwd>/')
def clear(pwd):
    global ADMINPWD, server
    if pwd == ADMINPWD:
        os.system('cls')
        return '200 OK', 200
    else:
        return 'wrong password'


if __name__ == '__main__':
    print('服务器{}已启动!'.format(config.settings['addr_port']))
    server = Server()
    t = threading.Thread(target=server.start)  # , name='LoopThread')
    t.start()
    flaskapp.run(host='0.0.0.0', port=5418, debug=False)

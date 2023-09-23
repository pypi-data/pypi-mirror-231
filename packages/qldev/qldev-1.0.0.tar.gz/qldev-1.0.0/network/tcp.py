import random
import socket
from threading import Thread
from time import sleep

class TCPServer():
    def __init__(self, port, callback=None) :
        self.port = port
        self._callback = callback
        self._run = False
        self._socket = None
        self.clients = {}
        self._start()

    def is_run(self):
        return self._run
    
    def exists(self, devno):
        return not self.get_client(devno)
    
    def listen(self):

        while self._run:
            # 等待新的客户端连接
            client_socket, clientAddr = self._socket.accept()
            self.client_handler(client_socket, clientAddr)

    def client_handler(self, socket, addr):
        print(f"new client socket {addr[0]}:{addr[1]} connected.")


    def _start(self):
        if self.is_run():
            return

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 本地信息
        address = ('', self.port)
        # 绑定
        self._socket.bind(address)

        self._socket.listen(128)

        self._run = True

        lsn = Thread(target=self.listen)
        lsn.start()
    
    def get_client(self, devno = None):   
        if len(self.clients) == 0:
            print("TCP server has no client connection.")
            return None

        if devno:
            return self.clients[devno]
        else:
            # 默认返回一个设备
            key = random.sample(self.clients.keys(), 1)[0]
            return self.clients[key]

        
def client_listen(socket, callback):
    while True:
        try:
            # 接收对方发送过来的数据
            recv_data = socket.recv(1024)  # 接收1024个字节
            if recv_data:
                # print(data)
                print('接收到的数据为:', recv_data.decode('utf-8'))
                callback     
        except:
            print("获取到异常")
            break


class ServerContainer(object):
    def __init__(self) :
        self.servers = {}
        
    def add_listen(self, port):
        if self.exists(port):
            print(f"server[{port}] exists already.")
            return
        tcp_server = TCPServer(port)
        self.servers[port] = tcp_server

        return tcp_server

        
    def exists(self, port):
        if self.servers[port]:
            return True
        return False


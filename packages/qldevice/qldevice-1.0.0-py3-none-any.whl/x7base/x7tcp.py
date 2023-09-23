import hashlib
from threading import Thread
from time import sleep
from typing import Literal, overload
from device.message import X7MessageStream
from network import TCPServer
from .x7parser import *
from .x7utils import *
from .devinfo import *

class X7TCP(TCPServer):
    def __init__(self, port=19128, callback=None):
        super().__init__(port, callback)

    # trigger仅在脑电采集时生效
    # type是trigger的标识-int类型
    def trigger(self, type=0, devno = None):
        # 获取设备
        client = self.get_client(devno)
        if client is None:
            if devno:
                print(f"X7base({devno}) not found")
            return

        else:
            client.trigger(type)

    # id是音频编号，取值范围为[0-9]，表示第1-10个音频位置
    # volumn是音量大小，取值范围[1-10]
    def wav_trigger(self, id, volumn, devno = None):
        # 获取设备
        client = self.get_client(devno)
        if client is None:
            if devno:
                print(f"X7base({devno}) not found")
            return
            
        else:
            client.wav_trigger(id, volumn)
       
    # id是音频编号，取值范围为[0-9]，表示第1-10个音频位置
    # fname是本地音频文件的存储路径  
    def update_wav(self, id, fname, devno = None, buffer=3072):    
        # 获取设备
        client = self.get_client(devno)
        if client is None:
            if devno:
                print(f"X7base({devno}) not found")
            return

        with open(fname, 'rb') as f:
            flen = f.seek(0, 2)
            print(f"file{fname} len is {flen}")
            client.wav_update_ready(id, flen)
            sleep(0.1)

            f.seek(0)
            offset = 0
            buf = f.read(buffer)
            md5 = hashlib.md5()
            while buf:
                blen = len(buf)
                print(f"update(id:{id}, offset:{offset}/{flen}, llen:{blen})")
                client.wav_update(id, offset, blen, buf)
                md5.update(buf)
                # 指令发送间隔，避免数据处理异常
                sleep(0.01)
                offset += blen
                buf = f.read(buffer)
            print(f"file{fname} offset is {offset} md5 is {md5.hexdigest()}")

            client.wav_update_stop(id, md5.hexdigest())
            print(f'file{fname} update finished.')    
        
    # @overload
    def client_handler(self, socket, addr):
        print(f"new client socket {addr[0]}:{addr[1]} connected.")
        ClientHandler(socket, MessageParser(), callback=self._client_changed)        
    
    def _client_changed(self, devno, type: Literal["add", "remove"], client = None):
        print(f'{type} client {devno}')
        if type == 'add' and client:
            self.clients[devno] = client
            global_cache.connected_add(devno)
        else:
            self.clients.pop(devno)
            global_cache.connected_remove(devno)
        print(f"Now has {len(self.clients)} clients.")

class ClientHandler(X7MessageStream):
    def __init__(self, socket, addr = None, parser = None, callback=None) :
        super().__init__()
        self._socket = socket
        self._address = addr
        self._parser = parser
        self._callback = callback
        self._run = True
        self.devid = None
        self.devtype = None
        self.accept()

    def accept(self):        
        # self.ask()
        # recv = Thread(target=client_listen, args=(self._socket, self.ask()))
        recv = Thread(target=self._consumer)
        recv.start()

        # 获取设备信息
        self.get_device_info()

    
    # 处理数据接收
    def _consumer(self):
        if self._parser is None:
            self._parser = MessageParser()

        while self._run:
            try:
                # 接收对方发送过来的数据
                recv_data = self._socket.recv(1024)  # 接收1024个字节
                if recv_data:
                    self._parser.parse(recv_data, self.update_info)
                else:
                    break
            except Exception as e:
                print("ClientHandler._consumer()出现异常：")
                print(e)
                break

        # print(f"客户端{}:{}已关闭")
        self._socket.close()
        print(f"客户端{self._socket}连接已断开")
        if self._callback and self.devid:
            self._callback(self.devid, 'remove')


    def close(self):
        self._run = False

    def get_device_info(self):
        print("Ask the device info...")
        self._send(X7Command.get_device_info())

    def update_info(self, cmd, info):

        # print(f"update_info cmd {hex(cmd)}")

        if cmd == CommandEnum.GET_DEVICE_INFO:
            self.devid = info['dev_id'] if info and 'dev_id' in info.keys() else None
            self.devtype = info['dev_type'] if info and 'dev_type' in info.keys() else None   
            if self._callback and self.devid:
                self._callback(self.devid, 'add', client = self)

        if cmd == CommandEnum.SIGNALS:
            if len(self.channels) > 0:
                for idx, item in enumerate(self.channels.keys()):
                    self.channels[item].put(info)

    def trigger(self, type=0):
        self._send(X7Command.trigger(type))

    def wav_update_ready(self, id, len):
        self._send(X7Command.wav_update_ready(id, len))

    def wav_update(self, id, offset, len, data):
        self._send(X7Command.wav_update(id, offset, len, data))

    def wav_update_stop(self, id, checksum):
        self._send(X7Command.wav_update_stop(id, checksum))

    def wav_trigger(self, id, volumn):
        self._send(X7Command.wav_trigger(id, volumn))

    def _send(self, message):
        try:
            self._socket.send(message)
        except Exception as e:
            print("Tcp client send message...")
            print(e)


            
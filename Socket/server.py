#from asyncio.windows_events import NULL
import socket
import time
import select
# 建立一个服务端
def start_server(port):
    HOST='0.0.0.0'
    POST=port
    n=0
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind((HOST,POST)) #绑定要监听的端口
    except:
        print('PORT was none')
    server.listen(5) #开始监听 表示可以使用五个链接排队
    inputs = [server]
    outputs =[]
    while inputs:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
        try:
            read,write,excep=select.select(inputs,outputs,inputs)
        except ValueError:
            print('there is no true Value')
        for s in read:
            if s is server:
                connection,client_addr=s.accept()
                print('connected by',client_addr)
                inputs.append(connection)
            else:
                try:
                    data=s.recv(1024)
                except:
                    n+=5
                    if s in outputs and n==5:
                        print('recev err')
                        outputs.remove(s)
                    inputs.remove(s)
                    print('recev err close net')
                    s.close()
                    break
                if data:
                    print(data.decode(encoding='utf-8'))
                    if s not in outputs:
                        print("back to client")
                        outputs.append(s)
                else:
                    n+=5
                    if s in outputs and n==5:
                        print('no back to client')
                        outputs.remove(s)
                    inputs.remove(s)
                    print('lose 5 data close net')
                    s.close()
        for w in write:
            connet,addr=w.getpeername()
            print(connet,addr)
            #a,addr=w.accept()
            w.send('server send '.encode(encoding='utf-8'))
            outputs.remove(w)
        for s in excep:
            print('socker prob')
            inputs.remove(s)
            if s in outputs:
                print('send fail')
                outputs.remove(s)
            s.close()
if __name__ == '__main__':
    start_server(8801)

        # conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
        # print(addr)
        # while True:
        #     try:
        #         str=time.asctime(time.localtime(time.time()))
        #         print(str+"  ")
        #         print(addr)
        #         data = conn.recv(1024)  #接收数据
        #         if data:
        #             break
        #         a=socket.getaddrinfo
        #         print('recive:',data.decode()) #打印接收到的数据
        #         conn.send(data.upper()) #然后再发送数据
        #     #except ConnectionResetError as e:
        #     except:
        #         print('关闭了正在占线的链接！')
        #         break
        # conn.close()
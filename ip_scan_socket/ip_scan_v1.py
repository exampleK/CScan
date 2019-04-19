import socket

range = 100 #测试，地址从100开始
iplist = []

# hosts = ['127.0.0.1', '192.168.1.5', '10.0.0.1']

ports = [445, 22, 80, 443, 3389]

# for host in hosts:
while(range<256):
  range+=1
  hosts = ('192.168.1.{}'.format(range))
  for port in ports:
    try:
       s = socket.socket() # 不能放循环外面，否则会报WinError 10038] 在一个非套接字上尝试了一个操作
       s.settimeout(1)# 设置socket超时时间 时间单位sec
       print ("[+] Connecting to "+hosts+":"+str(port))
       s.connect((hosts, port)) # 双(( ip,port)) 
       s.send("test".encode()) # 如果不加encode(),s.recv会接收不到数据
       banner = s.recv(1024)
       if banner:
         print ("[+] Port "+str(port)+" open: "+str(banner))
       s.close()
    except:pass


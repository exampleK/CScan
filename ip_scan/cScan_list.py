import os
import time
range = 0
iplist = []
while(range<256):
    range+=1
    ip = ('1.1.1.{}'.format(range))
    cmd = (' ping -n 1 {}'.format(ip))

    if os.system(cmd) == 0:
        print('successful!')
        iplist.append(ip)
    else:
        print('failed!')

for x in iplist:
    file=open('c:\data2.txt','a+')
    file.write(x+'\n')
    file.close()
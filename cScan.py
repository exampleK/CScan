import os
import time
range = 0
while(range<256):
    range+=1
    ip = ('1.1.1.{}'.format(range))
    cmd = (' ping -n 1 {}'.format(ip))

    if os.system(cmd) == 0:
        print('successful!')
        txt=open('c:\data.txt','a+')
        txt.write(ip +'\n')
    else:
        print('failed!')

txt.close()
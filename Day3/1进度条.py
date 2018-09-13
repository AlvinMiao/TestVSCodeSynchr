import sys
from time import sleep#a单独引入方法
for i in range(20):
	sys.stdout.write("#")
	sys.stdout.flush()#缓冲区同步刷新
	sleep(0.2)#休眠时间，也可以说是程序打印间隔时间

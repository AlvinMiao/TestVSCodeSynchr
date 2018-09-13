#斐波那契数列引导出生成器
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		#print(b)
		yield b#yield在这里相当于保存了函数的中断状态，也就是返回当前状态的这个值
		a,b = b,a+b
		#t = (b,a+b)
		#a = t[0]
		#b = t[1]
		n = n+1
	return "done"
f = fib(10)
print(f)

#print("=====start loop=====")
'''
for i in f:
	print(i)
'''
#异常处理，通过__next()__方法超出range的时候，就会报错，对这一类报错需要进行一个异常处理

while True:
	try:
		x = next(f)
		print("f:",x)
	except StopIteration as e:
		print("Generator return value:",e.value)#这里的错误信息是生成器最后return的值
		break


#通过yield实现单线程情况下的并行效果

#简单的生产消费者模型

import time
def consumer(name):
	'''
	消费者模型
	'''
	print("%s 准备吃包子了"%name)
	while True:
		baozi = yield

		print("包子[%s]来了，被[%s]吃了！"%(baozi,name))

# c = consumer("alvin")
# c.__next__()#next仅仅是调用yield但是不传值给yield
# b1 = "香菇馅"
# c.send(b1)#调用yield，同时传值给yield


def productor(name):
	'''
	生产者模型
	'''
	c = consumer('A')
	c2 = consumer('B')
	c.__next__()
	c2.__next__()
	print("开始做包子了")

	for i in range(10):
		time.sleep(1)
		print("做了2个包子")
		c.send(i)
		c2.send(i)

productor("alvin")

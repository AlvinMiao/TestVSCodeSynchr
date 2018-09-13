#装饰器：本质上是函数，(装饰其他函数)就是为其他函数添加附加的功能
#装饰器的原则
'''
1.不能修改被装饰的函数的源代码
2.不能修改被装饰的函数的调用方式

'''
import time

def timmer(func):
	def warpper(*args,**kwargs):
		strat_time = time.time()
		func()
		stop_time = time.time()
		print("the func run time is %s" %(stop_time-strat_time))
	return warpper

@timmer
def test():
	time.sleep(3)
	print("hello,world")

test()


#实现装饰器的知识
'''
1.函数即'变量'
2.高阶函数
3.嵌套函数

高阶函数+嵌套函数  ==>装饰器


'''
#匿名函数
clac = lambda x:x*3
print(clac(3))

#匿名函数在内存中的存放方式
'''
函数就是变量，定义一个函数就等于把函数体赋值给函数名
因为匿名函数没有函数名，即使用过后对应的内存就会被回收
'''

#装饰器之高阶函数
'''
把一个函数名当做实参传给另外一个函数(不修改被装饰函数源代码的情况下为其添加功能)
返回值中包含函数名(不修改函数的调用方式)
'''
def bar():
	time.sleep(2)
	print('in the bar')

def test(func):
	start_time = time.time()
	func()
	stop_time = time.time()
	print("the func run time is %s"%(stop_time-start_time))

test(bar)

def foo():
	time.sleep(2)
	print('in the foo')

def test2(func):
	print(func)
	return(func)

#test2(foo)
foo = test2(foo)
foo()

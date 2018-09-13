'''
名称 特征 关键字
面向对象的编程 类 ---> class
面向过程的编程 过程 ---> def
函数式编程 函数 ---> def


def test(x): ---> 关键字 函数名 (参数)
	"test definition" ---> 描述当前函数
	x += 1 ---> 代码块的处理逻辑(函数体)
	return x ---> 返回值
'''

#函数：
def func1():
	'''test function'''
	print("in the func1")
	return 0

#过程：
def func2():
	'''Testing'''
	print("in the function2")

#过程相比较函数没有返回值
#x=func1()
#y=func2()

#print("from function1 return is %s"%x)
#print('from function2 return is %s'%y)
#在没有定义返回值的情况下，python会默认返回一个none值

import time #导入时间模块


time_format = "%Y-%m-%d %X"#定义时间格式
time_current = time.strftime(time_format)

def logger():
	'''creating logger file'''
	with open('logger.txt','a+') as f1:
		f1.write("%s ending code\n" %time_current)


def test():
	'''Testing'''
	print('hello world')
	logger()

#是个函数就得调用才能生效
#test()

'''
time.strftime()该函数接收以时间为元组，并返回可读字符串表示当地时间
时间格式由定义的格式所决定
函数的优点：
减少重复代码
保持数据一致
程序的可扩展性
'''

def function1():
	print('hello world')
	return 'str'

x=function1()

def mini():
	print("miao")
	return function1()

i = mini()#这里i是对mini这个function进行了调用
print('type of i:',type(i),i)


def CS():
	print('halo')
	return 'a'

def CS1():
	print('a')
	return CS()

j = CS1#j从某种意义上来讲算是对CS1这个function的一个指针
#指针就是一个变量，存储的是一段内存地址，并且在后续的程序运行中可以被更改
print('type of j:',type(j),j)


#参数组
#*是固定格式，args是形参名
#*args接收位置参数，并转换成元祖的方式
def demo1(*args):
	print(args)


#多个实参以tuple的形式传递给args
demo1(1,2,3,4)
demo1(*[1,1,2,3,5])#*args = *[1,1,,2,3,5]

#将多个关键字参数转换成字典的方式进行存储
def demo2(**kwargs):
	print(kwargs)
	#取出字典当中的元素
	print(kwargs['name'])
	print(kwargs['age'])


demo2(name='alvin',age=23)
demo2(**{'name':'Alvin','age':23})

#跟位置参数一起使用

def demo3(name,**kwargs):
	print(name)
	print(kwargs)

demo3('Saber')#若只传一个位置参数，后面的值将接受一个空字典

#跟默认参数结合
def demo4(name,sex='F',**kwargs):#参数组只能置于形参的最后
	print(name)
	print(sex)
	print(kwargs)

demo4('Archer',age=18)

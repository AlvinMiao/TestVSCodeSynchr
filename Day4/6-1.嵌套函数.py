#嵌套函数
def foo():
	print('in the foo')
	def bar():
		print('in the bar')
	bar()

#foo()

#在上一个栗子当中，bar()就类似于局部变量，作用域只在函数foo()中才能生效


#局部作用域和全局作用域的访问顺序
x = 0
def grandpa():
	x = 1
	def dad():
		x = 2
		def son():
			x = 3
			print(x)
		son()
	dad()
# grandpa()
#dad和son的调用都是同一个道理，因为程序在运行的时候，def所定义的内部函数相当于一个变量，变量需要被引用才能在代码块中生效，同理，函数在内部也需要被调用才能保证代码块的正确运行


#装饰器的最终形态
user,passwd = 'alvin','abc123'
def auth(auth_type):
	print('auth func:',auth_type)
	def outer_warpper(func):
		def warpper(*args,**kwargs):
			if auth_type == "local":
				print('warpper func args:',*args,**kwargs)
				username = input('Username:').strip()
				password = input('Password:').strip()
				if user == username and passwd == password:
					print('User has passed authentication')
					res = func(*args,**kwargs)
					print('-----after authentication-----')
					return res
				else:
					exit('Invalid Username or Password')
			elif auth_type == "ldap":
				print("ldap")
		return warpper
	return outer_warpper



def index():
	print("welcome to index page")

@auth(auth_type='local')
def home():
	print("welcome to home page")
	return "from home"

@auth(auth_type='ldap')
def bbs():
	print("welcome to bbs page")

index()
home()
bbs()

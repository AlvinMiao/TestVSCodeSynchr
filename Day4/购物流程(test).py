def login(func):
	'''
	这个是用于测试用户登录的模块，如果用户密码输错三次就将其写入黑名单中
	'''
	def warpper(*args,**kwargs):
		with open('blackName.txt','r+',encoding='utf-8') as lock_file,\
			open('user.txt','r+',encoding='utf-8') as access_file:
			#验证所输入用户是否在黑名单
			username = input('please input your username:').strip()
			for lock in lock_file:
				lock_user = lock.strip()#取出黑名单文件当中的用户信息
				if username == lock_user:
					print('This user have been locked,please contact admin!')
					break
				else:
					continue
			#用户验证模块
			if username != lock_user:
				passwd = input('please input your password:').strip()
				for account in access_file:
					#获取文件当中的信息，类似用户名和密码
					account_user = account.strip().split(" ")[0]
					account_passwd = account.strip().split(" ")[1]
					if username == account_user:
						if passwd == account_passwd:
							print("欢迎，%s"%account_user)
							func(*args,**kwargs)
							break
						else:
							print("Invalid password")
							#如果说第一次用户输入密码错误则进入该循环重新输入
							for count in range(0,2):
								count += 1
								passwd == input("please input your password:").strip()
								if passwd == account_passwd:
									print("欢迎，%s"%account_user)#需要断点测试
									func(*args,**kwargs)
									break
								else:
									print("Wrong password")
							if count == 2:
								print("This user have been locked,please contact admin!")
								lock_file.writelines(username)
								lock_file.close()#将信息写入之后关闭文件关闭该进程
				if username != account_user:
					print("No Such user")
	return warpper



def index():
    print('welcome to index page\n')
    print('--------after authtication-------')
    print('\n')

@login
def home():
    print('welcome to home page')

index()
home()

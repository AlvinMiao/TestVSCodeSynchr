#简单实现shell sed功能
'''
old_str = input('请输入要修改的字符：')
replace_str = input('请输入要替换的字符：')
with open('yesterday.txt','r',encoding='utf-8') as f1,\
	open('yeterday.bak','w',encoding='utf-8') as f2:
	 for line in f1.readlines():
	 	line = line.replace(old_str,replace_str)
	 	print(line)
	 	f2.write(line)
'''
#字符串转换字典

b = '''{
        'bakend': 'www.oldboy.org',
        'record':{
            'server': '100.1.7.9',
            'weight': 20,
            'maxconn': 30
        }
    }'''

#eval将字符串转换成json数据类型
# b = eval(b)
# print(b)
username,passwd = 'alvin','abc123'
def out(func):
    def warpper(*args,**kwargs):
        with open('blackName.txt','w+',encoding='utf-8') as f1:
            flie_list = f1.readlines()
            count = 0
            lock = []
            name = input('请输入用户名：').strip()
            #开始判断用户是否在黑名单
            for i in flie_list:
                line = i.strip("\n")
                lock.append(line)
            if name in lock:
                exit('对不起，您的账户已被锁定，请联系管理员')
            else:
                #如果用户没有在黑名单，判断用户是否存在
                if name == username:
                    while count < 3:
                        password = input('请输入密码：').strip()
                        if name == username and password == passwd:
                            print('欢迎，%s'%username)
                            func
                            break
                        else:
                            print('账号密码不匹配')
                            count += 1
                            if count == 3:
                                print("对不起，您的账号已被锁定，请联系管理员")
                                li = ['%s'%username]
                                f1.writelines(li)
                                exit()
                    else:
                        print("对不起，您的账号已被锁定，请联系管理员")
                        li = ['%s'%username]
                        f1.writelines(li)
                else:
                    print('Invalid Username or password')
                    exit()
    return warpper





def index():
    print('welcome to index page\n')
    print('--------after authtication-------')
    print('\n')

@out
def home():
    print('welcome to home page')

index()
home()


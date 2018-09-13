# arg = {
# 	'backend':'www.oldboy.org',
# 	'record':{
# 		'server':'100.1.7.9',
# 		'weight':20,
# 		'maxconn':3000
# 	}
# }

#大致的思路
'''
逐行读取文件
当遇到backend+域名的行的时候，将其子作用域放到一个空列表显示给用户看
再当我遇到以backend开头的时候就结束循环就ok了
因为这个子作用域是需要显示
的，就要拿出来，所以要特别显示出来，要与众不同，所以我们在这里定义标志位来显示这个与众不同
'''

def select(arg):
	result = []
	flag = False
	with open('haproxy.txt','r',encoding='utf-8') as f:
		for line in f:
			if line.strip() == "backend %s" %arg:
				flag = True
				continue
			if line.strip().startswith('backend'):
				flag = False
			if flag:
				result.append(line)
	return result

ret = select("www.oldboy.org")
for i in ret:
	print(i)



#更改购物车
'''
商品信息存在文件中(可以用代买读取文件信息，并且用列表的形式呈现)
已购买商品，余额记录
可以添加商品，修改价格
'''
#-r,以只读的模式打开该文件
#readlines()读取文件之后是以列表呈现
'''
with open('D:/PythonSpace/Day2/购物清单.txt','r') as f:
	for item,line in enumerate(f.readlines()):
		print(item,line.strip())


f1 = open('D:/PythonSpace/Day2/购物清单.txt','r')
try:
	lines = f1.readlines()
	print("type=",type(lines))
	for line in lines:
		print("line=",line)
finally:
	f1.close()

with open('D:/PythonSpace/Day2/工资表.txt','a') as f1:
	f1.writelines('Alvin,3800')
'''

Salary = input("please input your salary:")
if Salary.isdigit():
	Salary = int(Salary)
	while True:


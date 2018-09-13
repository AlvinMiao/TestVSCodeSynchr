'''
要求:
启动程序之后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
允许用户选择商品后，检测余额否足够，够就直接进行扣款，不够进行提醒
可随时退出，退出时，打印已购买商品和余额
'''

#练习
_salary_ = input("please input your salary:")
Goods_list = [
	['iphone',5800],
	['Mac pro',12000],
	['Ipad',3200],
	['Ipod',980],
	['Iwatch',10600],
	['Phone',3200]
]
shoping_list = []

if  _salary_.isdigit():#用.isdigit进行判断，如果用户输入是string则进行类型更改
	_salary_ = int(_salary_)
	while True:
		for index,item in enumerate(Goods_list):
			#print(Goods_list.index(item),item)
			print(index,item)#enumerate 取出列表下标

		User_Choose = input("选择你要购买的商品>>>:")
		if User_Choose.isdigit():
			User_Choose = int(User_Choose)
			if User_Choose < len(Goods_list) and User_Choose >= 0 :
				p_item = Goods_list[User_Choose]
				if p_item[1] <= _salary_:
					shoping_list.append(p_item)
					_salary_ -= p_item[1]
					print("Added %s into shopping cart,your current balance is %s" %(p_item,_salary_))
				else:
					print("您的余额还剩%s，已不足购买[%s]号商品"%(_salary_,User_Choose))
			else:
				print("不存在你所选择的商品编号[%s],请重新输入"%(User_Choose))
		elif User_Choose == 'q':
			print("------Shopping List------")
			for p in shoping_list:
				print(p)
			print("您的余额为:",_salary_)
			exit()
		else:
			print("Invaild Choose....")
else:
	print("不存在你所输入的选项...")
	exit()


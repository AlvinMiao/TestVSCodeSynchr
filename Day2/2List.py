Names = ["Alvin","Alex","ZhangSan","BuZhiHan","NanMo","Lufy","Merlin","Arthur","Alvin"]

#取值
print(Names[1])#列标取单个数值
print(Names[1:3])#从下标为1的值开始，到下标为3的值结束，其中不包括3,切片取值
print(Names[-1])#在不知道列表长度的时候单独取最后一个
print(Names[-3:-1])#切片的取值方法是从列表的左边开始数的
print(Names[-2:])#切片取列表的最后两个值

#追加
Names.append("TangXiaoWu")#追加在末尾
Names.insert(1,"Appache")#插入在指定位置

#更改
Names[1] = "Ngnix"

#删除
'''
Names.remove("Alex")
print(Names)
#del Names[1] = Names.pop(1)
#Names.pop()#在不输入下标的情况下删除列表最后一个
'''


print(Names.index("ZhangSan"))#查找指定元素的位置
print(Names.count("Alvin"))#统计某个元素的重复个数
Names.sort#根据特殊符号，数字，大写，小写进行排序(ASCII码)



#List.copy浅copy如果list1当中存在list2则当list2被更改的时候，copy的副本也会更改

'''
完全独立的两份备份的话 import copy
list2 = copy.deepcopy(list1)
完全独立的两个内存块

列表循环
for i in list：
	print(i)

步长切片：
print list[0:-1:2] = print list[::2]

sys模块是用c语言所编写的便以其自带的模块，不同于os有对应的os.py文件

浅copy：
list2 = list1.copy() 相对应的list2中的元素是list1当中的一个引用
两种浅copy的方式：
list2 = copy.copy(list1)
list2 = list1[:]  完全切片的浅copy
list2 = list(list1) 工厂函数
'''

#元组
#元组的长度在创建的过程中已经定论，不可被修改，只可以增，查

tuple1 = ('Alex','Alvin')
#字典只有两个方法，index&count
#使用情况，即相对比较重要的值，不希望被更改的，类似数据库连接等

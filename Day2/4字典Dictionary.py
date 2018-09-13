#集合和字典
#字典----> 一种key-value的数据类型
'''
字典的特性：
键值对
无序(没有下标)
key必须是唯一的
'''

info = {
	'stu1001':"Alvin",
	'stu1002':"Arche",
	'stu1003':"Saber",
}

B = {
	'stu1001':"Assassin",
	1:2,
	3:4
}

info.update(B)#合并两个字典，有相同的key就覆盖，没有就插入进去
print(info)
print(info.items())#将字典的所有元素转换成列表,Key--Value以元祖的形式呈现

C = dict.fromkeys([6,7,8],"Test")#初始化一个单层字典,前面是Key后面是Value

X = dict.fromkeys([1,2,3],[1,{"Name":"Alvin"},231])
print(X)
X[2][1]['Name'] = "Alvin Chen"
print(X)
#.fromkeys()这个方法所有的Key所指向的都是同一个内存地址，所以，当一个Value被更改的时候其他的Key所对应的Value都会被更改


'''
改和查
#print(info["stu1001"])
info["stu1001"]="Lancer"#改
info["stu1004"]="Caster"#基于健进行查询，如不存在就是增加

print(info.get("stu1004"))#自己不确定字典是不是有这个key的时候,如果存在就会返回值，不存在则返回none
print('stu1005' in info)#判断该健是不是存在于这个dic
python2------info.has_key("stu1005")

print(info.values)#.values输出的是不包括key的值
print(info.keys)#输出所有key值
'''

'''
删
del info["stu1004"]#python自带删除的方法
info.pop("stu1004")#指定删除
info.popitem()#随机删除
'''
#多级字典的嵌套

China = {
	"HuNan":{
		"ChangSha":["KaiFu","TianXin","FuRong"],
		"ZhuZhou":["ShiFeng","HuSong"],
		"XiangTan":["YueTang","YuHu"],
	},
	"JiangSu":{
		"NanJing":["XuanWu","FuKou"],
		"ChangZhou":["TianNing","ZhongLou"],
	},
}
#相关操作
#China["JiangSu"]["ChangZhou"][] = "2" #根据级别一级一级向下最后一级选择下标

#China.setdefault("GuangZhou",{"DongGuan"}:["DongCheng","XiCheng"])
#.setdefault()这个方法的作用主要是用于对当前的dict进行查询，如果Key值存在就将Key所对应的值返回，如果不存在就创建一个新的，值就是自己所定义这个
#所有的Key值建议最好是使用非中文，以免编译过程出现乱码
print(China)

'''
Json和pickle的对比
Json只可以序列化相对简单的数据类型，比如字典这种，对于函数这类json无法序列化
pickle可以序列化python当中的所有数据类型。
'''

#Json的序列与反序列
'''
import json

info = {
	'name':"alvin",
	'age':22,
}

将数据写入到文件当中(序列化)
f = open('json.txt','w+')
f.write(json.dumps(info))
反序列化
data = json.loads(f.read()) 定义一个临时变量用来承载反序列的数据额
'''

#pickle的序列与反序列
import pickle

def sayhi(name):
	print("hello"，name)

info = {
	'name':'alvin',
	'age':22,
	'func':sayhi
}

f = open("pickle.txt",'wb')#因为pickle序列化之后的数据类型为byte
f.write(pickle.dumps(info))
f.close()
#pickle序列化的另一种写法
'''
pickle.dump(info,f)------>(要序列化的对象，写入的文件)
f.close()
'''


'''
f = open("pickle.txt",'rb)
dat = pickle.loads(f.read())
f.close()
反序列化的另一种写法
dat = pickle.load(f)

info当中写入了一个func的内存地址，但是由于内存在使用过后就会被释放，除非在反序列的代码当中有相同的数据，不然就会出现数据的缺失，当然也不建议这样使用
'''

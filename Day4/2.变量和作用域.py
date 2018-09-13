#局部变量
def test(name,age=18,*args,**kwargs):
	print(name)
	print(age)
	print(args)
	print(kwargs)
	logger("test4")

def logger(source):
	print('from %s'%source)


name = "Saber"
school = "Los.edu"
def change_name(name):
	global school
	print("before chage",name,school)
	school = "GUI"
	#定义一个只在函数里面生效的局部变量
	name="alvin chen"
	print("after name",name)

name='alvin'
change_name(name)
print(name)
print(school)

#不要用global改局部变量为全局，因为一个函数可能会在程序的多个地方出现

#列表，字典，集合可以在局部变量里面更改全局变量的值(除了字符串和整数不能再局部变量里面进行更改)
names = ["Saber","Arche","Caster"]
def change_list():
	names[0] = "Alvin"
	print("inside func:",names)

change_list()
print(names)

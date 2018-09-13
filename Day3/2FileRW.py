#对于文件的操作
#the way to open the file
import io
f = open("购物清单.txt",'r',encoding="utf-8")
#f在这里就是文件句柄，即文件的内存对象包含文件名，字符集，大小，在内存的起始位置
#open当中可以写相对路径或者直接写绝对路径
#打开的文件编码格式依照系统默认来看
data = f.read()
date2 = f.readlines()
print(data)
print("----------date2----------",date2)
#文件在被读过之后，句柄的位置发生变化到了文件的末尾，所以在第二次读是不会有任何数据出现
f.close()

#fi = open("购物清单.txt",'r',encoding="utf-8")
#da = fi.readlines()

#f1 = open("WriteTest.txt",'w',encoding="utf-8")
#j = f1.write("我爱北京天安门,\n")
#j1 = f1.writelines(da)
'''
read,readline,readlines三个方法的差异，前两者读取文件都是以字符串的形式进行读取，read则会读取整个文件，并且有多少行就读取多少行，即一次性读取，而readline则是单行读取，readlines则是一次性读取整个文件，并且以列表的形式所体现

w在python中是以写的情况打开一个文件，如果已经存在这个文件，则会出现覆盖的情况

文件操作权限
r只读模式打开
w只写模式打开
a追加模式在文件指针的地方开始写入

'''

'''
write,writeline
write所传入的是一个字符串，不管代码写多少行，要是没有换行符，都会写在第一行里面
writelines则传入的是一个序列，即传入的值是一个列表类型的时候，会自动进行换行
'''

f = open("WriteTest.txt",'r',encoding="utf-8")
for index,line in enumerate(f.readlines()):
	if index == 9:
		print('-------------------')
		continue
	print(line.strip())
f.close
#在基于上述循环的情况下,为了保证读取大文件的时候程序顺畅，更改以下写法
f = open("WriteTest.txt",'r',encoding='utf-8')
#计数
count = 0
for line in f:
	if count == 9:
		print("---------------")
		count += 1
		continue
	print(line)
f.close()
#对比两种写法，后者相较于前者效率更为的高，并且使用内存更小
#当然上述的办法是将f转换为迭代器

#其他方法：
'''
f.tell()#获取文件指针的位置，按照一行数据有多少字符进行计数
f.seek()#指定该文件的指针位置，默认为第0个字符
f.encoding() #文件编码
f.errors()#文件异常处理
f.fileno()#显示python所调用的IO对象的接口
f.name()#打印文件名字
f.seekable()#判断该文件是否是可操作的，类似tty文件就不可被操作，返回布尔值
f.isatty()#判断指定文件是不是tty(终端设备文件)
f.flush()#刷新缓冲区

#关于内存缓存，考虑到程序写入硬盘的效率，于是并非写一行就到硬盘，而是先在缓存区进行一下停留，保证程序的正常运行，等缓冲区满了或者是程序终止再写入到硬盘当中去
#.flush()则是强制将内存缓冲区的数据写入到硬盘，并清空缓冲区
f.truncate()从文件指针所在的位置开始截断，默认从0开始，即清空当前文件
'''
#文件的修改
'''
可读可写 r+ 以读和追加的形式打开文件
可写可读 w+ 先创建一个文件，再开始写
由于在源文件上的修改等同于覆盖，所以在python3.0+之后不再允许在文件指针处进行修改
a+ 追加读写
rb 以二进制的形式读写文件
rb的使用情形，网络传输Socket
在python3.0之后socket传输只能用二进制模式在2.0中还可以使用字符传输

'''
f = open("Test","wb")
f.write("Hello,Byte\n".encode())#文件内不按照二进制模式进行处理
f.close()

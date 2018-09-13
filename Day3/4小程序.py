import io
import sys

'''
f = open("WriteTest.txt",'r',encoding='utf-8')
f_new = open('WriteTest.bak','w',encoding='utf-8')

for line in f:
	if "Just gonna stand there and watch me burn" in line:
		line = line.replace("Just gonna stand there and watch me burn","just standing there")
	f_new.write(line)
f.close()
f_new.close()
'''
#字符编码
#在python2.7的环境下，字符编码默认是ASCII码
#编结码的方法
'''
str.encode()编码
str.decode()解码
当str的编码格式已经是目标编码格式(s=u'你好'那就不能在解码成utf-8或者unicode码)
'''
#-*-coding:gbk-*- #这里只对文件的编码格式进行更改

s = '你好'#这里的编码格式为Unicode
s_gbk = s.encode('gbk')#Unicode ---> gbk
gbk_utf8 = s_gbk.decode("gbk").encode('utf-8')

print(gbk_utf8)
print(s_gbk)
#在python3中，encode不光更改了编码集，还会把字符集改为byte类型

#编码中gbk向下兼容gb18030向下兼容gb2312

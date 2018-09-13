#！/use/bin/env
'''
name = "Alvin"
print("my name is", name)
'''
# 简单的input程序
'''
name = input("What is your name ?")
print("Hello" + name)
'''

# 格式化输出:
username = input("Username:")
Job = input("Job:")
Age = int(input("Age:"))  # 这里int代表强制将数据类型进行转换

info = '''
-------info of %s -------
Username:%s
Job:%s
Age:%d
''' % (username,username,Job,Age)
# 括号里面的变量要和上面占位符的需求一致

info2 = '''
-------info of {_name} -------
Username:{_username}
Job:{_Job}
Age:{_Age}
'''.format(
    _name=username,
    _username=username,
    _Job=Job,
    _Age=Age
)
# 元素和'_'所定义的临时变量相互对应，组成一个list的对应关系（健--值）

info3 = '''
-------info of {0} -------
Username:{0}
Job:{1}
Age:{2}
'''.format(username,Job,Age)
print(info3)

#%s代表字符串输出 %d数字输出 f--->浮点型输出
# 在python2中有一个raw_input作用和input类似
# 在python2中的input() 接收的什么格式就输出什么格式
# 即需要输出字符串必须加""

'''
对比format2和format3中间可以发现
format2以键值对的方式呈现出来的list虽然代码看上去比较的复杂，但是清晰地知道输出的内容或者是format的是什么
format3最大的好处则是简化代码量，用下标的方式代表元素，但是不能清晰地表达编码者的意图
'''

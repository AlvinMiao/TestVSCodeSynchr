# 密文输入密码
'''
import getpass

_username = input("username:")
_password = input("password:")
# 调用这个方法用于加密密码
#Password = getpass.getpass("password:")
print(_username, _password)

# if---else流控制
if _username == "Alvin" and _password == "123":
    print("Welcome user {name} login".format(name=_username))
else:
    print("Invalid username")
'''

#猜年龄
_Age_of_somebody = 56
_age_of_guess = int(input("please input your guess："))
if _age_of_guess == _Age_of_somebody:
	print("Yes,you got it!")
elif _age_of_guess > _Age_of_somebody:
	print("Think smaller...")
else:
	print("Think bigger...")

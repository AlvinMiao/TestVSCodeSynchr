#基于猜年龄的程序来写循环
'''
_Age_of_somebody = 56
_age_of_guess = int(input("please input your guess："))
if _age_of_guess == _Age_of_somebody:
	print("Yes,you got it!")
elif _age_of_guess > _Age_of_somebody:
	print("Think smaller...")
else:
	print("Think bigger...")
'''

'''
#最简单的while循环
count = 0
while True:
	print("count:",count)
	count+=1
	if count == 1000:
		break
'''

'''
_Age_of_somebody = 56
_age_of_guess = int(input("please input your guess："))
#计数循环
count = 0
while True: #while count <= 3
	if count == 3:
		break
	if _age_of_guess == _Age_of_somebody:
		print("Yes,you got it!")
		break
	elif _age_of_guess > _Age_of_somebody:
		print("Think smaller...")
	else:
		print("Think bigger...")
	count +=1
'''

#优化版
#计数循环
_Age_of_somebody = 56
count = 0
while count < 3:
	_age_of_guess = int(input("please input your guess："))

	if _age_of_guess == _Age_of_somebody:
		print("Yes,you got it!")
		break
	elif _age_of_guess > _Age_of_somebody:
		print("Think smaller...")
	else:
		print("Think bigger...")
	count +=1
	if count == 3:
		_continueFlag_ = input("do you want to try again y/n ")
		if _continueFlag_ == 'y':
			count =0
		elif _continueFlag_ == 'n':
			print("thanks....")
		else:
			print("Invaild choose....")

'''
else: #表示如果上述循环体成立则，内部循环结束，不用输出，若不成立，则else输出
	print("you have tried too many times...")
'''



'''
for i in range(10):#i为循环的临时变量，range等于循环从0开始循环10次
	print("loop",i)
'''


'''
#for循环版本的猜年龄
_Age_of_somebody = 56
for i in range(3):
	_age_of_guess = int(input("please input your guess："))
	if _age_of_guess == _Age_of_somebody:
		print("Yes,you got it!")
		break
	elif _age_of_guess > _Age_of_somebody:
		print("Think smaller...")
	else:
		print("Think bigger...")
if i >= 2:
	_continue_flag_ = input("do you want to try again? y/n ")
	if _continue_flag_ == 'y':
		i = 0
	elif _continue_flag_ == 'n':
		print("thanks....")
	else:
		print("Invaild choose....")

'''

#当for循环正常结束，才会执行这个else,break跳出的话不会执行该段代码
'''
else:
	print("you've tried too many times...")

#for循环只输出偶数
for i in range (0,10,2):#从零开始，循环十次，要求输出的数字能被2整除，这个2被称为步程
	print("loop",i)

'''
#continue 跳出本次循环开始下一次循环
#break 结束整个循环

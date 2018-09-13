#三级菜单
china = {
	'北京':{
		"沙河":{

		},
		"朝阳":{
			"望京":["奔驰","陌陌"],
			"国贸":["CICC","HP"],
			"东直门":["Advent","飞信"]
		},
		"海淀":{

		},
	},
	'山东':{
		"德州":{

		},
		"青岛":{

		},
		"济南":{

		},
	},

}

exit_flag = False

while not exit_flag:
	for i in china:
		print(i)
	choice = input("选择进入1>>>:")
	if choice in china:
		while not exit_flag:
			for j in china[choice]:
				print("\t",j)

			choice2 = input("选择进入2>>>:")
			if choice2 in china[choice]:
				while not exit_flag:
					for i3 in china[choice][choice2]:
						print("\t\t",i3)

					choice3 = input("选择进入3>>>:")
					if choice3 in china[choice][choice2]:
						for i4 in china[choice][choice2][choice3]:
							print("\t\t",i4)

						choice4 = input("最后一层，按b返回，按q退出>>>:")
						if choice4 == "b":
							pass#pass在这里相当于什么也不做一是用来站位，而是什么也不做
						elif choice4 == "q":
							exit_flag = True
					if choice3 == "b":
						break
					elif choice3 == "q":
						exit_flag = True
			if choice2 == "b":
				break
			elif choice2 == "q":
				exit_flag = True

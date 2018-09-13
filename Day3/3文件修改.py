import io

f = open("WriteTest.txt",'r',encoding='utf-8')
f_new = open('WriteTest.bak','w',encoding='utf-8')

for line in f:
	if "Just gonna stand there and watch me burn" in line:
		line = line.replace("Just gonna stand there and watch me burn","just standing there")
	f_new.write(line)
f.close()
f_new.close()

#

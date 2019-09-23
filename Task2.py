"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
#建立字典
#1.建立播出号码字典
number_time_dic = {}
for i in range(len(calls)):
	key = calls[i][0]
	value = 0
	for m in range(len(calls)):
		if key == calls[m][0]:
			value = int(value)+int(calls[m][3])
	for n in range(len(calls)):
		if key == calls[n][1]:
			value = int(value)+int(calls[n][3])
	if key not in number_time_dic:
		number_time_dic.update({key:value})
#2.字典加入接收号码
for i in range(len(calls)):
	if calls[i][1] not in number_time_dic:
		key = calls[i][1]
		value = 0
		for n in range(len(calls)):
			if key == calls[n][1]:
				value = int(value)+int(calls[n][3])
		number_time_dic.update({key:value})

#找到最大值并输出信息
for key,value in number_time_dic.items():
	if(value == max(number_time_dic.values())):
		print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key,value))	
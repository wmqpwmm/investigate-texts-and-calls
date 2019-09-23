"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
#删除非电话号码信息
def del_time(list_intact,n):
	for i in range(len(list_intact)):
		del list_intact[i][2]
del_time(texts,2)
del_time(calls,2)
del_time(calls,2)

#组成新列表
telephone_numbers_repetitive = []
for i in range(len(texts)):
	telephone_numbers_repetitive.extend(texts[i])
for i in range(len(calls)):
	telephone_numbers_repetitive.extend(calls[i])

#非重复电话计数
telephone_numbers = []
count = 0
for i in range(len(telephone_numbers_repetitive)):
	if telephone_numbers_repetitive[i] not in telephone_numbers:
		count += 1
		telephone_numbers.append(telephone_numbers_repetitive[i])

#输出结果
print("There are {} different telephone numbers in the records.".format(count))

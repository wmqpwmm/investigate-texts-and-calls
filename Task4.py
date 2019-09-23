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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电
请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
#1建立播出电话、接收电话、短信电话列表
call_n_list = []
answer_n_list =[]
text_list = []

for i in range(len(calls)):
	call_n_list.append(calls[i][0])

for i in range(len(calls)):
	answer_n_list.append(calls[i][1])

for i in range(len(texts)):
	text_list.extend(texts[i][0:2])
#2.建立非电话推销号码列表
not_telemarketers = answer_n_list + text_list
#3.找到电话推销号码
telemarketers = []
for number in call_n_list:
	if number not in not_telemarketers:
		telemarketers.append(number)
telemarketers = sorted(list(set(telemarketers)))
#4.输出结果
print("These numbers could be telemarketers: ")
for number in telemarketers:
	print(number)

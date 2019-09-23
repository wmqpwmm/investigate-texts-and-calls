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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。
第一部分: 找出被班加罗尔地区（Bangalore）的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。
输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。
第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？
输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

#第一部分
#1.找出播出号码为Bangalore地区的电话记录
bg_n = "(080)"
bg_calln_list = []
bg_calln_list_r = []
for i in range(len(calls)):
	if bg_n in calls[i][0]:
		bg_calln_list.append(calls[i][1])
N = len(bg_calln_list)#播出号码为Bangalore地区的电话记录总条数
for i in range(len(bg_calln_list)):
	if bg_n in bg_calln_list[i]:
		bg_calln_list_r.append(bg_calln_list[i])
M = len(bg_calln_list_r)#播出号码和接受号码均为Bangalore地区的电话记录总条数
#3.找codes
codes_list = []
fixed_b = "("
fixed_e = ")"
mobiles = ["7","8","9"]
sells = "140"
for i in range(len(bg_calln_list)):
	if bg_calln_list[i][0] == fixed_b:
		for n in range(len(bg_calln_list[i])):
			if bg_calln_list[i][n] == fixed_e:
				codes_list.append(bg_calln_list[i][0:n+1])
	elif bg_calln_list[i][0] in mobiles:
		codes_list.append(bg_calln_list[i][0:4])
	elif bg_calln_list[i][0:3] == sells:
		codes_list.append(bg_calln_list[i][0:4])

#3.去重和排序
codes_list = list(set(codes_list))
codes_list.sort()
#4.输出结果
print("The numbers called by people in Bangalore have codes:")
for i in codes_list:
    print(i)

#第二部分
print("\n{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(M/N*100,2)))

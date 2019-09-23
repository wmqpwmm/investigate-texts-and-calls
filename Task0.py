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
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
text_list = texts[0]
call_list = calls[len(calls)-1]

print("First record of texts, {} texts {} at time {}".format(str(text_list[0]),str(text_list[1]),str(text_list[2])))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(str(call_list[0]),str(call_list[1]),str(call_list[2]),str(call_list[3])))

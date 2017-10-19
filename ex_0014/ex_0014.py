#第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
#{
#	"1":["张三",150,120,100],
#	"2":["李四",90,99,95],
#	"3":["王五",60,66,68]
#}
#请将上述内容写到 student.xls 文件中，如下图所示：
import pandas as pd
import json
import win32api
filepath = "data/Student.txt"
f = open(filepath)
s = f.read()
s = json.loads(s)
df = pd.DataFrame(s)
df = df.T
df.to_excel("data/Student.xls",header = None)
win32api.ShellExecute(0, 'open', 'excel.exe', 'data/Student.xls', '', 1)# 打开文件
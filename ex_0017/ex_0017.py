#第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如
#下所示：
#<?xml version="1.0" encoding="UTF-8"?>
#<root>
#<students>
#<!--
#	学生信息表
#	"id" : [名字, 数学, 语文, 英文]
#-->
#{
#	"1" : ["张三", 150, 120, 100],
#	"2" : ["李四", 90, 99, 95],
#	"3" : ["王五", 60, 66, 68]
#}
#</students>
#</root>
import pandas as pd
import xml.dom
import win32api
filepath = "d:/python_project/ex_0014/data/Student.xls"
df = pd.read_excel(filepath,header = None)#,index_col= 0)
#df = dict(df)
#df = json.dumps(df, ensure_ascii=False, indent=1)
#df = df.to_json(force_ascii = False,orient = 'split')
str1 = "{\n\t"
for i in range(3):
    str1 = str1 + str(df.ix[i].values)
    str1 = str1 + "\n\t"
str1 = str1.replace("[","\"")
#str1 = str1.replace(" ",",")
str1 = str1.replace(" '","\" : [\"")
str1 = str1.replace("'","\"")
str1 = str1 + "\n  }"
#str1 = str1.replace(" ",",")
#str1 = "{\n\t" + str1
print(str1)
dom=xml.dom.getDOMImplementation()#创建文档对象，文档对象用于创建各种节点。
doc=dom.createDocument(None,"root",None)
root = doc.documentElement
students = doc.createElement('students')
root.appendChild(students)
comment = doc.createComment('\n\t学生信息表\n\t\"id\":[名字，数学，语文，英文]\n')
students.appendChild(comment)
nameT=doc.createTextNode(str1)
students.appendChild(nameT)
xmlfile=open('student.xml','w')
doc.writexml(xmlfile,addindent=' ', newl='\n', encoding='utf-8')
xmlfile.close()
win32api.ShellExecute(0, 'open', 'notepad.exe', 'student.xml', '', 1)# 打开文件
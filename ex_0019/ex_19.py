#第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
#所示：
#<?xml version="1.0" encoding="UTF-8"?>
#<root>
#<numbers>
#<!--
#	数字信息
#-->
#[
#	[1, 82, 65535],
#	[20, 90, 13],
#	[26, 809, 1024]
#]
#</numbers>
#</root>
import pandas as pd
import xml.dom
import win32api
filepath = "d:/python_project/ex_0016/data/numbers.xls"
def Write_xls2xml(filepath,element,comment,savepath):
    try:
        df = pd.read_excel(filepath, header=None)  # ,index_col= 0)
    except IOError:
        print("Cannot open file:\"", filepath, "\",please check!")
        exit()
    str1 = "[\n\t["#调整格式以符合题意
    for i in range(3):
        for j in range(3):
            str1 = str1 + str(df.ix[i][j])
            if j < 2:
                str1 = str1 + ", "
            if j == 2 and i != 2:
                str1 = str1 + "],\n\t["
    str1 = str1 + "]\n  ]"
    dom=xml.dom.getDOMImplementation()#创建文档对象，文档对象用于创建各种节点。
    doc=dom.createDocument(None,"root",None)#创建根节点
    root = doc.documentElement
    students = doc.createElement(element)#创建元素
    root.appendChild(students)
    comment = doc.createComment(comment)#创建comment
    students.appendChild(comment)
    nameT=doc.createTextNode(str1)
    students.appendChild(nameT)
    xmlfile=open(savepath,'w')
    doc.writexml(xmlfile,addindent=' ', newl='\n', encoding='utf-8')#写入的文件有转义字符&quot;,所以下一步需要重新读取并整理数据
    xmlfile.close()
    xml_file = open(savepath)#重新读取xml并转换转义字符
    try:
        xml_content = xml_file.read()  #
    finally:
        xml_file.close()
    xml_content =xml_content.replace("&quot;","\"")#替换转义字符
    output = open(savepath, 'w')
    output.write(xml_content)
    output.close( )
    win32api.ShellExecute(0, 'open', 'notepad.exe', savepath, '', 1)# 打开文件
if __name__ =="__main__":
    comment = '\n\t数字信息\n'
    Write_xls2xml(filepath,"numbers",comment,'numbers.xml')
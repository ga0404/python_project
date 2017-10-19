#第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
#[
#	[1, 82, 65535],
#	[20, 90, 13],
#	[26, 809, 1024]
#]
#请将上述内容写到 numbers.xls 文件中，如下图所示：
import pandas as pd
import json
import win32api
filepath = "data/numbers.txt"
f = open(filepath)
s = f.read()
s = json.loads(s)
df = pd.DataFrame(s)
print(df)
#df = df.T
df.to_excel("data/numbers.xls",header = None,index = None)
win32api.ShellExecute(0, 'open', 'excel.exe', 'data/numbers.xls', '', 1)      # 打开文件
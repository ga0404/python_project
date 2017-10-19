#第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，
#然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」
#，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，
#对每月通话时间做个统计。
import pandas as pd
filepath = "data/2017年09月语音通信.xls"
def phone_time(filepath):
    try:
        data = pd.read_excel(filepath)  # ,index_col= 0)
    except IOError:
        print("Cannot open file:\"", filepath, "\",please check!")
        exit()
    time = pd.DataFrame(data, columns=['通话时长'])
    print(time)
if __name__ =="__main__":
    phone_time(filepath)
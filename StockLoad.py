# -- coding:utf-8--

import sys
import urllib.request
import time


# 查看日K线图：
# http://image.sinajs.cn/newchart/daily/n/sh601006.gif
# 分时线的查询：
# http://image.sinajs.cn/newchart/min/n/sh000001.gif
# 周K线查询：
# http://image.sinajs.cn/newchart/weekly/n/sh000001.gif
# 月K线查询：
# http://image.sinajs.cn/newchart/monthly/n/sh000001.gif

def f(value):
    return "{:0,.2f}".format(round(float(value), 2))


stocks = []
fileInfo = open("d:\\analysisStock.txt")

for line in fileInfo:
    stocks.append(line)

while True:
    dateStr = ""
    for oneStockInfo in stocks:
        try:
            oneStock = oneStockInfo.split(",")
            noticeMessage = " "
            oneStock = oneStockInfo.split(",")
            if oneStock[1][0] == "1":  # 去掉回车符号
                noticeMessage = "********"

            res_data = urllib.request.urlopen('http://hq.sinajs.cn/list=' + oneStock[0]).read().decode('gb2312')
            # print(res_data)
            info = res_data.split(",")
            if dateStr == "":
                dateStr = info[31]
                print("-" * 50 + dateStr)

            stockNameInfo = info[0]
            stockNameStartPos = stockNameInfo.index('"')
            stockName = stockNameInfo[stockNameStartPos + 1:]
            print("%s %s\t%s\t%s\t%s%%\t%s\t%s\t%s\t%s" % (
                stockName, f(info[1]), f(info[2]), f(info[3]),
                f(100 * (float(info[3]) - float(info[2])) / float(info[2])), f(float(info[3]) - float(info[2])),
                f(info[4]), f(info[5]), noticeMessage))
        except:
            print(sys.exc_info())

    time.sleep(5)



    # 查看日K线图：
    # http://image.sinajs.cn/newchart/daily/n/sh601006.gif
    # 分时线的查询：
    # http://image.sinajs.cn/newchart/min/n/sh000001.gif
    # 周K线查询：
    # http://image.sinajs.cn/newchart/weekly/n/sh000001.gif
    # 月K线查询：
    # http://image.sinajs.cn/newchart/monthly/n/sh000001.gif

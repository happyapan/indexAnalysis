# -- coding:utf-8--

import sys
import urllib.request
import time
import os
from stock_analysis.Avg import Avg
from stock.BaseStock import BaseStock
import tools.TimeUtil as timeUtil

def f(value):
    format_value ="{:0,.2f}".format(round(float(value), 2))
    if len(format_value) == 4:
        format_value = " " + format_value
    if len(format_value) == 5:
        format_value = " " + format_value
    return format_value


stocks = []
fileInfo = open("D:" + os.sep + "analysisStock.txt")

for line in fileInfo:
    stocks.append(line)

avg = Avg()
avg_clos = {}
base = BaseStock("base")
pingan_datas = base.get_stock_data('601318.SH', 'PingAn', '20190701', timeUtil.day_after(0))
lastest_trade_date = pingan_datas[0].get_trade_date()
print("lastest_trade_date:"+lastest_trade_date)
while True:
    dateStr = ""
    for oneStockInfo in stocks:
        oneStockInfo = oneStockInfo.strip('\n')
        oneStockInfo = oneStockInfo.strip(' ')
        try:
            if oneStockInfo[0] == '#':
                continue
            elif oneStockInfo == '000001':
                stock_code = oneStockInfo+".SZ"
                oneStockInfo = 'sh' + oneStockInfo
            elif oneStockInfo[0] in ['0', '3']:
                stock_code = oneStockInfo + ".SZ"
                oneStockInfo = 'sz' + oneStockInfo
            elif oneStockInfo[0] in ['6']:
                stock_code = oneStockInfo + ".SH"
                oneStockInfo = 'sh' + oneStockInfo

            res_data = urllib.request.urlopen('http://hq.sinajs.cn/list=' + oneStockInfo).read().decode('gb2312')
            # print(res_data)
            info = res_data.split(",")
            if dateStr == "":
                dateStr = info[31]
                print("-" * 50 + dateStr)

            stockNameInfo = info[0]
            stockNameStartPos = stockNameInfo.index('"')
            stockName = stockNameInfo[stockNameStartPos + 1:]

            avg_result = None
            if oneStockInfo in ['sz399001', 'sz399006', 'sh000001']:
                pass
            elif stock_code in avg_clos.keys():
                avg_result = avg_clos[stock_code]
            else:
                avg_result = avg.get_avg(stock_code, "")
                avg_clos[stock_code] = avg_result

            if len(stockName) == 3:
                stockName = stockName + " "

            if  oneStockInfo in ['sz399001', 'sz399006', 'sh000001']:
                print("%s %s %s %s[    5     10     20     30] %s%% %s %s %s" % (
                    stockName, f(info[1]), f(info[2]), f(info[3])
                    , f(100 * (float(info[3]) - float(info[2])) / float(info[2])), f(float(info[3]) - float(info[2])),
                    f(info[4]), f(info[5])))
            else:
                print("%s %s %s %s[%s %s %s %s] %s%% %s %s %s" % (
                    stockName,
                    f(info[1]),
                    f(info[2]),
                    f(info[3]),
                    f(avg_result[lastest_trade_date]["5"]),
                    f(avg_result[lastest_trade_date]["10"]),
                    f(avg_result[lastest_trade_date]["20"]),
                    f(avg_result[lastest_trade_date]["30"]),
                    f(100 * (float(info[3]) - float(info[2])) / float(info[2])), f(float(info[3]) - float(info[2])),
                    f(info[4]),
                    f(info[5])))
        except:
            print(sys.exc_info())

    time.sleep(5)

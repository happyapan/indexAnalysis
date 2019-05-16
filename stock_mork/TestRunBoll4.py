from stock.BaseStock import BaseStock
import IndexConstants
import sys

import stock_mork.StockMork_15_3_5 as stockMork_15_3_5

base = BaseStock("base")

# ----------------------------------------------------------------------------------------------
stock = base.get_all_60_stock()
statistics_data = {
    "winTime": 0,
    "winMoney": 0,
    "down5LineTime": 0,
    "down5LineMoney": 0,
    "lostTime": 0,
    "lostMoney": 0,
    "otherTime": 0,
    "otherMoney": 0
}
for one in stock:
    savedStdout = sys.stdout  # 保存标准输出流
    with open(IndexConstants.date_file_path + "15_3_5_60.txt", 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        stockMork_15_3_5.mork_bollBackDownLine_15_3_5(one, stock[one], statistics_data)
    sys.stdout = savedStdout  # 恢复标准输出流

stock = base.get_all_30_stock()
statistics_data = {
    "winTime": 0,
    "winMoney": 0,
    "down5LineTime": 0,
    "down5LineMoney": 0,
    "lostTime": 0,
    "lostMoney": 0,
    "otherTime": 0,
    "otherMoney": 0
}
for one in stock:
    savedStdout = sys.stdout  # 保存标准输出流
    with open(IndexConstants.date_file_path + "15_3_5_30.txt", 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        stockMork_15_3_5.mork_bollBackDownLine_15_3_5(one, stock[one], statistics_data)
    sys.stdout = savedStdout  # 恢复标准输出流

stock = base.get_all_00_stock()
statistics_data = {
    "winTime": 0,
    "winMoney": 0,
    "down5LineTime": 0,
    "down5LineMoney": 0,
    "lostTime": 0,
    "lostMoney": 0,
    "otherTime": 0,
    "otherMoney": 0
}
for one in stock:
    savedStdout = sys.stdout  # 保存标准输出流
    with open(IndexConstants.date_file_path + "15_3_5_00.txt", 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        stockMork_15_3_5.mork_bollBackDownLine_15_3_5(one, stock[one], statistics_data)
    sys.stdout = savedStdout  # 恢复标准输出流

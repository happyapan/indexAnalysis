from stock.BaseStock import BaseStock
import IndexConstants
import sys
import stock_mork.StockMork_20_5_9 as stockMork_20_5_9
import stock_mork.StockMork_20_3_9 as stockMork_20_3_9
import stock_mork.StockMork_10_3_9 as stockMork_10_3_9
import stock_mork.StockMork_20_5_5 as stockMork_20_5_5


base = BaseStock("base")
stock = base.get_all_stock()
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
    with open(IndexConstants.date_file_path + "20_3_9.txt", 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        stockMork_20_3_9.mork_bollBackDownLine_20_3_9(one, stock[one], statistics_data)
    sys.stdout = savedStdout  # 恢复标准输出流

# ----------------------------------------------------------------------------------------------
stock = base.get_all_stock()
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
    with open(IndexConstants.date_file_path + "20_5_9.txt", 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        stockMork_20_5_9.mork_bollBackDownLine_20_5_9(one, stock[one], statistics_data)
    sys.stdout = savedStdout  # 恢复标准输出流

# ----------------------------------------------------------------------------------------------
stock = base.get_all_stock()
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
    with open(IndexConstants.date_file_path + "10_3_9.txt", 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        stockMork_10_3_9.mork_bollBackDownLine_10_3_9(one, stock[one], statistics_data)
    sys.stdout = savedStdout  # 恢复标准输出流

# ----------------------------------------------------------------------------------------------
stock = base.get_all_stock()
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
    with open(IndexConstants.date_file_path + "20_5_5.txt", 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        stockMork_20_5_5.mork_bollBackDownLine_20_5_5(one, stock[one], statistics_data)
    sys.stdout = savedStdout  # 恢复标准输出流

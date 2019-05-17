from stock.BaseStock import BaseStock
import IndexConstants
import sys

from stock_mork.StockMork import MorkBollBackDownLine

base = BaseStock("base")
mork_ball = MorkBollBackDownLine(10, -3, 5, 5, 999)

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
savedStdout = sys.stdout  # 保存标准输出流
with open(IndexConstants.date_file_path + "10_3_5_60.txt", 'at') as file:
    sys.stdout = file  # 标准输出重定向至文件
    for one in stock:
        mork_ball.mork_bollBackDownLine(one, stock[one], statistics_data)
sys.stdout = savedStdout  # 恢复标准输出流

# ----------------------------------------------------------------------------------------------
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
savedStdout = sys.stdout  # 保存标准输出流
with open(IndexConstants.date_file_path + "10_3_5_30.txt", 'at') as file:
    sys.stdout = file  # 标准输出重定向至文件
    for one in stock:
        mork_ball.mork_bollBackDownLine(one, stock[one], statistics_data)
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
savedStdout = sys.stdout  # 保存标准输出流
with open(IndexConstants.date_file_path + "10_3_5_00.txt", 'at') as file:
    sys.stdout = file  # 标准输出重定向至文件
    for one in stock:
        mork_ball.mork_bollBackDownLine(one, stock[one], statistics_data)
sys.stdout = savedStdout  # 恢复标准输出流
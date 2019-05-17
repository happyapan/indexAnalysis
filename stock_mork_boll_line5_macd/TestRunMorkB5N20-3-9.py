from stock.BaseStock import BaseStock
import IndexConstants
import sys

from stock_mork_boll_line5_macd.StockMorkB5M import MorkB5N

base = BaseStock("base")
mork_ball = MorkB5N(20, -3, 9, 5, 999, -999, 99999)

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
with open(IndexConstants.date_file_path + "MorkB5N20_3_9_5_999_Z_60.txt", 'at') as file:
    sys.stdout = file  # 标准输出重定向至文件
    for one in stock:
        mork_ball.mork_b5m(one, stock[one], statistics_data)
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

savedStdout = sys.stdout  # 保存标准输出流
with open(IndexConstants.date_file_path + "MorkB5N20_3_9_5_999_Z_30.txt", 'at') as file:
    sys.stdout = file  # 标准输出重定向至文件
    for one in stock:
        mork_ball.mork_b5m(one, stock[one], statistics_data)
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
with open(IndexConstants.date_file_path + "MorkB5N20_3_9_5_999_Z_00.txt", 'at') as file:
    sys.stdout = file  # 标准输出重定向至文件
    for one in stock:
        mork_ball.mork_b5m(one, stock[one], statistics_data)
sys.stdout = savedStdout  # 恢复标准输出流
from stock.BaseStock import BaseStock
import tools.TimeUtil as timeUtil
import IndexConstants as constant
import time
from tools.PrintUtil import *

base = BaseStock("base")
stock = base.get_all_stock()

count = 1
index = 1
for one in stock:
    print(str(count) + "--" + one)
    count = count + 1
    index = index + 1
    stock_datas = base.query_stock_data(one, stock[one], timeUtil.day_after(-20000), timeUtil.today())
    if stock_datas is not None:
        stock_file_path = constant.stock_file_path + one + '.txt'
        p_file_list_with_no_format(stock_file_path, stock_datas)

    # stock_datas_hfq = base.query_stock_data_hfq(one, stock[one], timeUtil.day_after(-20000), timeUtil.today())
    # if stock_datas_hfq is not None:
    #     stock_file_path = constant.stock_file_path_hfq + one + '.txt'
    #     p_file_list_with_no_format(stock_file_path, stock_datas_hfq)

    if index > 190:
        print("wait 1 minute for tushare rule.....")
        time.sleep(60)
        index = 0


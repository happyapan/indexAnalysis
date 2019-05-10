from indexData.BaseData import BaseData
from tools.PrintUtil import *
import IndexConstants


class All_Stock(BaseData):
    def fresh_stock_code(self):
        data = self.pro.query('stock_basic', exchange='', list_status='L',
                              fields='ts_code,name,industry')
        stock_datas = data.values.tolist()
        print("Start Writing stock data......")
        if stock_datas is not None:
            p_file_list(IndexConstants.all_stock_full_path, stock_datas)
        print("success!")


all_stock = All_Stock("allStock")
all_stock.fresh_stock_code()

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

            # all_ST_stock_path = date_file_path + "01All_ST.txt"
            # all_60_stock_path = date_file_path + "01All_60.txt"
            # all_00_stock_path = date_file_path + "01All_00.txt"
            # all_30_stock_path = date_file_path + "01All_30.txt"
            temp_code = []
            for i in stock_datas:
                if i[0].startswith("6"):
                    temp_code.append(i)
            p_file_list(IndexConstants.all_60_stock_path, temp_code)

            temp_code = []
            for i in stock_datas:
                if i[0].startswith("0"):
                    temp_code.append(i)
            p_file_list(IndexConstants.all_00_stock_path, temp_code)

            temp_code = []
            for i in stock_datas:
                if i[0].startswith("3"):
                    temp_code.append(i)
            p_file_list(IndexConstants.all_30_stock_path, temp_code)

            temp_code = []
            for i in stock_datas:
                if "ST" in str(i[1]):
                    temp_code.append(i)
            p_file_list(IndexConstants.all_ST_stock_path, temp_code)

        print("success!")


all_stock = All_Stock("allStock")
all_stock.fresh_stock_code()

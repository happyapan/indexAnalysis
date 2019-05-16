import IndexConstants as constants
from indexData.BaseData import BaseData
import tools.TimeUtil as timeUtil
import tools.PrintUtil as printUtil
from stock.StockDayData import StockDayData
import operator

from stock.StockDayDataHFQ import StockDayDataHFQ


class BaseStock(BaseData):
    def __init__(self, name):
        self.total_stock = {}
        self.total_st_stock = {}
        self.total_60_stock = {}
        self.total_30_stock = {}
        self.total_00_stock = {}
        BaseData.__init__(self, name)

    def get_all_stock(self):
        if len(self.total_stock) > 0:
            return self.total_stock
        else:
            all_data = printUtil.read_file_list(constants.all_stock_full_path)
            for one_stock in all_data:
                detail = str(one_stock).split(",")
                self.total_stock[detail[0]] = detail[1]
        return self.total_stock

    def get_all_st_stock(self):
        if len(self.total_st_stock) > 0:
            return self.total_st_stock
        else:
            all_data = printUtil.read_file_list(constants.all_ST_stock_path)
            for one_stock in all_data:
                detail = str(one_stock).split(",")
                self.total_st_stock[detail[0]] = detail[1]
        return self.total_st_stock

    def get_all_60_stock(self):
        if len(self.total_60_stock) > 0:
            return self.total_60_stock
        else:
            all_data = printUtil.read_file_list(constants.all_60_stock_path)
            for one_stock in all_data:
                detail = str(one_stock).split(",")
                self.total_60_stock[detail[0]] = detail[1]
        return self.total_60_stock

    def get_all_30_stock(self):
        if len(self.total_30_stock) > 0:
            return self.total_30_stock
        else:
            all_data = printUtil.read_file_list(constants.all_30_stock_path)
            for one_stock in all_data:
                detail = str(one_stock).split(",")
                self.total_30_stock[detail[0]] = detail[1]
        return self.total_30_stock

    def get_all_00_stock(self):
        if len(self.total_00_stock) > 0:
            return self.total_00_stock
        else:
            all_data = printUtil.read_file_list(constants.all_00_stock_path)
            for one_stock in all_data:
                detail = str(one_stock).split(",")
                self.total_00_stock[detail[0]] = detail[1]
        return self.total_00_stock

    def query_stock_data(self, stock_code, stock_name, start_date, end_date):
        stock_datas = []
        resultList = self.pro.query('daily', ts_code=stock_code, start_date=start_date,
                                    end_date=end_date).values.tolist()
        # ts_code trade_date  open  high   low  close  pre_close  change    pct_chg  vol  amount
        if resultList is not None and len(resultList) > 0:
            for one in resultList:
                stock_datas.append(StockDayData(one))
        return stock_datas

    #后赋权 --接口有问题
    # def query_stock_data_hfq(self, stock_code, stock_name, start_date, end_date):
    #     stock_datas_hfq = []
    #     resultList = self.pro.pro_bar(ts_code=stock_code, adj='hfq', start_date=start_date, end_date=end_date)\
    #         .values.tolist()
    #     # ts_code trade_date  open  high   low  close  pre_close  change    pct_chg  vol  amount
    #     if resultList is not None and len(resultList) > 0:
    #         for one in resultList:
    #             stock_datas_hfq.append(StockDayDataHFQ(one))
    #     return stock_datas_hfq

    #日期 大 到 小 也就是 近到远
    def get_stock_data(self, stock_code, stock_name, start_date, end_date):
        # print("Get %s[%s]   from %s to %s" % (stock_code, stock_name, start_date, end_date))
        stocks = printUtil.read_file_list(constants.stock_file_path + stock_code + ".txt")
        if stocks is not None and len(stocks) > 0:
            stock_datas = []
            for one in stocks:
                oneRowData = one.split(",")
                trade_date = oneRowData[1]
                if operator.ge(trade_date, start_date) and operator.le(trade_date, end_date):
                    stock_datas.append(StockDayData(oneRowData))
            return stock_datas
        return None

    # def get_stock_data_hfq(self, stock_code, stock_name, start_date, end_date):
    #     # print("Get %s[%s]   from %s to %s" % (stock_code, stock_name, start_date, end_date))
    #     stocks = printUtil.read_file_list(constants.stock_file_path_hfq + stock_code + ".txt")
    #     if stocks is not None and len(stocks) > 0:
    #         stock_datas = []
    #         for one in stocks:
    #             oneRowData = one.split(",")
    #             trade_date = oneRowData[1]
    #             if operator.ge(trade_date, start_date) and operator.le(trade_date, end_date):
    #                 stock_datas.append(StockDayDataHFQ(oneRowData))
    #         return stock_datas
    #     return None

    # def get_stock_realtime(self, stock_code):
    #     resultList = self.pro.ts.get_realtime_quotes('000581').values.tolist()
    #     # ts_code trade_date  open  high   low  close  pre_close  change    pct_chg  vol  amount
    #     if resultList is not None and len(resultList) > 0:
    #         for one in resultList:
    #              print(one)



##TEST
# base = BaseStock("base")
# datas = base.get_stock_data('000004.SZ', '国农科技', '20190302', timeUtil.day_after(-1))
# printUtil.p_list(datas)
#
# print(base.query_stock_data('000004.SZ', '国农科技', timeUtil.day_after(-1), timeUtil.day_after(-1))[0])

# stock = base.get_all_stock()
#
# count = 1
# for one in stock:
#     base.get_one_stock_daily(one, stock[one])
#     count = count + 1
#     if count > 20:
#         break
# base = BaseStock("base")
# base.get_stock_realtime("000004.SZ")

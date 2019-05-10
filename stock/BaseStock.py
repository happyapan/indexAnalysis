import IndexConstants as constants
from indexData.BaseData import BaseData
import tools.TimeUtil as timeUtil
import tools.PrintUtil as printUtil
from stock.StockDayData import StockDayData


class BaseStock(BaseData):
    def __init__(self, name):
        self.total_stock = {}
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

    def query_stock_data(self, stock_code, stock_name, start_date, end_date):
        stock_datas = []
        resultList = self.pro.query('daily', ts_code=stock_code, start_date=start_date,
                                    end_date=end_date).values.tolist()
        # ts_code trade_date  open  high   low  close  pre_close  change    pct_chg  vol  amount
        if resultList is not None and len(resultList) > 0:
            for one in resultList:
                stock_datas.append(StockDayData(one))
        return stock_datas



##TEST
# base = BaseStock("base")
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

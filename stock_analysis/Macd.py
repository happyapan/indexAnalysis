from stock.BaseStock import BaseStock
import tools.TimeUtil as timeUtil


class Macd(object):
    def __init__(self):
        self.base = BaseStock("base")
        self._ema_short = []
        self._ema_lang = []
        self._diff = []
        self._eda = []
        self._delta=[]
        self.trade_date = []

        # 短时
        self.short = 12
        # 长时
        self.long = 26
        # DIF参数：9
        self.dif = 9

    # {
    #     '20190513': {
    #         'diff': 0.7732937859731557,
    #         'eda': 0.9415498112527317,
    #         'macd': -0.3365120505591521
    #     },
    #     '20190514': {
    #         'diff': 0.6013899635176436,
    #         'eda': 0.8735178417057141,
    #         'macd': -0.544255756376141
    #     }
    # }
    def get_macd(self, stock_code, stock_name):
        day_len= -20000
        date = timeUtil.today()
        stock_dates = self.base.get_stock_data(stock_code, stock_name, timeUtil.day_after_day(date, day_len), date)
        if stock_dates is not None and len(stock_dates) > 1:
            stock_dates.reverse()
            macd_result = {}
            # 计算EMA
            EMA1 = []
            EMA2 = []
            for index in range(len(stock_dates)):
                self.trade_date.append(stock_dates[index].get_trade_date())
                if index == 0:
                    # 初始化短时EMA和长时EMA
                    EMA1.append(stock_dates[index].get_close())
                    EMA2.append(stock_dates[index].get_close())
                else:
                    EMA1.append(
                        2 / (self.short + 1) * (stock_dates[index].get_close() - EMA1[index - 1]) + EMA1[index - 1])
                    EMA2.append(
                        2 / (self.long + 1) * (stock_dates[index].get_close() - EMA2[index - 1]) + EMA2[index - 1])

            self._ema_short = EMA1
            self._ema_lang = EMA2
            self._diff = []
            for index in range(len(EMA1)):
                self._diff.append(EMA1[index]-EMA2[index])

            for index in range(len(EMA1)):
                if index == 0:
                    self._eda.append(self._diff[index])
                else:
                    self._eda.append(
                        2 / (self.dif + 1) * (self._diff[index] - self._eda[index - 1]) + self._eda[index - 1])

            # macd
            self._delta =[]
            for index in range(len(self._diff)):
                self._delta.append((self._diff[index]-self._eda[index])*2)

            for ii in range(0,len(self.trade_date)):
                macd_result[self.trade_date[ii]] = {
                    "diff": self._diff[ii],
                    "eda": self._eda[ii],
                    "macd": self._delta[ii]
                }
            return macd_result

        else:
            print("No Data Find! %s[%s] on  %s " % (stock_code, stock_name, date))
            return None

# macd = Macd()
# result = macd.get_macd('000004.SZ', '国农科技')
# print(result)
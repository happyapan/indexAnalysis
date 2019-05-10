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

        # 短时
        self.short = 12
        # 长时
        self.long = 26
        # DIF参数：9
        self.dif = 9

    def get_macd(self, stock_code, stock_name, date, day_len):
        stock_dates = self.base.get_stock_data_hfq(stock_code, stock_name, timeUtil.day_after_day(date, -1 * day_len), date)

        if stock_dates is not None and len(stock_dates) > 1:
            stock_dates.reverse()
            trade_date=[]
            # 计算EMA
            EMA1 = []
            EMA2 = []
            for index in range(len(stock_dates)):
                trade_date.append(stock_dates[index].get_trade_date())
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

            #macd
            self._delta =[]
            for index in range(len(self._diff)):
                self._delta.append((self._diff[index]-self._eda[index])*2)

            for index in range(len(self._delta)):
                print("%s diff[%.3f]--eda[%.3f] -- macd[%.3f]"%(trade_date[index],self._diff[index],self._eda[index],self._delta[index]))

        else:
            print("No Data Find! %s[%s] on  %s " % (stock_code, stock_name, date))


macd = Macd()
macd.get_macd('000004.SZ', '国农科技', '20190509', 20000)
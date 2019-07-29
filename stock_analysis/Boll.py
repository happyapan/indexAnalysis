from stock.BaseStock import BaseStock
import tools.TimeUtil as timeUtil
import math


class Boll(object):
    def __init__(self):
        self.analysis_day = 20
        self.base = BaseStock("base")
        self.up_track = []
        self.avg_line = []
        self.down_track = []
        self.trade_date = []

    # {
    #     '20190513': {
    #         'up_track': 20.895620489161818,
    #         'avg_line': 17.52700000000012,
    #         'down_track': 14.158379510838419
    #     },
    #     '20190514': {
    #         'up_track': 20.742542659338184,
    #         'avg_line': 17.343500000000116,
    #         'down_track': 13.94445734066205
    #     }
    # }
    def get_boll(self, stock_code, stock_name):

        day_len = -20000
        date = timeUtil.today()
        stock_dates = self.base.get_stock_data(stock_code, stock_name, timeUtil.day_after_day(date, day_len), date)
        if stock_dates is not None and len(stock_dates) > 1:
            boll_result = {}
            stock_dates.reverse()
            # N天之内所有的开盘总和
            day_count_sum = 0
            for index in range(len(stock_dates)):
                self.trade_date.append(stock_dates[index].get_trade_date())
                day_count_sum += stock_dates[index].get_close()
                if index < self.analysis_day:
                    boll_result[stock_dates[index].get_trade_date()]={
                        "up_track": 0,
                        "avg_line": 0,
                        "down_track": 0,
                    }
                else:
                    day_count_sum = day_count_sum - stock_dates[index - self.analysis_day].get_close()
                    middle_value = day_count_sum / self.analysis_day
                    md = 0.0
                    for i in range(index - self.analysis_day + 1, index + 1):
                        md = md + math.pow(middle_value - stock_dates[i].get_close(), 2)

                    md = md / self.analysis_day
                    md = math.sqrt(md)
                    boll_result[stock_dates[index].get_trade_date()] = {
                        "up_track": middle_value + 2 * md,
                        "avg_line": middle_value,
                        "down_track": middle_value - 2 * md,
                    }

            return boll_result
        else:
            return None


if __name__ == "__main__" :
    ball = Boll()
    result = ball.get_boll('300059.SZ', 'dfcf')
    print(result)

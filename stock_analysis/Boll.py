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

    # return {
    #     "trade_date": self.trade_date, 交易日期
    #     "up_track": self.up_track, 上轨
    #     "avg_line": self.avg_line,  中轨
    #     "down_track": self.down_track 下轨
    # }
    def get_boll(self, stock_code, stock_name):
        day_len = -20000
        date = timeUtil.today()
        stock_dates = self.base.get_stock_data_hfq(stock_code, stock_name, timeUtil.day_after_day(date, day_len), date)
        if stock_dates is not None and len(stock_dates) > 1:
            stock_dates.reverse()
            # N天之内所有的开盘总和
            day_count_sum = 0
            for index in range(len(stock_dates)):
                self.trade_date.append(stock_dates[index].get_trade_date())
                day_count_sum += stock_dates[index].get_close()
                if index < self.analysis_day:
                    self.up_track.append(0)
                    self.avg_line.append(0)
                    self.down_track.append(0)
                else:
                    day_count_sum = day_count_sum - stock_dates[index - self.analysis_day].get_close()
                    middle_value = day_count_sum / self.analysis_day
                    md = 0.0
                    for i in range(index - self.analysis_day + 1, index + 1):
                        md = md + math.pow(middle_value - stock_dates[i].get_close(), 2)

                    md = md / self.analysis_day
                    md = math.sqrt(md)
                    self.up_track.append(middle_value + 2 * md)
                    self.avg_line.append(middle_value)
                    self.down_track.append(middle_value - 2 * md)

            return {
                "trade_date": self.trade_date,
                "up_track": self.up_track,
                "avg_line": self.avg_line,
                "down_track": self.down_track
            }


# ball = Boll()
# result = ball.get_boll('000004.SZ', '国农科技')
# print(result["trade_date"])
# for pp in range(len(result["trade_date"])):
#     print("%s: Up[%.3f],Avg[%.3f],Down[%.3f]" % (
#         result["trade_date"][pp], result["up_track"][pp], result["avg_line"][pp], result["down_track"][pp]))

from stock.BaseStock import BaseStock
import tools.TimeUtil as timeUtil
import math


class Avg(object):
    def __init__(self):
        self.analysis_day = 20
        self.base = BaseStock("base")

    # return {
    #     "trade_date": trade_date,  交易日期
    #     "day5": day5_line,
    #     "day10": day10_line,
    #     "day20": day20_line,
    #     "day30": day30_line,
    #     "day60": day60_line,
    #     "day120": day120_line,
    # }
    def get_avg(self, stock_code, stock_name):
        day_len = -20000
        date = timeUtil.today()
        stock_dates = self.base.get_stock_data(stock_code, stock_name, timeUtil.day_after_day(date, day_len), date)
        if stock_dates is not None and len(stock_dates) > 1:
            stock_dates.reverse()
            day5_line = []
            day10_line = []
            day20_line = []
            day30_line = []
            day60_line = []
            day120_line = []
            trade_date = []

            day5 = 0
            day10 = 0
            day20 = 0
            day30 = 0
            day60 = 0
            day120 = 0

            for index in range(len(stock_dates)):
                trade_date.append(stock_dates[index].get_trade_date())

                # Day 5
                day5 += stock_dates[index].get_close()
                if index < 5:
                    day5_line.append(day5 / (index + 1))
                else:
                    day5 -= stock_dates[index - 5].get_close()
                    day5_line.append(day5 / 5)

                # Day 10
                day10 += stock_dates[index].get_close()
                if index < 10:
                    day10_line.append(day10 / (index + 1))
                else:
                    day10 -= stock_dates[index - 10].get_close()
                    day10_line.append(day10 / 10)

                # Day 20
                day20 += stock_dates[index].get_close()
                if index < 20:
                    day20_line.append(day20 / (index + 1))
                else:
                    day20 -= stock_dates[index - 20].get_close()
                    day20_line.append(day20 / 20)

                # Day 30
                day30 += stock_dates[index].get_close()
                if index < 30:
                    day30_line.append(day30 / (index + 1))
                else:
                    day30 -= stock_dates[index - 30].get_close()
                    day30_line.append(day30 / 30)

                # Day 60
                day60 += stock_dates[index].get_close()
                if index < 60:
                    day60_line.append(day60 / (index + 1))
                else:
                    day60 -= stock_dates[index - 60].get_close()
                    day60_line.append(day60 / 60)

                # Day 120
                day120 += stock_dates[index].get_close()
                if index < 120:
                    day120_line.append(day120 / (index + 1))
                else:
                    day120 -= stock_dates[index - 120].get_close()
                    day120_line.append(day120 / 120)

            # END LOOP-------------------------------

            return {
                "trade_date": trade_date,
                "day5": day5_line,
                "day10": day10_line,
                "day20": day20_line,
                "day30": day30_line,
                "day60": day60_line,
                "day120": day120_line,
            }

        else:
            return None


# avg = Avg()
# result = avg.get_avg('000004.SZ', '国农科技')
# for pp in range(len(result["trade_date"])):
#     print("%s: 5[%.3f],10[%.3f],20[%.3f],30[%.3f],60[%.3f],120[%.3f]" % (
#         result["trade_date"][pp], result["day5"][pp], result["day10"][pp], result["day20"][pp], result["day30"][pp],
#         result["day60"][pp], result["day120"][pp]))

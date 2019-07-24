from stock.BaseStock import BaseStock
import tools.TimeUtil as timeUtil
import math


class Avg(object):
    def __init__(self):
        self.analysis_day = 20
        self.base = BaseStock("base")


    def get_avg(self, stock_code, stock_name):
        day_len = -20000
        date = timeUtil.today()
        stock_dates = self.base.get_stock_data(stock_code, stock_name, timeUtil.day_after_day(date, day_len), date)
        if stock_dates is not None and len(stock_dates) > 1:
            avg_result= {}
            stock_dates.reverse()
            day3_line = []
            day4_line = []
            day5_line = []
            day6_line = []
            day7_line = []
            day8_line = []
            day9_line = []
            day10_line = []
            day15_line = []
            day20_line = []
            day30_line = []
            day60_line = []
            day120_line = []
            trade_date = []

            day3 = 0
            day4 = 0
            day5 = 0
            day6 = 0
            day7 = 0
            day8 = 0
            day9 = 0
            day10 = 0
            day15 = 0
            day20 = 0
            day30 = 0
            day60 = 0
            day120 = 0

            for index in range(len(stock_dates)):
                trade_date.append(stock_dates[index].get_trade_date())
                # Day 3
                day3 += stock_dates[index].get_close()
                if index < 3:
                    day3_line.append(day3 / (index + 1))
                else:
                    day3 -= stock_dates[index - 3].get_close()
                    day3_line.append(day3 / 3)

                # Day 4
                day4 += stock_dates[index].get_close()
                if index < 4:
                    day4_line.append(day4 / (index + 1))
                else:
                    day4 -= stock_dates[index - 4].get_close()
                    day4_line.append(day4 / 4)

                # Day 5
                day5 += stock_dates[index].get_close()
                if index < 5:
                    day5_line.append(day5 / (index + 1))
                else:
                    day5 -= stock_dates[index - 5].get_close()
                    day5_line.append(day5 / 5)

                # Day 6
                day6 += stock_dates[index].get_close()
                if index < 6:
                    day6_line.append(day6 / (index + 1))
                else:
                    day6 -= stock_dates[index - 6].get_close()
                    day6_line.append(day6 / 6)

                # Day 7
                day7 += stock_dates[index].get_close()
                if index < 7:
                    day7_line.append(day7 / (index + 1))
                else:
                    day7 -= stock_dates[index - 7].get_close()
                    day7_line.append(day7 / 7)

                # Day 8
                day8 += stock_dates[index].get_close()
                if index < 8:
                    day8_line.append(day8 / (index + 1))
                else:
                    day8 -= stock_dates[index - 8].get_close()
                    day8_line.append(day8 / 8)

                # Day 9
                day9 += stock_dates[index].get_close()
                if index < 9:
                    day9_line.append(day9 / (index + 1))
                else:
                    day9 -= stock_dates[index - 9].get_close()
                    day9_line.append(day9 / 9)

                # Day 10
                day10 += stock_dates[index].get_close()
                if index < 10:
                    day10_line.append(day10 / (index + 1))
                else:
                    day10 -= stock_dates[index - 10].get_close()
                    day10_line.append(day10 / 10)

                # Day 15
                day15 += stock_dates[index].get_close()
                if index < 15:
                    day15_line.append(day15 / (index + 1))
                else:
                    day15 -= stock_dates[index - 15].get_close()
                    day15_line.append(day15 / 15)

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

            for ii in range(0,len(trade_date)):
                avg_result[trade_date[ii]] = {
                    "3": day3_line[ii],
                    "4": day4_line[ii],
                    "5": day5_line[ii],
                    "6": day6_line[ii],
                    "7": day7_line[ii],
                    "8": day8_line[ii],
                    "9": day9_line[ii],
                    "10": day10_line[ii],
                    "15": day15_line[ii],
                    "20": day20_line[ii],
                    "30": day30_line[ii],
                    "60": day60_line[ii],
                    "120": day120_line[ii]
                }

            return avg_result
        else:
            return None


if __name__ =='main':
    avg = Avg()
    result = avg.get_avg('000004.SZ', '国农科技')
    print(result)

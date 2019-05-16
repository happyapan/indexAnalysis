import stock_strategy.BollBackDownLine as boll
import tools.TimeUtil as timeUtil
from stock.BaseStock import BaseStock
from stock_analysis.Avg import Avg
from stock_analysis.Boll import Boll


def mork_bollBackDownLine(stock_code, stock_name):
    day1_up = 0
    day1_down = 0
    day3_up = 0
    day3_down = 0
    base = BaseStock("base")
    avg = Avg()
    avg_result = avg.get_avg(stock_code, stock_name)
    ball_class = Boll()
    boll_result = ball_class.get_boll(stock_code, stock_name)

    for i in range(0, 150):
        catch_stock = boll.analysis_stock(stock_code, stock_name, timeUtil.day_after_day(timeUtil.today(), i * -1), boll_result)

        if catch_stock is not None:
            after_datas = base.get_stock_data(stock_code, stock_name,
                                              timeUtil.day_after_day(catch_stock.get_trade_date(), 1),
                                              timeUtil.day_after_day(catch_stock.get_trade_date(), 20))
            after_datas.reverse()
            # if len(after_datas) >= 1:
            #     if catch_stock.get_close() < after_datas[0].get_close():
            #         day1_up = day1_up + 1
            #     else:
            #         day1_down = day1_down + 1
            # if len(after_datas) >= 3:
            #     if catch_stock.get_close() < after_datas[2].get_close():
            #         day3_up = day3_up + 1
            #     else:
            #         day3_down = day3_down + 1
            if len(after_datas) >= 1:
                if catch_stock.get_down_line_day_count() >= 5:
                    print(stock_name+ ":" + str(catch_stock))
                    print("突破日股价[%.2f] Boll 下轨天数：%d" % (catch_stock.get_close(), catch_stock.get_down_line_day_count()))

                    print("Line5[%.3f] - close[%.3f]" % (avg.get_one_day_avg(avg_result, catch_stock.get_trade_date())["5"], catch_stock.get_close()))
                    print_avg_line(catch_stock, avg, avg_result, after_datas, 0)
                    if len(after_datas) >= 2:
                        print_avg_line(catch_stock, avg, avg_result, after_datas, 1)
                    if len(after_datas) >= 3:
                        print_avg_line(catch_stock, avg, avg_result, after_datas, 2)
                    if len(after_datas) >= 4:
                        print_avg_line(catch_stock, avg, avg_result, after_datas, 3)
                    if len(after_datas) >= 5:
                        print_avg_line(catch_stock, avg, avg_result, after_datas, 4)
                    if len(after_datas) >= 6:
                        print_avg_line(catch_stock, avg, avg_result, after_datas, 5)
                    if len(after_datas) >= 7:
                        print_avg_line(catch_stock, avg, avg_result, after_datas, 6)
                    if len(after_datas) >= 8:
                        print_avg_line(catch_stock, avg, avg_result, after_datas, 7)
                    if len(after_datas) >= 9:
                        print_avg_line(catch_stock, avg, avg_result, after_datas, 8)


def print_avg_line(catch_stock, avg, avg_result, after_datas, day_count):
    print("Mork --> Day %d[%.2f],[%.2f%%] VS Catch [%.2f],[%.2f%%] " % ((day_count+1),
                                                                                after_datas[day_count].get_close(),
                                                                                after_datas[day_count].get_pct_chg(),
                                                                                (after_datas[day_count].get_close() - catch_stock.get_close()),
                                                                                100 * (after_datas[day_count].get_close() - catch_stock.get_close()) / catch_stock.get_close()))
    one_day_avg = avg.get_one_day_avg(avg_result, after_datas[day_count].get_trade_date())
    print("Line3[%.3f] - Line5[%.3f] - Line6[%.3f] - Line8[%.3f] - close[%.3f]" % (one_day_avg["3"],
                                                                                   one_day_avg["5"],
                                                                                   one_day_avg["6"],
                                                                                   one_day_avg["8"],
                                                                                   after_datas[day_count].get_close()))
    # print("Line5[%.3f] - close[%.3f]" % ( one_day_avg["5"], after_datas[day_count].get_close()))




base = BaseStock("base")
stock = base.get_all_stock()
for one in stock:
    mork_bollBackDownLine(one, stock[one])


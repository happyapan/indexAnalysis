import stock_strategy.BollBackDownLine as boll
import tools.TimeUtil as timeUtil
from stock.BaseStock import BaseStock
from stock_analysis.Avg import Avg

def mork_bollBackDownLine_20_5_9(stock_code, stock_name, statistics_data):
    day1_up = 0
    day1_down = 0
    day3_up = 0
    day3_down = 0
    base = BaseStock("base")
    avg = Avg()
    avg_result = avg.get_avg(stock_code, stock_name)

    for i in range(0, 300):
        catch_stock = boll.analysis_stock(stock_code, stock_name, timeUtil.day_after_day(timeUtil.today(), i * -1))
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
                    test_trade = {
                        "startBuy": 0,
                        "startBuyDate": "",
                        "endBuy": 0,
                        "endBuyDate": "",
                        # 止损率
                        "lostBuffRate": -5,
                        # 止盈利率
                        "winBuffRate": 20,
                        "earn": 0,
                        "earnRate": 0,
                        "holdDay": 0,
                        "forceSell": False,
                        "forceSellType": ""
                    }

                    print("Line5[%.3f] - close[%.3f]" % (avg.get_one_day_avg(avg_result, catch_stock.get_trade_date())["5"], catch_stock.get_close()))
                    cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 0, test_trade)
                    if len(after_datas) >= 2:
                        cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 1, test_trade)
                    if len(after_datas) >= 3:
                        cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 2, test_trade)
                    if len(after_datas) >= 4:
                        cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 3, test_trade)
                    if len(after_datas) >= 5:
                        cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 4, test_trade)
                    if len(after_datas) >= 6:
                        cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 5, test_trade)
                    if len(after_datas) >= 7:
                        cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 6, test_trade)
                    if len(after_datas) >= 8:
                        cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 7, test_trade)
                    if len(after_datas) >= 9:
                        cal_print_avg_line(catch_stock, avg, avg_result, after_datas, 8, test_trade)

                    if test_trade["startBuy"] > 0:
                        print(test_trade)
                        if test_trade["forceSellType"] == "down5Line":
                            statistics_data["down5LineTime"]=statistics_data["down5LineTime"]+1
                            statistics_data["down5LineMoney"] = statistics_data["down5LineMoney"] + test_trade["earnRate"]
                        elif test_trade["forceSellType"] == "winBuffRate":
                            statistics_data["winTime"] = statistics_data["winTime"] + 1
                            statistics_data["winMoney"] = statistics_data["winMoney"] + test_trade["earnRate"]
                        elif test_trade["forceSellType"] == "lostBuffRate":
                            statistics_data["lostTime"] = statistics_data["lostTime"] + 1
                            statistics_data["lostMoney"] = statistics_data["lostMoney"] + test_trade["earnRate"]
                        else:
                            statistics_data["otherTime"] = statistics_data["otherTime"] + 1
                            statistics_data["otherMoney"] = statistics_data["otherMoney"] + test_trade["earnRate"]

                        print(statistics_data)



def cal_print_avg_line(catch_stock, avg, avg_result, after_datas, day_count, test_trade):
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
    # 当前价格突破5日线，买入
    if test_trade["startBuy"] == 0:
        if after_datas[day_count].get_close() > one_day_avg["5"]:
            test_trade["startBuy"] = after_datas[day_count].get_close()
            test_trade["holdDay"] = 1
            test_trade["startBuyDate"] = after_datas[day_count].get_trade_date()
    elif test_trade["forceSell"] == False:
        # 还未强制卖出
        test_trade["holdDay"] = test_trade["holdDay"] + 1
        test_trade["endBuy"] = after_datas[day_count].get_close()
        test_trade["endBuyDate"] = after_datas[day_count].get_trade_date()
        test_trade["earn"] = test_trade["endBuy"] - test_trade["startBuy"]
        # 计算损益
        test_trade["earnRate"] = 100 * (test_trade["endBuy"] - test_trade["startBuy"]) / test_trade["startBuy"]
        if after_datas[day_count].get_close() < one_day_avg["5"]:
            # 跌破5日线，抛出
            test_trade["forceSell"] = True
            test_trade["forceSellType"] = "down5Line"
            return test_trade
        #止盈或止损
        if test_trade["earnRate"] > test_trade["winBuffRate"]:
            test_trade["forceSell"] = True
            test_trade["forceSellType"] = "winBuffRate"
            return test_trade
        if test_trade["earnRate"] < test_trade["lostBuffRate"]:
            test_trade["forceSell"] = True
            test_trade["forceSellType"] = "lostBuffRate"
            return test_trade

    return test_trade

    # 当前价格跌破5日线，卖出

    # print("Line5[%.3f] - close[%.3f]" % ( one_day_avg["5"], after_datas[day_count].get_close()))









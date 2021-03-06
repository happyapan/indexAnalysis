import stock_strategy.BollBackDownLine as boll
import tools.TimeUtil as timeUtil
from stock.BaseStock import BaseStock
from stock_analysis.Avg import Avg
from stock_analysis.Boll import Boll


class MorkBollBackDownLine(object):

    def __init__(self, win_buff_rate, lost_buff_rate, cal_day, min_down_day, max_down_day):
        self._winBuffRate = win_buff_rate    # 止盈率
        self._lostBuffRate = lost_buff_rate  # 止损率
        self._calDay = cal_day               # 计算天数
        self._minDownDay = min_down_day      # boll 下轨最小天数
        self._maxDownDay = max_down_day      # boll 下轨最大天数

    def mork_bollBackDownLine(self, stock_code, stock_name, statistics_data):
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
                if len(after_datas) >= 1:
                    catch_down_line_day=catch_stock.get_down_line_day_count()
                    if catch_down_line_day >= self._minDownDay and catch_down_line_day <= self._maxDownDay:
                        print(stock_name + ":" + str(catch_stock))
                        print("%s	突破日股价	%.2f	Boll下轨天数	%d" % (stock_code, catch_stock.get_close(), catch_down_line_day))
                        test_trade = {
                            "stockCode": stock_code,
                            "startBuy": 0,
                            "startBuyDate": "",
                            "endBuy": 0,
                            "endBuyDate": "",
                            # 止损率
                            "lostBuffRate": self._lostBuffRate,
                            # 止盈利率
                            "winBuffRate": self._winBuffRate,
                            "earn": 0,
                            "earnRate": 0,
                            "holdDay": 0,
                            "forceSell": False,
                            "forceSellType": ""
                        }

                        print("Line5[%.3f] - close[%.3f]" % (avg_result[catch_stock.get_trade_date()]["5"], catch_stock.get_close()))
                        self.cal_print_avg_line(catch_stock, avg_result, after_datas, 0, test_trade)
                        for cal_day in range(2, self._calDay+1):
                            if len(after_datas) >= cal_day:
                                self.cal_print_avg_line(catch_stock, avg_result, after_datas, cal_day-1, test_trade)

                        if test_trade["startBuy"] > 0:
                            print("stockCode	%s	startBuy	%.2f	 startBuyDate	%s		endBuy	%.2f	endBuyDate	%s	earn	%.2f	earnRate	%.2f	holdDay	%d	forceSell	%s	forceSellType	%s"
                                  %(
                                      test_trade["stockCode"],
                                      test_trade["startBuy"],
                                      test_trade["startBuyDate"],
                                      test_trade["endBuy"],
                                      test_trade["endBuyDate"],
                                      test_trade["earn"],
                                      test_trade["earnRate"],
                                      test_trade["holdDay"],
                                      test_trade["forceSell"],
                                      test_trade["forceSellType"]
                                    )
                                )
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

                            print("code	%s	winTime	%d	winMoney	%.3f	down5LineTime	%d	down5LineMoney	%.3f	lostTime	%d	lostMoney	%.3f	otherTime	%d	otherMoney	%.3f"
                                  %(
                                      stock_code,
                                      statistics_data["winTime"],
                                      statistics_data["winMoney"],
                                      statistics_data["down5LineTime"],
                                      statistics_data["down5LineMoney"],
                                      statistics_data["lostTime"],
                                      statistics_data["lostMoney"],
                                      statistics_data["otherTime"],
                                      statistics_data["otherMoney"]
                                  )
                                  )

        return statistics_data


    def cal_print_avg_line(self, catch_stock, avg_result, after_datas, day_count, test_trade):

        print("%sMork 	Day%d	%.2f	%.2f%%	VS_Catch	%.2f	%.2f%%"
              % (
                  after_datas[day_count].get_trade_date(),
                  (day_count+1),
                  after_datas[day_count].get_close(),
                  after_datas[day_count].get_pct_chg(),
                  (after_datas[day_count].get_close() - catch_stock.get_close()),
                  100 * (after_datas[day_count].get_close() - catch_stock.get_close()) / catch_stock.get_close()
                )
              )

        one_day_avg = avg_result[after_datas[day_count].get_trade_date()]
        print("%sLine	Day5	%.3f	day3	%.3f	Day6	%.3f	day8	%.3f	close	%.3f"
              % (
                   after_datas[day_count].get_trade_date(),
                   one_day_avg["5"],
                   one_day_avg["3"],
                   one_day_avg["6"],
                   one_day_avg["8"],
                   after_datas[day_count].get_close()
                )
              )
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






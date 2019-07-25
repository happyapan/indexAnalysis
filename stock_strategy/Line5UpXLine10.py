# 5日线上穿10日线，股价收盘价站上10日线

import tools.TimeUtil as timeUtil
from stock.BaseStock import BaseStock
from stock_analysis.Avg import Avg
import tools.PrintUtil as pt
import IndexConstants as constant
from stock.StockDayData import StockDayData


# 判断该股票在某天的股价，是否站上10日线，并且5日线向上突破10日线，形成金叉
def analysis_stock(stock_code, stock_name, trade_data):
    base = BaseStock("base")
    avg = Avg()
    avg_result = avg.get_avg(stock_code, stock_name)

    trade_data_avg = None
    try:
        trade_data_avg = avg_result[trade_data]
    except:
        pass

    if trade_data_avg is None:
        return None

    current_stock_data = base.get_pre_stock_data(stock_code, trade_data, 0)
    pre_stock_data = base.get_pre_stock_data(stock_code, trade_data, -1)

    pre_trade_data_avg = avg_result[pre_stock_data.get_trade_date()]

    if pre_stock_data is not None \
            and trade_data_avg["5"] > trade_data_avg["10"] \
            and current_stock_data.get_close() > trade_data_avg["5"] \
            and pre_trade_data_avg["5"] < pre_trade_data_avg["10"] \
            and pre_stock_data.get_close() < pre_trade_data_avg["10"] \
            and pre_stock_data.get_close() > pre_trade_data_avg["5"]:
        return current_stock_data

    return None


if __name__ == '__main__':
    base = BaseStock("base")
    stock = base.get_all_stock()
    trade_data = "20190723"
    print("Start---" + trade_data)
    for one in stock:
        shoot_stock = analysis_stock(one, stock[one], trade_data)
        if shoot_stock is not None:
            print("______________"+shoot_stock.get_trade_date())
            after_n_day_trade = base.query_stock_data(shoot_stock.get_ts_code(),
                                                      stock[one],
                                                      shoot_stock.get_trade_date(),
                                                      timeUtil.day_after_day(trade_data, 2)
                                                      )
            pt.p_file_list_with_no_format_add(constant.date_file_path + "Line5Up10_20190723.txt", after_n_day_trade)
            end_trade = after_n_day_trade[0]
            start_trade = after_n_day_trade[-1]
            trade_diff = end_trade.get_close() - start_trade.get_close()
            first_day_msg = "No1 %.2f  rate: %.2f" % (trade_diff, 100 * trade_diff / start_trade.get_close())

            second_trade = after_n_day_trade[-2]
            second_trade_diff = end_trade.get_close() - second_trade.get_close()

            sed_day_msg = "No2 %.2f  rate: %.2f" % (
            second_trade_diff, 100 * second_trade_diff / second_trade.get_close())

            pt.p_file_no_format_add(constant.date_file_path + "Line5Up10_20190723.txt",
                                    [first_day_msg, sed_day_msg])

# for i in range(15):
    #     trade_data = timeUtil.day_after_day("20190723", -1 * i)
    #     print("Start---" + trade_data)
    #     for one in stock:
    #         shoot_stock = analysis_stock(one, stock[one], trade_data)
    #         if shoot_stock is not None:
    #             after_n_day_trade = base.query_stock_data(shoot_stock.get_ts_code(),
    #                                                       stock[one],
    #                                                       shoot_stock.get_trade_date(),
    #                                                       timeUtil.day_after_day(trade_data, 10)
    #                                                       )
    #             pt.p_file_list_with_no_format(constant.date_file_path + "Line5Up10_20190723.txt", after_n_day_trade)
    #             end_trade = after_n_day_trade[0]
    #             start_trade = after_n_day_trade[-1]
    #             trade_diff = end_trade.get_close() - start_trade.get_close()
    #             first_day_msg = "No1 %.2f  rate: %.2f" % (trade_diff, 100 * trade_diff / start_trade.get_close())
    #
    #             second_trade = after_n_day_trade[-2]
    #             second_trade_diff = end_trade.get_close() - second_trade.get_close()
    #
    #             sed_day_msg = "No2 %.2f  rate: %.2f" % (
    #             second_trade_diff, 100 * second_trade_diff / second_trade.get_close())
    #
    #             pt.p_file_no_format_add(constant.date_file_path + "Line5Up10_20190723.txt",
    #                                     [first_day_msg, sed_day_msg])

# 5日线上穿10日线，股价收盘价站上10日线

import tools.TimeUtil as timeUtil
from stock.BaseStock import BaseStock
from stock_analysis.Avg import Avg
import tools.PrintUtil as pt
import IndexConstants as constant
from stock.StockDayData import StockDayData


# 判断该股票在某天的股价，是否站上10日线，并且5日线向上突破10日线，形成金叉
from stock_analysis.Boll import Boll


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

    if pre_stock_data is None:
        return None

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
    avg = Avg()
    ball = Boll()

    for i in range(3):
        trade_data = timeUtil.day_after_day("20190726", -1*i)
        print("Start---" + trade_data)
        result_file_path = constant.date_file_path + "Line5Up10_" + trade_data + ".txt"
        pt.p_file_no_format_add(result_file_path,
                                ["code,date,O,H,L,C,P,Diff,R,count,sum,avg5,avg10,avg20,up_track,avg_line,down_track".replace(",", "	")])
        for one in stock:
            shoot_stock = analysis_stock(one, stock[one], trade_data)
            if shoot_stock is not None:
                print(" %s(%s):%s" % (stock[one],one, shoot_stock.get_trade_date()))

                after_n_day_trade = base.get_stock_data(shoot_stock.get_ts_code(),
                                                          stock[one],
                                                          shoot_stock.get_trade_date(),
                                                          timeUtil.day_after_day(trade_data, 10)
                                                          )
                message = []
                shoot_avg_result = avg.get_avg(one, stock[one])
                shoot_ball_result = ball.get_boll(one, stock[one])
                for one_stock_data in after_n_day_trade:
                    one_messgae = str(one_stock_data)

                    try:
                        shoot_avg_result[one_stock_data.get_trade_date()]
                        one_messgae= one_messgae + ",%s,%s,%s" % (
                            shoot_avg_result[one_stock_data.get_trade_date()]['5'],
                            shoot_avg_result[one_stock_data.get_trade_date()]['10'],
                            shoot_avg_result[one_stock_data.get_trade_date()]['20']
                        )
                    except:
                        one_messgae = one_messgae + ",_,_,_"

                    try:
                        one_messgae = one_messgae + ",%s,%s,%s" % (
                            shoot_ball_result[one_stock_data.get_trade_date()]['up_track'],
                            shoot_ball_result[one_stock_data.get_trade_date()]['avg_line'],
                            shoot_ball_result[one_stock_data.get_trade_date()]['down_track']
                        )
                    except:
                        one_messgae = one_messgae + ",_,_,_"

                    message.append(one_messgae.replace(",", "	"))

                pt.p_file_list_with_no_format_add(result_file_path, message)

                pt.p_file_no_format_add(result_file_path,
                                        [" %s(%s):%s" % (stock[one], one, shoot_stock.get_trade_date())])

